from pydantic import BaseModel, EmailStr, Field
from typing import Optional
from datetime import datetime

class UserCreate(BaseModel):
    username: str = Field(..., min_length=3, max_length=50, example="dev_warrior")
    email: EmailStr = Field(..., example="hello@example.com")
    full_name: Optional[str] = Field(None, example="Alex Builder")

class TaskCreate(BaseModel):
    title: str = Field(..., min_length=1, max_length=200, example="Complete Module 2")
    priority: int = Field(..., ge=1, le=5, description="1 is low, 5 is high", example=5)
    due_date: Optional[datetime] = Field(None, example="2026-12-31T23:59:59")
  
