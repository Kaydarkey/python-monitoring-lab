import psutil
import time
import os

def clear_screen():
    os.system('cls' if os.name == 'nt' else 'clear')

def system_monitor():
    while True:
        # Clear the screen
        clear_screen()

        # Get CPU usage
        cpu_usage = psutil.cpu_percent(interval=1)

        # Get memory usage
        memory_info = psutil.virtual_memory()
        memory_usage = memory_info.percent
        memory_total = memory_info.total // (1024 ** 2)  # in MB
        memory_available = memory_info.available // (1024 ** 2)  # in MB

        # Get disk usage
        disk_info = psutil.disk_usage('/')
        disk_usage = disk_info.percent
        disk_total = disk_info.total // (1024 ** 3)  # in GB
        disk_used = disk_info.used // (1024 ** 3)  # in GB
        disk_free = disk_info.free // (1024 ** 3)  # in GB

        # Get network statistics
        net_info = psutil.net_io_counters()
        bytes_sent = net_info.bytes_sent // (1024 ** 2)  # in MB
        bytes_received = net_info.bytes_recv // (1024 ** 2)  # in MB

        # Display the information
        print("=== System Monitor ===")
        print(f"CPU Usage: {cpu_usage}%")
        print(f"Memory Usage: {memory_usage}% ({memory_available} MB available / {memory_total} MB total)")
        print(f"Disk Usage: {disk_usage}% ({disk_used} GB used / {disk_total} GB total, {disk_free} GB free)")
        print(f"Network: {bytes_sent} MB sent / {bytes_received} MB received")

        # Wait for a short period before refreshing
        time.sleep(1)

# Run the monitor
if __name__ == "__main__":
    system_monitor()
