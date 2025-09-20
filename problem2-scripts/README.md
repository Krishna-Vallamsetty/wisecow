# Problem 2: DevOps Scripts in Python

This repository contains the Python script solutions for the second problem statement of the AccuKnox DevOps Trainee assessment. We have chosen to implement **Objective 1 (System Health Monitoring)** and **Objective 4 (Application Health Checker)**.

## 1. System Health Monitoring Script (`health_monitor.py`)

This script monitors the health of the local system, checking CPU usage, memory usage, and disk space. It logs the status to both the console and a file named `system_health.log`.

### Setup
The script requires the `psutil` library. You can install it using pip:
```bash
pip install psutil
