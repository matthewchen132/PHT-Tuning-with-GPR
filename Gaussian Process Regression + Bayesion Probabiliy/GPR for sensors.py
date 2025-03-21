import numpy as np
import pandas as pd
import serial
import time
import logging

# Set up logging
logging.basicConfig(filename='sensor_data.log', level=logging.DEBUG)

def read_sensor_data(sensor_serial):
    try:
        if sensor_serial.in_waiting > 0:
            serial_reading = sensor_serial.readline()  # Read one full line
            decoded_data = serial_reading.decode("utf-8").strip()
            return decoded_data
    except UnicodeDecodeError:
        logging.error("Received non-text data. Check encoding.")
    return None

def main():
    sensor_data = []
    try:
        with serial.Serial(port="COM5", baudrate=921600, timeout=1) as sensor_serial:
            time.sleep(1)  # Allow sensor to initialize
            while True:
                decoded_data = read_sensor_data(sensor_serial)
                if decoded_data:
                    print(f"Decoded: {decoded_data}")
                    sensor_data.append(decoded_data)

                time.sleep(0.001)  # Manage CPU usage efficiently
    except KeyboardInterrupt:
        print("Program interrupted. Closing serial port.")
    finally:
        if sensor_data:
            sensor_df = pd.DataFrame(sensor_data, columns=['Sensor Reading'])
            sensor_df.to_csv('sensor_data.csv', index=False)
        else:
            logging.error("No sensor data collected.")

if __name__ == "__main__":
    main()
