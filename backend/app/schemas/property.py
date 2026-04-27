from pydantic import BaseModel, Field
from typing import Optional, List
from datetime import datetime

# Used when CREATING a property (input)
class PropertyCreate(BaseModel):
    title: str = Field(..., min_length=3, max_length=255, example="Spacious 3BHK in Koramangala")
    description: Optional[str] = Field(None, example="Modern apartment with great natural light")
    price: float = Field(..., gt=0, example=4500000.0)
    location: str = Field(..., example="Koramangala, Bangalore")
    bedrooms: int = Field(..., ge=1, le=20, example=3)
    bathrooms: int = Field(..., ge=1, le=20, example=2)
    area_sqft: float = Field(..., gt=0, example=1200.0)
    property_type: str = Field(..., example="apartment")

# Used when RETURNING a property (output)
class PropertyResponse(BaseModel):
    id: int
    title: str
    description: Optional[str]
    price: float
    location: str
    bedrooms: int
    bathrooms: int
    area_sqft: float
    property_type: str
    images: List[str] = []
    ai_analysis: dict = {}
    created_at: datetime

    class Config:
        from_attributes = True  # allows converting SQLAlchemy model → Pydantic

# Used when UPDATING a property (all fields optional)
class PropertyUpdate(BaseModel):
    title: Optional[str] = None
    description: Optional[str] = None
    price: Optional[float] = None
    location: Optional[str] = None
    bedrooms: Optional[int] = None
    bathrooms: Optional[int] = None
    area_sqft: Optional[float] = None
    property_type: Optional[str] = None