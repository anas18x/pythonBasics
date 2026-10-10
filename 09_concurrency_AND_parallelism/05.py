import threading
import time

counter = 0

def increment():
    global counter

    temp = counter          # Read shared value
    time.sleep(0.1)          # Pause to let the other thread run
    counter = temp + 1       # Write updated value

thread1 = threading.Thread(target=increment)
thread2 = threading.Thread(target=increment)

thread1.start()
thread2.start()

thread1.join()
thread2.join()

print(counter)
###################################################
#Both threads can read the same initial value before either writes its result.
#this is race condition
#We use a Lock to protect the critical section, the code that must not be executed concurrently by competing threads.


counter = 0
#lets us protect a critical section so that only one thread at a time can execute it while holding the lock.
lock = threading.Lock()

def increment2():
    global counter

    with lock:
        temp = counter
        time.sleep(0.1)
        counter = temp + 1

thread1 = threading.Thread(target=increment2)
thread2 = threading.Thread(target=increment2)

thread1.start()
thread2.start()

thread1.join()
thread2.join()

print(counter)  # 2