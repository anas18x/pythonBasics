def generatorFn():
    yield "cup 1 : chai"
    yield "cup 2 : lemon chai"
    yield "cup 3 : chai-samosa"
    
stall = generatorFn()    
print(stall)