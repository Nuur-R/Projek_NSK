import serial
import time
import os

arduino = serial.Serial(port='COM7', baudrate=115200, timeout=.1)
path=f'{os.path.dirname(os.path.realpath(__file__))}/data'

def updateData(dataaa):
    with open(path+'/card.csv', 'w') as f:
        f.writelines(f'{dataaa}')

def rfid_reader():
    time.sleep(0.05)
    data = arduino.readline().decode("utf-8")
    updateData(data)
    return data

def main():
    while True:
        print(rfid_reader())
        
main()