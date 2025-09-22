# Problem 2: DevOps Scripts in Python

This repository contains the Python script solutions for the second problem statement of the AccuKnox DevOps Trainee assessment.

---

## 1. System Health Monitoring Script (`health_monitor.py`)

This script monitors the health of the local system by checking key resources: CPU usage, memory usage, and disk space.

### Setup and Execution

```
pip install psutil
python health_monitor.py
```
### Example Output
```bash
2025-09-20 17:30:01,234 - INFO - OK: CPU usage is normal: 15.4%
2025-09-20 17:30:01,235 - INFO - OK: Memory usage is normal: 45.8%
2025-09-20 17:30:01,236 - INFO - OK: Disk space is normal: 55.2% used
```
## 2. Application Health Checker (app_health_checker.py)
This script acts as an external uptime monitor. It checks the health of predefined web applications by making HTTP requests.

### Setup and Execution
```Bash
pip install requests
python app_health_checker.py
```
### Example Output
```Code snippet

2025-09-20 17:22:46,427 - INFO - UP: '[https://www.google.com](https://www.google.com)' is functioning correctly (Status Code: 200)
2025-09-20 17:22:48,560 - INFO - UP: '[https://www.github.com](https://www.github.com)' is functioning correctly (Status Code: 200)
2025-09-20 17:22:50,832 - ERROR - DOWN: '[http://httpbin.org/status/503](http://httpbin.org/status/503)' is not functioning correctly (Status Code: 503)
