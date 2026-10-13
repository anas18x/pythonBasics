from pydantic import BaseModel

class Product(BaseModel):
    id : int
    name : str
    price : float
    in_stock : bool = True
    

class User(BaseModel):
    id : int
    name : str
    is_active : bool
    
    
# input_data = {"id":101, "name":"xyz", "is_active" : True}    
# user = User(**input_data)

productOne = Product(id=1, name="phone", price=100)
productTwo = Product(id=1, name="phone", price=100, in_stock=False)
