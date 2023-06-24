# usecase/kitchen.py
from abc import ABC, abstractmethod

from domain.order import Order


class KitchenInterface(ABC):
    @abstractmethod
    async def cook_order(self, order: Order):
        pass


class Kitchen(KitchenInterface):
    async def cook_order(self, order: Order):
        return order
