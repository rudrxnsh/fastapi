from pydantic import BaseModel

class productDTO(BaseModel):
    id: int 
    product_name: str 
    price: float 
    description: str