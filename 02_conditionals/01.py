isAllowed = False

if isAllowed:
    print("user is allowed")
else:
    print("user not allowed")
    
#-----------------------------------------

preferedSnack = input("enter your prefered snacks : ").lower()
if(preferedSnack == "chai"):
    preferedCupSize = input("enter cup sizes (small,medium) : ").lower()
    if(preferedCupSize != "small" and preferedCupSize != "medium"):
        print("unknown cup size")
    else:
        print("order placed")
else :
    print("item unavailable")
  
# ---------------------------------------------
orderAmount = int(input("enter ur order amount : "))
delivery_fee = 0 if orderAmount > 300 else 30
print(f"delivery fee is -> {delivery_fee}")
        
        
#----------------------------------------------------
seat_type = input("eneter ur prefered seat type (sleeper/ac/general) : ").lower()

match seat_type:
    case "sleeper":
        print(f"u choose {seat_type}")
    case  "ac":    
        print(f"u choose {seat_type}")
    
    case _:
        print("invalid seat type")    