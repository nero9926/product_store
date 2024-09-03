from fastapi import FastAPI

app = FastAPI(
    title="product_store",
)


@app.get("/")
def read_root():
    return {"Hello": "World"}
