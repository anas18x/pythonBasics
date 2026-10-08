import threading
import time

def take_orders():
    for i in range(1,4):
        print(f"taking order for {i}")
        time.sleep(1)
        
def make_orders():
    for i in range(1,4):
        print(f"making order for {i}")
        time.sleep(5)


#creating therads
order_thread = threading.Thread(target=take_orders)    
making_thread = threading.Thread(target=make_orders)

order_thread.start()    
making_thread.start()    

order_thread.join()    
making_thread.join()  

print("both task finished")  

