from fastapi import FastAPI, Request
from mockData import products

app = FastAPI()

@app.get("/")
def home():
    return "Welcome Home"

##path params
@app.get("/get_product_by_id/{product_id}")
def get_one_product(product_id: int):
    #product = None
    for product in products:
        if product.get("id") == product_id:
            return product
    return {
        "error": "NO product is available with this id"
    }


# query params
@app.get("query_product")
def get_product_by_id(request: Request):
    return {
        "product_name" : dict(request.get_query_params("name"))
    }
    
    
@app.get("/products")
def return_products():
    return {'product': products}
    
    
@app.get("/item/{item_id}")
def get_item_by_id(item_id: int):
    for item in products:
        if item.get("id") == item_id:
            return item
        
    return {
        "error": "No Item is available with this ID"
    }
    

## query params

@app.get("/query")
def serve_query(request: Request):
    return {
        "metadata": request.query_params.get("name")
    }
    
@app.get("/request")
def serve_request(request: Request):
    l = dict(request.query_params)
    return {
        "input_recived": l
    }
    
    
@app.post("/create_product")
def create_product():
    return {
        "msg": "Product created successfully"
    }