# adapter/controller/http/waiter.py
from fastapi import FastAPI, APIRouter
from usecase.order import OrderInputFactory, OrderOutputPort
from adapter.presenter.customer import OrderOutputFactory
from resource.request import OrderRequest


class Waiter:
    def __init__(self, router: APIRouter, input_factory: OrderInputFactory, output_factory: OrderOutputPort):
        self.input_factory = input_factory
        self.output_factory = output_factory

        @router.post("/order")
        async def handle_order(request: OrderRequest):
            output_port = self.output_factory()
            input_port = self.input_factory(output_port)
            return await input_port.place_order(request)

