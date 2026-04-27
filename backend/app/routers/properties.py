from fastapi import APIRouter, Depends, HTTPException, Query
from sqlalchemy.orm import Session
from sqlalchemy import select, and_
from typing import List, Optional
from app.database import get_db
from app.models.property import Property
from app.schemas.property import PropertyCreate, PropertyResponse, PropertyUpdate

router = APIRouter(prefix="/api/properties", tags=["Properties"])


@router.post("/", response_model=PropertyResponse, status_code=201)
def create_property(
    data: PropertyCreate,
    db: Session = Depends(get_db)
):
    property = Property(**data.model_dump())
    db.add(property)
    db.commit()
    db.refresh(property)
    return property


@router.get("/", response_model=List[PropertyResponse])
def get_properties(
    location: Optional[str] = Query(None),
    min_price: Optional[float] = Query(None),
    max_price: Optional[float] = Query(None),
    bedrooms: Optional[int] = Query(None),
    property_type: Optional[str] = Query(None),
    limit: int = Query(20, le=100),
    offset: int = Query(0, ge=0),
    db: Session = Depends(get_db)
):
    query = db.query(Property)

    if location:
        query = query.filter(Property.location.ilike(f"%{location}%"))
    if min_price is not None:
        query = query.filter(Property.price >= min_price)
    if max_price is not None:
        query = query.filter(Property.price <= max_price)
    if bedrooms is not None:
        query = query.filter(Property.bedrooms == bedrooms)
    if property_type:
        query = query.filter(Property.property_type == property_type)

    return query.offset(offset).limit(limit).all()


@router.get("/{property_id}", response_model=PropertyResponse)
def get_property(property_id: int, db: Session = Depends(get_db)):
    property = db.query(Property).filter(Property.id == property_id).first()

    if not property:
        raise HTTPException(status_code=404, detail="Property not found")

    return property


@router.put("/{property_id}", response_model=PropertyResponse)
def update_property(
    property_id: int,
    data: PropertyUpdate,
    db: Session = Depends(get_db)
):
    property = db.query(Property).filter(Property.id == property_id).first()

    if not property:
        raise HTTPException(status_code=404, detail="Property not found")

    update_data = data.model_dump(exclude_unset=True)
    for field, value in update_data.items():
        setattr(property, field, value)

    db.commit()
    db.refresh(property)
    return property


@router.delete("/{property_id}", status_code=204)
def delete_property(property_id: int, db: Session = Depends(get_db)):
    property = db.query(Property).filter(Property.id == property_id).first()

    if not property:
        raise HTTPException(status_code=404, detail="Property not found")

    db.delete(property)
    db.commit()