from sqlalchemy.orm import Session
from datetime import datetime
import sys

sys.path.append('.')
from data_structure import models, schemas


# for customer table
def get_customer(db: Session, customer_id: int):
    return db.query(models.Customer).filter(models.Customer.id == customer_id).first()


def get_customer_by_email(db: Session, email: str):
    return db.query(models.Customer).filter(models.Customer.email == email).first()


def get_customers(db: Session, skip: int = 0, limit: int = 100):
    return db.query(models.Customer).offset(skip).limit(limit).all()


def create_customer(db: Session, customer: schemas.CustomerCreate, address: schemas.AddressCreate):
    fake_hashed_password = customer.password + "notreallyhashed"
    db_customer = models.Customer(email=customer.email, firstname=customer.firstname, lastname=customer.lastname,
                                  last_logged_in=int(round(datetime.now().timestamp())), gender=customer.gender,
                                  phone_number=customer.phone_number, is_active=customer.is_active,
                                  password=fake_hashed_password,
                                  created_on=int(round(datetime.now().timestamp())))
    db.add(db_customer)
    db.commit()
    db.refresh(db_customer)
    #print(dir(db_customer))
    db_address = models.Address(customer_id=db_customer.id, line1=address.line1, line2=address.line2, city=address.city,
                                state=address.state,
                                country=address.country,
                                pincode=address.pincode)
    db.add(db_address)
    db.commit()
    db.refresh(db_address)
    return db_customer

def create_purchase(db: Session, id:int, product: list[schemas.ProductCreate]):
    am=[i.price for i in product ]
    print(am)
    db_purchase= models.Purchases(amount=sum(am), purchase_date=int(round(datetime.now().timestamp())),customer_id=id)
    db.add(db_purchase)
    db.commit()
    db.refresh(db_purchase)
    for p in product:
        db_product=models.Product(name=p.name, price=p.price, type=p.type, purchase_id=db_purchase.id)
        db.add(db_product)
        db.commit()
        db.refresh(db_product)

def create_verification(db: Session, id:int, doc:bytes, typeq:str):

    db_verification = models.Verification(customer_id=id,file=doc, type=typeq)
    db.add(db_verification)
    db.commit()
    db.refresh(db_verification)

