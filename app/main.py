from database import session
from crud import create_user, create_product, create_order

db = session()

user1 = create_user(db,"Nouman","nouman@emumba.com")
user2 = create_user(db,"Yashfa","yashfa@emumba.com")
product1 = create_product(db,"Laptop",125000.23,"L-123-B")
products = [
    {"product_id":product1.id, "quantity":1}
]
order = create_order(db,user1.id,products)

 