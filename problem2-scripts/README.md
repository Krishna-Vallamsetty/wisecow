# Problem 2: DevOps Scripts in Python

This repository contains Python script solutions for the second problem statement of the AccuKnox DevOps Trainee assessment. I have chosen to implement Objective 1 (System Health Monitoring) and Objective 4 (Application Health Checker).

---

## 1. System Health Monitoring Script (`health_monitor.py`) 🖥️

This script monitors the health of the local system by checking key resources: **CPU usage**, **memory usage**, and **disk space**. It is designed to be proactive, logging the status to both the console and a persistent file (`system_health.log`). If any resource exceeds a predefined threshold, it will raise a clear alert.

### Setup and Execution

```bash
# 1. Install the required psutil library
pip install psutil

# 2. Execute the script
python health_monitor.py
Example Output (Normal Conditions)
Code snippet

2025-09-20 17:30:00,123 - INFO - --- Starting System Health Check ---
2025-09-20 17:30:01,234 - INFO - OK: CPU usage is normal: 15.4%
2025-09-20 17:30:01,235 - INFO - OK: Memory usage is normal: 45.8%
2025-09-20 17:30:01,236 - INFO - OK: Disk space is normal: 55.2% used


2. Application Health Checker (app_health_checker.py) 🌐
This script acts as an external uptime monitor. It checks the health of a list of predefined web applications by making HTTP requests and validating their status codes. It logs whether each application is UP (functioning correctly) or DOWN (unavailable or returning an error) to both the console and a file (app_health.log).

Setup and Execution
Bash

# 1. Install the required requests library
pip install requests

# 2. Execute the script
python app_health_checker.py
Example Output
Code snippet

2025-09-20 17:22:44,723 - INFO - --- Starting Application Health Checks ---
2025-09-20 17:22:46,427 - INFO - UP: '[https://www.google.com](https://www.google.com)' is functioning correctly (Status Code: 200)
2025-09-20 17:22:48,560 - INFO - UP: '[https://www.github.com](https://www.github.com)' is functioning correctly (Status Code: 200)
2025-09-20 17:22:50,832 - ERROR - DOWN: '[http://httpbin.org/status/503](http://httpbin.
