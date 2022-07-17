import multiprocessing
import time
import rfidReader
import dataManagemen
import mysqlConnection

def rfid():
    while True:
        data = rfidReader.rfid_reader()
        # print('UID : '+data)
        dataManagemen.updateData(data)
        
def readData():
    while True:
        data = dataManagemen.readData()
        print('CSV : '+data)
        # dataManagemen.dataMatch(data)
        mysqlConnection.data_checker(data)
        time.sleep(1)
        
def process1():
    while True:
        print('process 1= = = = =')
        time.sleep(1)
    
def process2():
    while True:
        print('process 2 = = = = =')
        time.sleep(0.1)
    
if __name__ == "__main__":
    # creating processes
    p1 = multiprocessing.Process(target=rfid, args=())
    p2 = multiprocessing.Process(target=readData, args=())

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
    # rfid()