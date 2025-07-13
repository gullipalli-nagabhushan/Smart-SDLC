from pydantic import BaseModel,EmailStr
class LoginUser(BaseModel):
    email: EmailStr
    password: str
class RegisterUser(BaseModel):
    name: str
    email: EmailStr
    password: str
    
