# Problem 2: DevOps Scripts in Python

This folder contains the Python script solutions for the second problem statement of the AccuKnox DevOps Trainee assessment. We have chosen to implement **Objective 1 (System Health Monitoring)** and **Objective 4 (Application Health Checker)**.

## 1. System Health Monitoring Script (`health_monitor.py`)

This script monitors the health of the local system by checking key resources: CPU usage, memory usage, and disk space. It is designed to be proactive, logging the status to both the console and a persistent file (`system_health.log`). If any resource exceeds a predefined threshold, it will raise a clear alert.

### Setup and Execution

You can install the necessary library and run the script with the following commands:

```bash
# 1. Install the required psutil library
pip install psutil

# 2. Execute the script
python health_monitor.py
Example Output (Normal Conditions)
2025-09-20 17:30:00,123 - INFO - --- Starting System Health Check ---
2025-09-20 17:30:01,234 - INFO - OK: CPU usage is normal: 15.4%
2025-09-20 17:30:01,235 - INFO - OK: Memory usage is normal: 45.8%
2025-09-20 17:30:01,236 - INFO - OK: Disk space is normal: 55.2% used
2025-09-20 17:30:01,237 - INFO - INFO: Total number of running processes: 254
2025-09-20 17:30:01,238 - INFO - --- System Health Check Finished ---
Example Output (Alert Conditions)
This shows an example of the script successfully detecting and alerting on high memory usage.

2025-09-20 17:21:14,691 - WARNING - ALERT: High memory usage detected: 91.3%
