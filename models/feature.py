from pydantic import BaseModel

class Feature(BaseModel):
    id: int = None
    title: str
    description: str
    image_url: str
    is_active: bool = True
