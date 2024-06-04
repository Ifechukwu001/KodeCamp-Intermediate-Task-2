from typing import Annotated
from fastapi import FastAPI, Query

app = FastAPI()


@app.get("/items")
def items(
    name: Annotated[str, Query()],
    category: Annotated[str, Query()],
    price: Annotated[float, Query()],
):
    return {"name": name, "category": category, "price": price}
