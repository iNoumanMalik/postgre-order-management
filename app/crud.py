from sqlalchemy.orm import Session
from models import User, Product, Order, OrderItem

def create_user(db:Session,name:str,email:str):
    user = User(name=name,email=email)
    db.add(user)
    db.commit()
    db.refresh(user)
    return user

def create_product(db:Session, name:str,price:float,sku:str):
    product = Product(name=name,price=price,sku=sku)
    db.add(product)
    db.commit()
    db.refresh(product)
    return product

def create_order(db:Session,user_id:int, products):
    
    try:
        order = Order(user_id = user_id)
        db.add(order)
        
        for item in products:
            order_item = OrderItem(product_id = item["product_id"], order = order, quantity= item["quantity"])
            db.add(order_item)
        db.commit()
        db.refresh(order)
        return order
    
    except Exception:
        db.rollback()
        raise
