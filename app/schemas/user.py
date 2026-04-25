from pydantic import BaseModel

# inbound request body (like a CreateStudentDto in .NET)
class UserCreate(BaseModel):
    username: str
    first_name: str
    last_name: str
    password: str

# outbound response shape (like a StudentResponseDto)

class UserLogin(BaseModel):
    username: str
    password: str

class UserResponse(BaseModel):
    id: int
    username: str
    first_name: str
    last_name: str
    model_config = {"from_attributes": True}

class Token(BaseModel):
    access_token: str
    token_type: str

