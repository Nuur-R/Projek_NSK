import os
import eel
import rfidReader as rfid
import mysqlConnection as conn
import multiprocessing

guiPath = os.path.dirname(os.path.realpath(__file__)) + '/GUI'
eel.init(guiPath)
eel.start("main.html", mode='edge',block=False)

dataPath=f'{os.path.dirname(os.path.realpath(__file__))}/data'

def updateData(dataaa):
    with open(dataPath+'/card.csv', 'w') as f:
        f.writelines(f'{dataaa}')
def readData():
    with open(dataPath+'/card.csv', 'r') as f:
        data = f.readline()
        return data
        
def readRFIDandWritetoCSV():
    while True:
        eel.sleep(1)
        data = rfid.rfid_reader()
        print('UID : '+data)
        updateData(data)
def readCSVandWritetoDB():
    while True:
        data = readData()
        conn.data_checker(data)
        


if __name__ == "__main__":
    # creating processes
    p1 = multiprocessing.Process(target=readRFIDandWritetoCSV, args=())
    p2 = multiprocessing.Process(target=readCSVandWritetoDB, args=())

    # starting process 1
    p1.start()
    # starting process 2
    p2.start()

    # wait until process 1 is finished
    p1.join()
    # wait until process 2 is finished
    p2.join()

    # both processes finished
    print("Done!")
        
# print("Main loop started")
# main()
# print("Main loop ended")