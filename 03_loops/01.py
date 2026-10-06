for count in range(1,11):
    print(f"current count is {count}")


# users = ["anas","anish","anon"]

# for user in users:
#     print(f"{user}")
    
    
#------------------------------------------    
menu = ["dish1",'dish2',"dish3"]    
for dish in menu:
    print(f"{dish}")

print(list(enumerate(menu)))  

for index, item in enumerate(menu, start=1):
    print(f"{index} : {item}")  



# #--------while
temp = 40
while temp <= 100:
    print(f"current temp {temp}")
    temp+=10 
    
    
numbers = [1,2,3,4,5,6,7,8,9]
for number in numbers:
    if number == 5:
        print(f"current number is {number}")
        break
    
    if number == 3:
        print(f"current number is {number}")
        continue

   
    
#---------- walrus - walrus is an assignment expression that allows you to assign a value to a variable as part of an expression. It is denoted by the := operator.
value = 12
if(not (remainder := value % 2)):
    print(f"remainder is {remainder} and value is even")
    
    

#---------------------
available_items = ["item1","item2","item3"]
if (item := input("enter item name : ")) in available_items:
        print(f"{item} is available")
else :
    print(f"{item} is not available")    
    
    
 #------------------------------------------
users = [
      {"name": "anas", "age": 25},
      {"name": "anish", "age": 30},
      {"name": "anon", "age": 35}
]  

for user in users:
    # print(f"user name is {user['name']} and age is {user['age']}")
    print(user)
    
    
    
    
#------TYPES    

#pure fn -> pure function is a function that always produces the same output for the same input and has no side effects. It does not modify any external state or variables. It only depends on its input parameters to produce a result.
def pure_fn(a, b):
    return a + b

# impure fn -> impure function is a function that may produce different outputs for the same input or has side effects. It may modify external state or variables, or depend on external factors to produce a result.
def impure_fn(a, b):
    global c
    c = a + b
    return c


def recursive_fn(n):
    return "count reaches 0" if n==0 else recursive_fn(n-1)


#lambdas(anaonymous functions) -> lambda function is a small anonymous function that can take any number of arguments, but can only have one expression. It is defined using the lambda keyword.
add = lambda a, b: a + b

userroles = ["admin","user","guest"]
list(filter(lambda role: role=="admin", userroles))  # filter function is used to filter the elements of a list based on a condition. It takes a function and a list as arguments and returns a new list containing only the elements that satisfy the condition defined in the function.

list(map(lambda role: role.upper(), userroles))  # map function is used to apply a function to all the elements of a list. It takes a function and a list as arguments and returns a new list containing the results of applying the function to each element of the original list.