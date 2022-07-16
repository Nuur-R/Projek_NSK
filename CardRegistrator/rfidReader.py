import serial
import time

arduino = serial.Serial(port='COM7', baudrate=9600, timeout=.1)

def rfid_reader():
    time.sleep(0.05)
    data = arduino.readline().decode("utf-8")
    return data 