# domain/order.py

from pydantic import BaseModel


class Order(BaseModel):
    dish_name: str
