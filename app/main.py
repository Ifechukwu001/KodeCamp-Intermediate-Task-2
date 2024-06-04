from typing import Annotated
from fastapi import FastAPI, Query, Body
from pydantic import BaseModel, EmailStr

app = FastAPI()


@app.get("/items")
def items(
    name: Annotated[str, Query()],
    category: Annotated[str, Query()],
    price: Annotated[float, Query()],
):
    return {"name": name, "category": category, "price": price}


@app.get("/search")
def search(
    query: Annotated[str, Query()],
    page: Annotated[int, Query(ge=1)] = 1,
    size: Annotated[int, Query(ge=1)] = 3,
):
    animals = [
        "dog",
        "cat",
        "fish",
        "bird",
        "rabbit",
        "hamster",
        "turtle",
        "snake",
        "lizard",
        "iguana",
        "catfish",
        "lion",
        "giraffe",
        "penguin",
        "elephant",
        "ant",
        "spider",
        "bat",
        "monkey",
        "kangaroo",
        "zebra",
        "fox",
        "dolphin",
        "bear",
        "deer",
        "chimpanzee",
        "rhinoceros",
        "coyote",
        "wolverine",
        "cheetah",
        "hyena",
        "hippopotamus",
        "crocodile",
        "gorilla",
        "orangutan",
        "gazelle",
        "badger",
        "raccoon",
        "skunk",
        "opossum",
        "walrus",
    ]

    data = [animal for animal in animals if query in animal]
    offset = (page - 1) * size
    trimmed_data = data[offset : offset + size]

    result = {
        "next": f"/search?query={query}&page={page+1}&size={size}"
        if trimmed_data and trimmed_data[-1] != data[-1]
        else None,
        "previous": f"/search?query={query}&page={page-1}&size={size}"
        if page > 1
        else None,
        "data": trimmed_data,
    }
    return result


class Address(BaseModel):
    street: str
    city: str
    zip: str


class User(BaseModel):
    name: str
    email: EmailStr
    address: Address


@app.post("/users")
def users(profile: Annotated[User, Body(embed=True)]):
    return {"profile": profile}
