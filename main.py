#!/usr/bin/python3
# -*- coding: utf8 -*-
# vim: ts=4 sts=4 sw=4 et ai

import prometheus_client
import telnetlib
import json
import os
from pprint import pprint


class FAHClient:
    """Class to handle communications over telnet to FAHClient"""

    # Prompt sequence to scan for
    prompt = b"> "

    def __init__(self, host, port=36330, password=None, timeout=10):
        # Establish telnet session
        self.host = host
        self.port = port
        self.password = password
        self.timeout = timeout


    def __enter__(self):
        self.client = telnetlib.Telnet(self.host, self.port, self.timeout)

        # Get initial prompt and check it
        initial_prompt = self.client.read_until(self.prompt).decode("utf8")
        if not "Folding@home" in initial_prompt:
            raise Exception("Found something, but probably not the Folding@Home"
                "server at {0}:{1}. Expected to find \"Folding@home\" in text:\n{2}"
                .format(host, port, initial_prompt)
            )

        if self.password:
            self.auth(self.password)

        return self

    def __exit__(self, exc_type, exc_value, exc_tb):
        self.client.write(b"quit\n")
        self.client.read_all()

    def msg(self, message):
        # Send a message
        self.client.write(bytes(message + "\n", "utf8"))

        # Get response
        reply = self.client.read_until(self.prompt).decode("utf8")

        # Clean response
        pieces = [s for s in reply.splitlines() if s]
        pieces = filter(lambda x: not "PyON " in x, pieces)
        pieces = filter(lambda x: not x.startswith("---"), pieces)
        pieces = filter(lambda x: not x.startswith(self.prompt.decode("utf8")), pieces)

        reply = os.linesep.join(pieces)

        return reply

    def json(self, message):
        reply = self.msg(message)
        # We get back python-style 'False' and 'True' which is invalid JSON
        reply = reply.replace("False", "false").replace("True", "true")
        return json.loads(reply)

    def auth(self, password):
        test_command = self.msg("help")

        # If the command responds normally, we can skip the auth
        if not "ERROR: unknown command" in test_command:
            return True

        auth_reply = self.msg("auth " + password)

        if "OK" in auth_reply:
            return True

        raise Exception("Failed to authenticate with Folding@Home server at "
            "{0}:{1}. Got response:\n{2}".format(self.host, self.port, auth_reply)
        )

if __name__ == "__main__":
    with FAHClient("192.168.1.20", "36330", "Foobar1234") as client:
        print(client.msg("ppd"))
        pprint(client.json("info"))
        pprint(client.json("options"))
        pprint(client.json("queue-info"))
        pprint(client.json("slot-info"))
        pprint(client.json("simulation-info 01"))

