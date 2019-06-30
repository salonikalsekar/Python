from threading import *
from time import sleep

class Thread1(Thread):
    def run(self):
        for i in range(4):
            print("thread1")
            sleep(1)


class Thread2(Thread):
    def run(self):
        for i in range(4):
            print("thread2")
            sleep(1)



a1 = Thread1()
sleep(0.2)
b1 = Thread2()

a1.start()
b1.start()


# we need to ask the main thread to wait till the two threads get over
a1.join()
b1.join()

print("bye")

# start is to start the thread
# execution takes time so we put sleep