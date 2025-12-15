from pydantic import BaseModel


# Базовая схема продукта
class Product(BaseModel):
    id: int
    name: str
