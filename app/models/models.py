from pydantic import BaseModel, Field


class Product(BaseModel):
    product_id: int
    name: str
    category: str
    price: float | None = Field(default=None, gt=0)
