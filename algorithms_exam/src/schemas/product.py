from pydantic import BaseModel


class ProductEntity(BaseModel):
    id: int
    name: str
