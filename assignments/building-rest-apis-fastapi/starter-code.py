"""
Starter code for Building REST APIs with FastAPI assignment
"""

from fastapi import FastAPI
from typing import List

app = FastAPI()

items = []

@app.get("/")
def read_root():
    return {"message": "Welcome to the FastAPI assignment!"}

@app.post("/items")
def create_item(name: str):
    item = {"id": len(items) + 1, "name": name}
    items.append(item)
    return item

@app.get("/items")
def list_items() -> List[dict]:
    return items

@app.put("/items/{item_id}")
def update_item(item_id: int, name: str):
    for item in items:
        if item["id"] == item_id:
            item["name"] = name
            return item
    return {"error": "Item not found"}

@app.delete("/items/{item_id}")
def delete_item(item_id: int):
    for item in items:
        if item["id"] == item_id:
            items.remove(item)
            return {"message": "Item deleted"}
    return {"error": "Item not found"}
