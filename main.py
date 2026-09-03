from fastapi import FastAPI, Request
from mockData import products
from dtos import productDTO

app = FastAPI()


@app.get("/")
def home():
    return "Home Page"

@app.get("/products")
def get_product():
    return products


# path params
@app.get("/product/{product_id}")
def get_product_by_id(product_id: int):
    # if product_id in products -> return product else return error message 
    #product = None
    for oneProduct in products:
        if oneProduct.get("id") == product_id:
            return oneProduct
        

    return {
        "error": "Product not found for this id"
    }


## Query Params
@app.get("/greet")
def greet_user(request: Request):
    query_params = dict(request.query_params)
    return {
        "greet": f"Hello {query_params.get('name')}, Your age is {query_params.get('age')}."
    }
    

# Practicing Query Params 
@app.get("/practice")
def practice_query_params(request: Request):
    #print(dict(request.query_params))
    return {
        
        "query_params": dict(request.query_params),
        "greet": f"Hello {request.query_params.get('name')}, Sex {request.query_params.get("sex")}, Age {request.query_params.get("age")}"
            
    }


@app.post("/create_product")
def create_product(product_data: productDTO):
    
    product_data = product_data.model_dump()
    products.append(product_data)
    
    return {
        "status": "product created successfully",
        "data": products
    }
    
#Update product
@app.put("/update_product/{product_id}")
def update_product(product_data: productDTO,product_id: int):
    for index, oneProduct in enumerate(products):
        if oneProduct.get("id") == product_id:
            products[index] = product_data.model_dump()
            return {
                "status": "Product Details Updated Successfully...",
                "product_details": product_data
            }
        
    return {
        "error": "ID invailed",
        
    }
    
    
# Delete method
@app.delete("/delete_content/{product_id}")
def delete_content(product_id: int):
    for index, product in enumerate(products):
        if product.get("id") == product_id:
            deleted_product = products.pop(index)
            return {
                "status": "Product Deleted Successffuly",
                "del_item": deleted_product
            }
    return {
        "error":  "no product was found with this index number"
    }