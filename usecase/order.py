# usecase/order.py
from abc import ABC, abstractmethod
from typing import Callable

from domain.order import Order as OrderDomain
from resource.request import OrderRequest
from usecase.kitchen import Kitchen, KitchenInterface


class OrderInputPort(ABC):
    @abstractmethod
    async def place_order(self, request: OrderRequest):
        pass


class OrderOutputPort(ABC):
    @abstractmethod
    async def order_ready(self, order: OrderDomain):
        pass


def OrderInputFactory(kitchen: KitchenInterface) -> Callable[[OrderOutputPort], OrderInputPort]:
    def factory(output_port: OrderOutputPort) -> OrderInputPort:
        return Order(kitchen, output_port)
    return factory


class Order(OrderInputPort):
    def __init__(self, kitchen: KitchenInterface, output_port: OrderOutputPort):
        self.kitchen = kitchen
        self.output_port = output_port

    async def place_order(self, request: OrderRequest):
        order = OrderDomain(dish_name=request.dish_name)
        await self.kitchen.cook_order(order)
        return await self.output_port.order_ready(order)
