import os
import eel
from random import randint
import rfidReader as rfid

print('Starting CardRegistrator')
eel.init(f'{os.path.dirname(os.path.realpath(__file__))}/GUI')
print('Starting GUI')
eel.start("main.html", mode='edge',block=False)

def main():
    print('Starting main')
    while True:
        eel.sleep(0.01)
        data = rfid.rfid_reader()
        print(data)
        eel.rfidData(data)
        
print("Main loop started")
main()
print("Main loop ended")