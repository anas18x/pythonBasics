class Parent:
    def __init__(self,type,strength):
        print("Parent class constructor")
        self.type = type
        self.strength = strength
        
   
        
# class Child(Parent):
#     def __init__(self,type,strength,level):
#         # super().__init__()
#         print("Child class constructor")
#         self.type = type
#         self.strength = strength
#         self.level = level
        
#     def childMethod(self):
#         print("Child class method")        
        
        
class Child(Parent):
    def __init__(self, type, strength,level):
        super().__init__(type,strength)
        self.level = level
        
        
        
childA = Child("masala",2,5)