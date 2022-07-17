from fastapi import FastAPI
from load import Articles

app = FastAPI()
articles = Articles()

@app.get("/items")
def list_items():
    return articles.get_all()

@app.get("/item/{id}")
def find_item(id: int):
    return articles.get_one(id)

@app.delete("/item/{id}")
def delete_item(id: int):
    articles.del_one(id)
    return "DELETED FROM DATABASE!"

