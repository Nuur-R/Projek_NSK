import multiprocessing
import time
def print_cube():
    for i in range(0,5):
        print('process 1 '+str(i))
        time.sleep(3)
    print('process 1 end')
def print_square():
    for i in range(0,5):
        print('process 2 = = = = ='+str(i))
        time.sleep(1)
    print('process 2 end')
    
if __name__ == "__main__":
    # creating processes
    p1 = multiprocessing.Process(target=print_square, args=())
    p2 = multiprocessing.Process(target=print_cube, args=())

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