# Prometheus exporter for Folding@Home Client

Track all sorts of stats for all your Folding@Home clients! More to come!

## Tracked data

Based upon one of my sample clients:

### slot-info
```json
[
  {
    "id": "01",
    "status": "READY",
    "description": "cpu:9",
    "options": {"cpus": "9"},
    "reason": "",
    "idle": false
  }
]
```

### simulation-info
```json
{"user": "deadeye536", "team": "223518", "project": 0, "run": 0, "clone": 0, "gen": 0, "core_type": 0, "core": "", "total_iterations": 0, "iterations_done": 0, "energy": 0, "temperature": 0, "start_time": "<invalid>", "timeout": 0, "deadline": 0, "eta": 0, "progress": 0, "slot": 1}
```

### options
```json
{"allow": "127.0.0.1", "child": "true", "command-deny-no-pass": "0/0", "daemon": "true", "fold-anon": "true", "gpu": "false", "passkey": "xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx", "password": "xxxxxxxx", "pid-file": "/var/run/fahclient.pid", "power": "full", "proxy": ":8080", "run-as": "fahclient", "team": "223518", "user": "deadeye536"}
```

### slot-options
```json
{"client-type": "advanced", "paused": "false"}
```

### ppd
```
1006431.593709
```

