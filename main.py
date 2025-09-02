from fastapi import FastAPI
from enum import Enum

app = FastAPI()


@app.get("/")
async def root():
    return {"message": "Hello World"}

food_items = {
    'indian': ["Dosa", "Samosa", "Chana"],
    'amrican': ["Pizza", "Burger", "Hot dog"],
    'itlian': ["Pasta", "Noodle", "Soup"]
}

class AvailableFoodItem(str, Enum):
    indian = "indian",
    amrican = "amrican",
    itlian = "itlian"

@app.get("/get-item/{cuisine}")
async def get_single_item(cuisine: AvailableFoodItem):
    # items = food_items.get(cuisine)
    # if not items:
    #     return f"{cuisine} not found"
    return food_items.get(cuisine)