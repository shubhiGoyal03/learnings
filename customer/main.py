import json

from fastapi import Depends, FastAPI, HTTPException, UploadFile, Body
from sqlalchemy.orm import Session
from fastapi.responses import RedirectResponse, JSONResponse

from data_structure import crud, models, schemas
from data_structure.database import SessionLocal, engine

models.Base.metadata.create_all(bind=engine)

app = FastAPI()


# Dependency
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()


# create customer
@app.post("/customer/", response_model=schemas.Customer)
def create_customer(*, customer: schemas.CustomerCreate, address: schemas.AddressCreate, db: Session = Depends(get_db)):
    db_customer = crud.get_customer_by_email(db, email=customer.email)
    if db_customer:
        raise HTTPException(status_code=400, detail="Email already registered")
    return crud.create_customer(db=db, customer=customer, address=address)


# create verification for customer
@app.post("/verification/", response_model=schemas.Customer)
def create_verification(email: str, doc: UploadFile, db: Session = Depends(get_db)):
    db_customer = crud.get_customer_by_email(db,email)
    #print("ASDEFRGTYHUJI",doc.file.read())
    if db_customer:
        # print(crud.create_customer(db=db, customer=customer, doc=doc.file.read( ), type=doc.content_type, address=address))
        crud.create_verification(db,db_customer.id,doc.file.read(),doc.content_type)
        return db_customer
    else:
        raise HTTPException(status_code=400, detail="Email doesn't exists!")

@app.post("/purchase/", response_model=schemas.Customer)
def create_purchase(email: str, product: list[schemas.ProductCreate] ,db: Session = Depends(get_db)):
    db_customer = crud.get_customer_by_email(db,email)
    #print("ASDEFRGTYHUJI",doc.file.read())
    if db_customer:
        # print(crud.create_customer(db=db, customer=customer, doc=doc.file.read( ), type=doc.content_type, address=address))
        crud.create_purchase(db,db_customer.id,product)
        return db_customer
    else:
        raise HTTPException(status_code=400, detail="Email doesn't exists!")


@app.get("/customer/", response_model=list[schemas.Customer])
def read_customers(skip: int = 0, limit: int = 100, db: Session = Depends(get_db)):
    customers = crud.get_customers(db, skip=skip, limit=limit)
    for c in customers:
        print((c))
    return customers


@app.get("/customer/{customer_id}", response_model=schemas.Customer)
def read_customer(customer_id: int, db: Session = Depends(get_db)):
    db_customer = crud.get_customer(db, customer_id=customer_id)
    if db_customer is None:
        raise HTTPException(status_code=404, detail="Customer not found")
    return db_customer
