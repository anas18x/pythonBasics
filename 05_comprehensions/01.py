# Comprehensions are concise way to create lists, sets, dictionaries


#LIST-COMPREHENSION
menu = [
    "masala chai",
    "iced lemon tea",
    "ginger chai"
]

# first way
iced_tea = list(filter(lambda tea: "iced" in tea, menu))
print(iced_tea)

# comprehension
# the first tea (at the very beginning of the expression) is the output expression that determines what value gets added to the new list.
icedTea = [tea for tea in menu if "iced" in tea]
print(icedTea)

#################################################################

# SET-COMPREHENSION
favorite_chais = [
    "masala chai",
    "green tea",
    "masala chai",
    "lemon tea",
    "green tea"
]

unique_chai = {chai for chai in favorite_chais}
print(unique_chai)



################################################################

# DICTIONARY-COMPREHENSION
tea_prices = {
    "masala chai" : 40,
    "lemon chai" : 50,
}

tea_prices_usd = {tea:price/80 for tea , price in tea_prices.items()}
print(tea_prices_usd)


#################################################################

# GENERATOR-COMPREHENSION
daily_sales = [5,10,15,2,20]
salesInfo = (sale for sale in daily_sales if sale > 5)
print(salesInfo)
    






