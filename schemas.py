"""
Database Schemas

Define your MongoDB collection schemas here using Pydantic models.
These schemas are used for data validation in your application.

Each Pydantic model represents a collection in your database.
Model name is converted to lowercase for the collection name:
- User -> "user" collection
- Product -> "product" collection
- BlogPost -> "blogs" collection
"""

from pydantic import BaseModel, Field, EmailStr
from typing import Optional


class AppUser(BaseModel):
    """
    Users collection schema
    Collection name: "appuser" (lowercase of class name)
    """
    email: EmailStr = Field(..., description="User email (unique)")
    password_hash: str = Field(..., description="Hashed password (bcrypt)")
    role: str = Field("user", description="Role: user or admin")
    name: Optional[str] = Field(None, description="Display name")


class DocxRequest(BaseModel):
    text: str
    font_family: str = Field("Times New Roman")
    font_size_global: float = Field(12.0, ge=6, le=72)
    font_size_paragraph: float = Field(12.0, ge=6, le=72)
    h1_size: float = Field(24.0, ge=6, le=96)
    h2_size: float = Field(18.0, ge=6, le=96)
    h3_size: float = Field(14.0, ge=6, le=96)
    line_spacing: float = Field(1.15, description="Line spacing multiplier")
    margin_top_mm: float = Field(25.4, description="Top margin in mm")
    margin_bottom_mm: float = Field(25.4, description="Bottom margin in mm")
    margin_left_mm: float = Field(25.4, description="Left margin in mm")
    margin_right_mm: float = Field(25.4, description="Right margin in mm")
