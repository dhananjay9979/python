from threading import *
from time import sleep
class hello(Thread):
    def run(self):
        for i in range(5):
            print('hello')
            sleep(1)

class hi(Thread):
    def run(self):
        for i in range(5):
            print('hi')
            sleep(1)

t1=hello()
t2=hi()
# to execute simultaniously
t1.start()
sleep(0.2) #to avoid collision of threads
t2.start()
# to avoid collision with main thread(main thread will execute after t1 and t2)
t1.join()
t2.join()
print("bye") #main tread