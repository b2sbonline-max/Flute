from pydantic import BaseModel, EmailStr, Field
from datetime import datetime
from typing import List, Optional

class UserBase(BaseModel):
    username: str = Field(..., min_length=3, max_length=50)
    email: EmailStr
    full_name: Optional[str] = None

class UserCreate(UserBase):
    password: str = Field(..., min_length=6)

class UserUpdate(BaseModel):
    email: Optional[EmailStr] = None
    full_name: Optional[str] = None
    is_active: Optional[bool] = None

class UserResponse(UserBase):
    id: int
    is_active: bool
    created_at: datetime
    last_login: Optional[datetime]
    
    class Config:
        from_attributes = True

class FieldBase(BaseModel):
    field_name_he: str
    field_name_en: str
    field_type: str = Field(..., pattern="^(varchar|integer|date|boolean|decimal)$")
    field_position: Optional[int] = None

class FieldCreate(FieldBase):
    pass

class FieldResponse(FieldBase):
    id: int
    table_name_en: str
    created_at: datetime
    
    class Config:
        from_attributes = True

class TableRegistryBase(BaseModel):
    table_name_en: str = Field(..., min_length=3, max_length=100)
    table_name_he: str = Field(..., min_length=3, max_length=100)

class TableRegistryCreate(TableRegistryBase):
    fields: List[FieldCreate]

class TableRegistryUpdate(BaseModel):
    table_name_he: Optional[str] = None

class TableRegistryResponse(TableRegistryBase):
    id: int
    created_by: int
    created_at: datetime
    updated_at: datetime
    fields: List[FieldResponse] = []
    
    class Config:
        from_attributes = True

class TokenResponse(BaseModel):
    access_token: str
    token_type: str = "bearer"
    user: UserResponse

class LoginRequest(BaseModel):
    username: str
    password: str

class MessageResponse(BaseModel):
    message: str
    success: bool
