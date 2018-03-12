#Python multithreading example.
#1. Calculate factorial using recursion.
#2. Call factorial function using thread. 

#!/usr/bin/python3

import _thread
import threading
# import time

threadId = 1

# Define a function for the thread
def factorial(threadName, n):
   global threadId
   if n < 1:   # base case
       print("%s: %d" % ("Thread", threadId ))
       threadId += 1
       return 1
   else:
       returnNumber = n * factorial(threadName,  n - 1 )  # recursive call
       print(threadName + str(n) + '! = ' + str(returnNumber))
       return returnNumber

# Create two threads as follows
try:
    _thread.start_new_thread(factorial,("Thread-1: ", 5, ))
    _thread.start_new_thread(factorial,("Thread-2: ", 4, ))
    print("Umesh Running thread count")
    print(threading.activeCount())
except:
    print ("Error: unable to start thread")

while 1:
   pass

