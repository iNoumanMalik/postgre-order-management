from database import Base, engine
from models import User, Product, Order, OrderItem

Base.metadata.create_all(engine) #Looks into all tables registered in Base.metadata. Generates SQL to create them in the database

