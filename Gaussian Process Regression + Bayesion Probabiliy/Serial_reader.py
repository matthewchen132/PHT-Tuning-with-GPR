import numpy as np
from scipy import stats
import matplotlib.pyplot as plt
import serial 
import time

# Instructions:
# (1) Make sure Serial just prints sensor reading in the line
# (2) Configure line below for amount of data wanted
numReadings = 100
# (3) Run


sensor_serial = serial.Serial(port="COM5", baudrate=921600, timeout=1)
time.sleep(2)  # for setup phase
sensor_array = np.array([])

while True:
    print("\n")
    if sensor_serial.in_waiting > 0:
        serial_reading = sensor_serial.readline()  # Read one full line
        # print(f"Raw Bytes: {serial_reading}")  # Check if binary or text
        try:
            decoded_data = serial_reading.decode("utf-8").strip()
            print(f"Decoded: {decoded_data}")
            if(len(sensor_array) == 0):
                sensor_array = np.append(sensor_array, decoded_data)
                print("data appended")
            elif(float(decoded_data) != float(sensor_array[-1])):
                sensor_array = np.append(sensor_array, float(decoded_data))
                print(f"Sensor Array: {sensor_array}") 
            else:
                print("waiting for new data")
        except UnicodeDecodeError:
            print("Received non-text data. Check encoding.")
        if(sensor_array.size == numReadings):
            break
    else:
        print("No data received.")
    
    time.sleep(0.2)  # Avoid spamming CPU
