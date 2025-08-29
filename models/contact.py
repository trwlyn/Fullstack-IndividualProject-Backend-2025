from pydantic import BaseModel, EmailStr

class Contact(BaseModel):
    id: int = None
    name: str
    email: EmailStr
    subject: str
    message: str
