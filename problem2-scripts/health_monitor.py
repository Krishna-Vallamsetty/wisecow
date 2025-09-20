
import psutil
import logging
from datetime import datetime

# --- CONFIGURATION ---
# Define the thresholds for alerts. You can change these values.
CPU_THRESHOLD_PERCENT = 80.0
MEMORY_THRESHOLD_PERCENT = 80.0
DISK_THRESHOLD_PERCENT = 80.0
LOG_FILE = "system_health.log"

# --- LOGGING SETUP ---
# Configure logging to output to both a file and the console.
logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(levelname)s - %(message)s',
    handlers=[
        logging.FileHandler(LOG_FILE),
        logging.StreamHandler()
    ]
)

def check_cpu_usage():
    """Checks the current CPU usage and logs an alert if it exceeds the threshold."""
    # Get CPU usage over a 1-second interval.
    cpu_usage = psutil.cpu_percent(interval=1)
    if cpu_usage > CPU_THRESHOLD_PERCENT:
        logging.warning(f"ALERT: High CPU usage detected: {cpu_usage}%")
    else:
        logging.info(f"OK: CPU usage is normal: {cpu_usage}%")

def check_memory_usage():
    """Checks the current memory usage and logs an alert if it exceeds the threshold."""
    memory_info = psutil.virtual_memory()
    memory_usage_percent = memory_info.percent
    if memory_usage_percent > MEMORY_THRESHOLD_PERCENT:
        logging.warning(f"ALERT: High memory usage detected: {memory_usage_percent}%")
    else:
        logging.info(f"OK: Memory usage is normal: {memory_usage_percent}%")

def check_disk_space():
    """Checks the disk space usage for the root partition and logs an alert if it exceeds the threshold."""
    # For Windows, psutil.disk_usage('C:') would be more specific. '/' works for the main drive.
    disk_info = psutil.disk_usage('/')
    disk_usage_percent = disk_info.percent
    if disk_usage_percent > DISK_THRESHOLD_PERCENT:
        logging.warning(f"ALERT: Low disk space detected: {disk_usage_percent}% used")
    else:
        logging.info(f"OK: Disk space is normal: {disk_usage_percent}% used")

def check_running_processes():
    """Logs the total number of running processes."""
    process_count = len(psutil.pids())
    logging.info(f"INFO: Total number of running processes: {process_count}")

def main():
    """Main function to run all health checks."""
    logging.info("--- Starting System Health Check ---")
    check_cpu_usage()
    check_memory_usage()
    check_disk_space()
    check_running_processes()
    logging.info("--- System Health Check Finished ---")

if __name__ == "__main__":
    main()
