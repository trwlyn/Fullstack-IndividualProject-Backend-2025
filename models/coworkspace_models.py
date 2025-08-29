from pydantic import BaseModel, Field
from typing import Optional

class Feature:
    id: int
    title: str
    description: str
    image_url: str
    is_active: bool

class PricingPlan:
    id: int
    name: str
    description: str
    price: float
    details: str
    is_popular: bool


class FeatureResponse(BaseModel):
    id: int
    title: str
    description: str
    image_url: str

    class Config:
        orm_mode = True

class PricingPlanResponse(BaseModel):
    id: int
    name: str
    description: str
    price: float = Field(..., description="Price in euros")
    details: str
    is_popular: Optional[bool] = False

    class Config:
        orm_mode = True