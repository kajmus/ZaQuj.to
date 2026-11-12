from pydantic import BaseModel

#user_register_schema
class UserRegister(BaseModel):
    name: str 
    password: str


class SessionVerifySchema(BaseModel):
    session_id: int