from pydantic import BaseModel
from datetime import date

class ProductBase(BaseModel):
    name: str
    price: float
    type: str | None

class ProductCreate(ProductBase):
    pass

class Product(ProductBase):
    id: int
    purchase_id: int

    class Config:
        orm_mode = True

class PurchasesBase(BaseModel):
    pass

class PurchasesCreate(PurchasesBase):
    pass

class Purchases(PurchasesBase):
    id: int
    customer_id: int
    purchase_date: int
    amount: float
    products: list[Product] = []

    class Config:
        orm_mode = True

class VerificationBase(BaseModel):
    pass

class VerificationCreate(VerificationBase):
    pass

class Verification(VerificationBase):
    id: int
    customer_id : int
    type: str
    #file: str

    class Config:
        orm_mode=True

class AddressBase(BaseModel):
    line1: str
    line2: str | None
    city: str
    state: str
    country: str
    pincode: int

class AddressCreate(AddressBase):
    pass

class Address(AddressBase):
    id: int
    customer_id: int

    class Config:
        orm_mode=True

class CustomerBase(BaseModel):
    email: str
    firstname:str
    lastname: str | None
    gender: str
    phone_number : int
    is_active: bool
    #last_logged_in: int(datetime.now().strftime("%Y%m%d%H%M%S"))

class CustomerCreate(CustomerBase):
    password: str

    class Config:
        orm_mode=True


class Customer(CustomerBase):
    created_on: date
    id: int
    addresses: list[Address] = []
    verification: Verification= None
    purchases: list[Purchases] = []

    class Config:
        orm_mode=True
