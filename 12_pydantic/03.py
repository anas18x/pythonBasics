from pydantic import BaseModel, field_validator

class Person(BaseModel):
    firstName: str
    lastName: str
    
    @field_validator("firstName","lastName")
    def checkName(cls, v):
            if not v.isalpha():
                raise ValueError("Name must be alphabetic")
            return v