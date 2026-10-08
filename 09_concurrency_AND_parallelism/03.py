import threading
import time

def task():
    print("Task started")
    time.sleep(5)
    print("Task completed")
    
thread = threading.Thread(target=task)
thread.start()

print("Main thread continues to run while the task is being executed in a separate thread.")    




### in case we want to wait for the thread to finish before continuing with the main thread, we can use the join() method:
def task2():
    print("Task started")
    time.sleep(5)  # Simulate a long-running task
    print("Task completed")

thread = threading.Thread(target=task2)
#controls starting the worker thread.
thread.start()

# makes the calling thread wait for it.
thread.join()  # Wait for the thread to finish

print("Worker finished, main thread continues execution.")    