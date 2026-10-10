import time
from multiprocessing import Process

def calculate():
    total = 0
    for i in range(20_000):
        total += i

# this is called the main guard, it ensures that the code inside it is only executed when the script is run directly, not when it is imported as a module in another script.
if __name__ == "__main__":
    start = time.perf_counter()

    p1 = Process(target=calculate, args=())
    p2 = Process(target=calculate, args=())

    p1.start()
    p2.start()

    p1.join()
    p2.join()

    print(f"Time: {time.perf_counter() - start:.2f}s")


