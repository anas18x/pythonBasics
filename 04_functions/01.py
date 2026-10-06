# def add(a, b):
#     return a + b

# print(add(2, 3)) 


#------------------
def getUser(userEmail):
    if not "@" in userEmail:
        print("invalid email")
    else:
        print(f"user email is {userEmail}")    

userEmail = input("enter user email : ")
getUser(userEmail)        
        
        
#--------------------------------------------------------------------        
def update_order():
    flavour = "ginger"
    shop = "bakehouse"
    
    def inner():
        # in order to modiify global variable we can use global keyword to modify the value of a variable defined in the global scope from within a function.
        global shop 
        
        # non local - we can use nonlocal keyword to modify the value of a variable defined in the outer function from within the inner function.
        nonlocal flavour
        flavour = "chocolate"
        print(f"flavour inside inner function is {flavour}")     
    
    print(f"flavour inside outer function is {flavour}")
    inner()
    
update_order()    


#---------------
def print_user_info(name, age=25):
    print(f"user name is {name} and age is {age}")
    
print_user_info("anas")  # default age is 25    
print_user_info("anas", 30)   # positional arguments  
print_user_info(age=30, name="anas")   # keyword arguments


#----------------
def print_user_info2(*args, **extras):
    print(args)
    print(extras)
    
    print(f"user name is {args[0]} and age is {args[1]} and gender is {args[2]} and city is {extras['city']} and country is {extras['country']}")
    
    
print_user_info2("anas", 30, "male", city="delhi", country="india")    