# adapter/controller/presenter/customer.py
from http import HTTPStatus
from typing import Callable
from urllib.request import Request

from usecase.order import OrderOutputPort
from domain.order import Order


def OrderOutputFactory() -> Callable[[], OrderOutputPort]:
    def factory() -> OrderOutputPort:
        return Customer()

    return factory


class Customer(OrderOutputPort):
    async def order_ready(self, order: Order):
        print(f"Your order of {order.dish_name} is ready!")
        return {HTTPStatus.OK: order.dish_name}

