#!/usr/bin/python
import threading # module used for multithreading
import time

exitFlag = 0

# myThread is used specifically here to encapsulate the behaviour
class myThread (threading.Thread): # threading.Thread is used for multithreading
    def __init__(self, threadID, name, counter, delay):
        threading.Thread.__init__(self) # creates thread
        self.threadID = threadID
        self.name = name
        self.counter = counter
        self.delay = delay
    
    def print_time(threadName, counter, delay):
        while counter:
            if exitFlag:
                threadName.exit()
            time.sleep(delay)
            print("%s: %s %d" % (threadName, time.ctime(time.time()),counter))
            print(f"Active count {threading.active_count()}, from thread {threading.current_thread()} with name {threading.current_thread().getName()}") # threading.active_count() gives number of active threads
            counter -= 1
        
    def run(self):
        print("Starting " + self.name)
        print(self)
        self.print_time(self.counter, self.delay)
        print("Exiting " + self.name)
    
# Create new threads

thread1 = myThread(1, "Thread-1", 1, 1)
thread2 = myThread(2, "Thread-2", 2, 2)
thread3 = myThread(3, "Thread-3", 3, 3)
thread4 = myThread(4, "Thread-4", 4, 4)
thread5 = myThread(5, "Thread-5", 5, 5)


# Start new Threads
thread1.start() # starts thread
thread2.start()
thread3.start()
thread4.start()
thread5.start()

thread1.join() # joins thread
thread2.join()
thread3.join()
thread4.join()
thread5.join()


print(f"Threads left: {threading.active_count()}, Exiting Main Thread")


# Answers to Questions

# a) 10 Seconds (if inclusive of first second)
#    If it was serial, it would need 20 seconds, therefore 2 threads with 10 seconds proves it is parallel
# b) - myThread encapsulates Thread behaviour
#    - threading.Thread class
#    - threading module
#    - threading.active_count() returns num active threads
#    - etc etc
# c) i. Done
#    ii. 25 seconds (if inclusive of the first second)
#        Since thread 5 was the longest, the time was limited by it
#    iii. active_count() returns number of active threads (master + number of created threads)
#         current_thread() returns info about where it was created as well as name
#         getName() is a member of current_thread() and returns the name (in this case, what we added)

