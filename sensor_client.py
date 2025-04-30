import socket

HOST = 'localhost'  # Same as server
PORT = 65432        # Same port as server

with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
    s.connect((HOST, PORT))
    print("Connected to sensor server.\n")
    while True:
        data = s.recv(1024)
        if not data:
            break
        print("Received:", data.decode())

