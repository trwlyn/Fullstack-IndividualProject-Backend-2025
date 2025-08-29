from pydantic import BaseModel
from decimal import Decimal

class PricingPlan(BaseModel):
    id: int = None
    name: str
    description: str
    price: Decimal
    details: str
    is_popular: bool = False
