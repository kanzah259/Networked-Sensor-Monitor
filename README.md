# Networked Sensor Monitor

This is a Python-based project where a sensor server sends simulated temperature and voltage data to a client using socket programming. The server continuously sends data, which the client then receives and displays.

## Installation

1. Clone the repository:
   ```bash
   git clone https://github.com/your-username/Networked-Sensor-Monitor.git
   ```
2. Navigate to the project folder:
   ```bash
   cd Networked-Sensor-Monitor
   ```

3. Install necessary dependencies (if any):
   ```bash
   pip install -r requirements.txt
   ```

## Running the Project

1. **Start the server**: 
   ```bash
   python sensor_server.py
   ```

2. **Start the client**:
   ```bash
   python sensor_client.py
   ```

The client will begin receiving data from the server, and the output will display the sensor readings.

## Features
- Real-time data simulation.
- Communication between server and client via TCP sockets.
- Customizable sensor data generation (temperature, voltage).

## Future Enhancements
- Implement additional sensor types (e.g., humidity, pressure).
- Add a graphical user interface for visualizing the data.
