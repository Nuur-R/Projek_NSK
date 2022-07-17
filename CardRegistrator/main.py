import eel
import os
import eel
from random import randint
import rfidReader as rfid
import dataManagemen as dm
import mysqlConnection as mc

@eel.expose
def hello():
    print("Hello from Python")

print('Starting CardRegistrator')
eel.init(f'{os.path.dirname(os.path.realpath(__file__))}/GUI')
print('Starting GUI')
eel.start("main.html", mode='edge',block=False)

def main():
    print('Starting main')
    while True:
        eel.sleep(0.01)
        data = rfid.rfid_reader()
        dm.updateData(data)
        print('1. Updated data Finish')
        data = dm.readData()
        print('2. Read data Finish')
        eel.sleep(1)
        mc.data_checker(data)
        print('3. Check data Finish')
        print(data)
        eel.rfidData(data)

print("Main loop started")
main()
print("Main loop ended") 