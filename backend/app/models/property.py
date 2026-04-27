from sqlalchemy import Column, Integer, String, Float, DateTime, Text, JSON
from sqlalchemy.sql import func
from app.database import Base

class Property(Base):
    __tablename__ = "properties"

    id = Column(Integer, primary_key=True, index=True)
    title = Column(String(255), nullable=False)
    description = Column(Text, nullable=True)
    price = Column(Float, nullable=False)
    location = Column(String(255), nullable=False)
    bedrooms = Column(Integer, nullable=False)
    bathrooms = Column(Integer, nullable=False)
    area_sqft = Column(Float, nullable=False)
    property_type = Column(String(50), nullable=False)  # apartment, house, villa
    images = Column(JSON, default=[])                   # list of image URLs
    ai_analysis = Column(JSON, default={})              # GPT-4 Vision results
    created_at = Column(DateTime(timezone=True), server_default=func.now())
    updated_at = Column(DateTime(timezone=True), onupdate=func.now())

    def __repr__(self):
        return f"<Property {self.title} - {self.location}>"