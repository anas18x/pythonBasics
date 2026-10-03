# for count in range(1,11):
#     print(f"current count is {count}")


# users = ["anas","anish","anon"]

# for user in users:
#     print(f"{user}")
    
    
#------------------------------------------    
# menu = ["dish1",'dish2',"dish3"]    
# for dish in menu:
#     print(f"{dish}")

# print(list(enumerate(menu)))  

# for index, item in enumerate(menu, start=1):
#     print(f"{index} : {item}")  



# #--------while
# temp = 40
# while temp <= 100:
#     print(f"current temp {temp}")
#     temp+=10 
    
    
flavours = ["ginger","tulsi","adrak","out of stock","discontinued"]
for flavour in flavours:    
    if flavour == "out of stock":
        continue
    if flavour == "discontinued":
        break
    print("discontinued item found")
    
    