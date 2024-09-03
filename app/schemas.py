from pydantic import BaseModel, EmailStr, ConfigDict
from datetime import datetime
from typing import Optional


class JournalBase(BaseModel):
    title: str
    content: str
    status: bool = False

class JournalCreate(JournalBase):
    pass

class UserOut(BaseModel):
    id: int
    email: EmailStr
    created_at: datetime

    class Config:
        #orm_mode = True
        model_config = ConfigDict(from_attributes=True)
        
class Journal(JournalBase):
    id: int
    created_at: datetime
    owner_id: int
    owner: UserOut

    class Config:
        #orm_mode = True
        model_config = ConfigDict(from_attributes=True)
    

class MoodBase(BaseModel):
     title: str
     content: str
     status: bool = False

class MoodCreate(MoodBase):
    pass


class Mood(MoodBase):
   id: int
   created_at: datetime
   owner_id: int
   owner: UserOut
   
   class Config:
        #orm_mode = True
        model_config = ConfigDict(from_attributes=True)


class UserCreate(BaseModel):
    email: EmailStr
    password: str



class UserLogin(BaseModel):
    email: EmailStr
    password: str

class Token(BaseModel):
    access_token: str
    token_type: str

class TokenData(BaseModel):
    id: Optional[str] = None