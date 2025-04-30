import socket
import random
import time

HOST = 'localhost'  # or your IP (127.0.0.1 works for localhost)
PORT = 65432        # Port to listen on

def generate_sensor_data():
    temp = round(random.uniform(20.0, 30.0), 2)  # Fake temp in °C
    voltage = round(random.uniform(3.0, 3.3), 2) # Fake voltage
    return f"Temp:{temp}C, Voltage:{voltage}V"

with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
    s.bind((HOST, PORT))
    s.listen()
    print("Sensor server running... waiting for connection.")
    conn, addr = s.accept()
    with conn:
        print(f"Connected by {addr}")
        while True:
            data = generate_sensor_data()
            conn.sendall(data.encode())
            time.sleep(1)  # Send every 1 second
