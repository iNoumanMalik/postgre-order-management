from sqlalchemy import Column, Integer, String, Float, ForeignKey, DateTime
from sqlalchemy.orm import relationship
from datetime import datetime
from database import Base

class User(Base):
    __tablename__ = "users"
    id: Column(Integer,primary_key=True)
    name: Column(String, nullable=False)
    email: Column(String, nullable=False)
    created_at: Column(DateTime, default=datetime.utcnow)
    
    orders = relationship("Order",back_populates="user")

class Product(Base):
    __tablename__ = "products"
    id: Column(Integer,primary_key=True)
    name: Column(String, nullable=False)
    price: Column(Float, nullable=False)
    sku: Column(String, unique=True, nullable=False)
    created_at: Column(DateTime, default=datetime.utcnow)
    
    order_items = relationship("OrderItem",back_populates="product")
    
    
class Order(Base):
    __tablename__ = "orders"
    id: Column(Integer,primary_key=True)
    user_id: Column(Integer, ForeignKey(users.id))
    created_at: Column(DateTime, default=datetime.utcnow)
    
    user = relationship("User",back_populates="orders")
    items = relationship("OrderItem",back_populates="order")
    
    

class OrderItem(Base):
    __tablename__ = "orderitems"
    id: Column(Integer,primary_key=True)
    product_id: Column(Integer, ForeignKey(products.id))
    order_id: Column(Integer, ForeignKey(orders.id))
    quantity: Column(Integer,default=1)
    
    order = relationship("Order",back_populates="items")
    Product = relationship("Product",back_populates="order_items")
    
