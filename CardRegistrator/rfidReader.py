import serial
import time

# arduino = serial.Serial(port='COM7', baudrate=9600, timeout=.1)

def rfid_reader():
    arduino = serial.Serial(port='COM7', baudrate=9600, timeout=.1)
    time.sleep(1)
    data = arduino.readline().decode("utf-8")
    return data 
    

# while True:
#     # num = input("Enter a number: ")
#     value = rfid_reader()
#     print('process')
#     print(value)