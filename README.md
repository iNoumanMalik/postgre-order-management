# Order Management System

A simple **Order Management System** built with **PostgreSQL** and **SQLAlchemy ORM** in Python.

---

## Overview

This project demonstrates a standard relational database implementation using Python. Key concepts covered:
- **ORM Models**: Mapping Python classes to PostgreSQL tables.
- **Relationships**: Handling One-to-Many (User to Orders) and Many-to-One (OrderItem to Product).
- **Integrity**: Enforcing unique constraints and foreign keys.
- **Transactions**: Ensuring data consistency during multi-step orders.

---

## Database Design



### Entities & Relationships
* **User**: `id`, `name`, `email` (Unique)
* **Product**: `id`, `name`, `sku` (Unique), `price`
* **Order**: `id`, `user_id` (FK), `created_at`
* **OrderItem**: `id`, `order_id` (FK), `product_id` (FK), `quantity`

---

## Full Setup & Initialization

Copy and paste the following sections into your terminal or SQL tool as needed.

### 1. SQL Database Initialization
Run these commands in your `psql` terminal or pgAdmin Query Tool:

```sql
CREATE DATABASE order_db;
CREATE USER app_user WITH PASSWORD 'secret';
GRANT ALL PRIVILEGES ON DATABASE order_db TO app_user;
```

### 2. Create database and user:

CREATE DATABASE order_db;
CREATE USER app_user WITH PASSWORD 'secret';
GRANT ALL PRIVILEGES ON DATABASE order_db TO app_user;


### 3. Set up Python environment:

python -m venv venv
source venv/bin/activate
pip install sqlalchemy psycopg2-binary


### 4. Configure database URL in database.py:

POSTGRES_URL = "postgresql+psycopg2://app_user:secret@localhost:5432/order_db"


### 5. Create tables:

python create_tables.py

### 6. Run
python main.py
