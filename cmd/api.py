# cmd/api.py is the entry point of the application.
from fastapi import FastAPI, APIRouter
from starlette.middleware.cors import CORSMiddleware

from adapter.controller.http.waiter import Waiter
from adapter.presenter.customer import OrderOutputFactory
from usecase.kitchen import Kitchen
from usecase.order import OrderInputFactory

app = FastAPI()

# CORS middleware
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


# Health check endpoint
@app.get("/health")
async def health_check():
    return {"status": "OK"}

# DI (Dependency Injection)
waiter_router = APIRouter(prefix="/test")
kitchen = Kitchen()
order_input_factory = OrderInputFactory(kitchen)
order_output_factory = OrderOutputFactory()
Waiter(waiter_router, order_input_factory, order_output_factory)

# add router
app.include_router(waiter_router)