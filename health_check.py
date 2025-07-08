import psutil
import datetime
from ping3 import ping
import os

# Create logs directory if it doesn't exist
os.makedirs("logs", exist_ok=True)


# Settings
THRESHOLDS = {
    "cpu": 85,
    "ram": 80,
    "disk": 90
}

LOG_FILE = "logs/system_log.txt"
PING_HOSTS = ["8.8.8.8", "google.com", "192.168.1.1"]

def log(message):
    timestamp = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    entry = f"[{timestamp}] {message}"
    print(entry)
    with open(LOG_FILE, "a", encoding="utf-8") as f:
        f.write(entry + "\n")

def check_resources():
    cpu = psutil.cpu_percent(interval=1)
    ram = psutil.virtual_memory().percent
    disk = psutil.disk_usage('/').percent

    log(f"CPU: {cpu}%, RAM: {ram}%, Disk: {disk}%")

    if cpu > THRESHOLDS["cpu"]:
        log("⚠️ High CPU usage!")
    if ram > THRESHOLDS["ram"]:
        log("⚠️ High RAM usage!")
    if disk > THRESHOLDS["disk"]:
        log("⚠️ Low Disk Space!")

def ping_hosts():
    for host in PING_HOSTS:
        latency = ping(host, timeout=2)
        if latency is None:
            log(f"❌ Ping to {host} FAILED.")
        else:
            log(f"✅ Ping to {host} succeeded ({round(latency * 1000)} ms)")

if __name__ == "__main__":
    log("=== Starting System Health Check ===")
    check_resources()
    ping_hosts()
    log("=== Check Complete ===\n")
