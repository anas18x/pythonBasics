from pydantic import BaseModel, Field, field_validator
from typing import List, Dict, Optional

class Cart(BaseModel):
    user_id : int
    items : List[str]
    quantity : Dict[str,int]
    productDescription : str = Field(
        ...,   #indicates the required field
        min_length=3,
        max_length=50
    )
    
    
userCart = Cart(
    user_id = 2,
    items = ["phones","keyboards"],
    quantity = {"phone":1, "keyboards":0},
    productDescription = "electronic items"
)    
    
    
###############################################################
class User(BaseModel):
    userName : str
    
    @field_validator('userName')    
    def userName_length(cls, v):
        if len(v) < 4:
            raise ValueError("username must be at 4char")
        return v    
    