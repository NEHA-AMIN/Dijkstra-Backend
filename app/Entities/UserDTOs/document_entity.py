from typing import Optional
from uuid import UUID
from datetime import datetime
from pydantic import BaseModel, validator

# ----------------------
# Input DTOs
# ----------------------
class CreateDocument(BaseModel):
    github_username: str
    latex: str
    base_structure: dict

    @validator('github_username')
    def github_username_cannot_be_empty(cls, v):
        if not v or not v.strip():
            raise ValueError('github_username cannot be empty')
        return v.strip()

    class Config:
        from_attributes = True


class UpdateDocument(BaseModel):
    latex: Optional[str] = None
    base_structure: Optional[dict] = None
    
    class Config:
        from_attributes = True


class ReadDocument(BaseModel):
    id: UUID
    profile_id: UUID
    latex: Optional[str] = None
    base_structure: Optional[dict] = None
    created_at: datetime
    updated_at: datetime
    
    class Config:
        from_attributes = True
