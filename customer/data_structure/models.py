from sqlalchemy import Boolean,Column,ForeignKey,Integer,String, BigInteger,PrimaryKeyConstraint,FLOAT,UniqueConstraint,LargeBinary
from sqlalchemy.orm import relationship
from datetime import datetime
from data_structure.database import Base

class Customer(Base):
    __tablename__="customer"
    __tableargs__=(PrimaryKeyConstraint('id'),UniqueConstraint('id','email'))

    id=Column(Integer,primary_key=True,autoincrement=True, index=True)
    email=Column(String)
    password=Column(String)
    firstname=Column(String)
    lastname=Column(String)
    gender=Column(String)
    phone_number=Column(BigInteger)
    is_active=Column(Boolean)
    last_logged_in=Column(BigInteger)
    created_on=Column(BigInteger)

    purchases = relationship('Purchases')
    addresses=relationship('Address')
    verification=relationship('Verification', uselist=False)

class Address(Base):
    __tablename__="address"
    __tableargs__ = (PrimaryKeyConstraint('id'))

    id=Column(Integer,primary_key=True,autoincrement=True, index=True)
    customer_id=Column(Integer,ForeignKey('customer.id'))
    line1=Column(String)
    line2=Column(String)
    city=Column(String)
    state=Column(String)
    country=Column(String)
    pincode=Column(BigInteger)



class Verification(Base):
    __tablename__ = "verification"
    __tableargs__ = (PrimaryKeyConstraint('id'))

    id = Column(Integer,primary_key=True, autoincrement=True, index=True)
    customer_id = Column(Integer, ForeignKey('customer.id'))
    type=Column(String)
    file=Column(LargeBinary)



class Purchases(Base):
    __tablename__ = "purchases"
    __tableargs__ = (PrimaryKeyConstraint('id'))

    id = Column(Integer,primary_key=True, autoincrement=True, index=True)
    customer_id = Column(Integer, ForeignKey('customer.id'))
    amount=Column(FLOAT)
    purchase_date=Column(BigInteger)

    products=relationship("Product")

class Product(Base):
    __tablename__ = "product"
    __tableargs__ = (PrimaryKeyConstraint('id'))

    id = Column(Integer,primary_key=True, autoincrement=True, index=True)
    purchase_id=Column(Integer,ForeignKey('purchases.id'))
    name=Column(String)
    price=Column(FLOAT)
    type=Column(String)


