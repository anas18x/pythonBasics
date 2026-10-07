

# METHOD RESOLUTION ORDER

class Parent:
    label = "A : Base Class"
    
    
class Child_A(Parent):
    label = "Child-A Class"
    

class Child_B(Parent):
    label = "Child-B Class"
    
# whichever class is mentioned first in the inheritance list will be given priority in the method resolution order.
class X(Child_A, Child_B):
    pass
class X(Child_B, Child_A):
    pass
        

obj1 = X()
print(obj1.label)