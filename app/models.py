from app.database import Base
from sqlalchemy import Column, Integer, String, Numeric, Date, ForeignKey


class Product(Base):
    __tablename__="products"

    id = Column(Integer,primary_key=True)
    product_name = Column(String)
    category = Column(String)
    cost_price = Column(Numeric)
    selling_price = Column(Numeric)


class Branch(Base):
    __tablename__="branches"

    id = Column(Integer,primary_key=True)
    branch_name = Column(String)
    city = Column(String)


class Inventory(Base):
    __tablename__="inventory"

    id = Column(Integer,primary_key=True)
    product_id = Column(Integer,ForeignKey("products.id"))
    branch_id = Column(Integer,ForeignKey("branches.id"))
    stock_qty = Column(Integer)
    reorder_level = Column(Integer)


class Sale(Base):
    __tablename__="sales"

    id = Column(Integer,primary_key=True)
    product_id = Column(Integer)
    branch_id = Column(Integer)
    quantity = Column(Integer)
    sale_date = Column(Date)
    total_amount = Column(Numeric)


class Shrinkage(Base):
    __tablename__="shrinkage"

    id = Column(Integer,primary_key=True)
    product_id = Column(Integer)
    branch_id = Column(Integer)
    quantity_lost = Column(Integer)
    loss_date = Column(Date)