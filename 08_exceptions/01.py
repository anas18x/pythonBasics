orders = ["chai1","chai2"]
try:
    print(orders[2])
except IndexError:
    print(IndexError)    
    

def checkUserRole(role):
    try:
        if(role=="unknown"):
            raise ValueError("not allowed")   
    except ValueError as e:
        print(e)
    finally:
        print("always runs")    
        
# checkUserRole("unknown")        


########################################################

def processOrder(item,quantity):
    try:
        price = {"masala":20}[item]
        cost = price*quantity
        print(f"total cost is {cost}")
    except KeyError:
        print("not avalable")
    except TypeError:
        print("quantity must be a number")        
        
# processOrder("ginger",2)        
# processOrder("masala","two")        



#################################################
class UserCheckError(Exception):
    pass
    

def checkUserRole(role):
    roles = ["user","admin"]
    if role not in roles:
        raise UserCheckError("unauthorized")

    print("allowed")
    
 
try:    
   checkUserRole("user")    
   checkUserRole("x")
except UserCheckError as error:
    print(error)   
    
        
