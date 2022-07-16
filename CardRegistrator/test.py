import threading
import time
import rfidReader

def rfid():
    # while True:
    #     print('process 1 = = = = =')
    #     # time.sleep(1)
    rfidReader.main()
    
def print_square():
    while True:
        print('process 2 = = = = =')
        time.sleep(1)
    
if __name__ == "__main__":
    # creating processes
    p1 = threading.Thread(target=print_square, args=())
    p2 = threading.Thread(target=rfid, args=())

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