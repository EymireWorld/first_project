from pydantic import BaseModel, EmailStr


class User(BaseModel):
    first_name: str
    last_name: str
    username: str
    email: EmailStr
    balance: int
