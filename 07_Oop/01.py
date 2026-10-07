class Parent:
    origin = "India"
    
    def __init__(self, size):
        self.size = size
        print("Parent class constructor")
        print("size:", self.size)
        
    def parentMethod(self):
        print("Parent class method")
        print("Parent origin:", self.origin)
        print("Parent size:", self.size)
        
print(Parent.origin)
child = Parent("Large")
child.parentMethod()  
child.origin = "USA"
print(child.origin)     
print(Parent.origin)