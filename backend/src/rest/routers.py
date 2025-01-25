from datetime import timedelta
from typing import Annotated, List

from fastapi import Depends, APIRouter, HTTPException
from fastapi.security import OAuth2PasswordRequestForm

from sqlalchemy.orm import Session
from starlette import status

from Oauth import create_access_token, get_current_user
from database_config.Config import get_db
from rest.models import Address, User, AddressCreate, UserCreate, UserResponse, getAddresses
from utils import hash_password, verify_password

router = APIRouter()

@router.get("/a")
def hello():
    return {"hello": "world"}
@router.post("/address")
def creating_adress(ads : AddressCreate , db: Session = Depends(get_db) , current_user: User = Depends(get_current_user)):
    aka = Address(street=ads.street,city=ads.city,zip_code=ads.zip_code,address_id=current_user.id)
    db.add(aka)
    db.commit()
    db.refresh(aka)
    return aka

@router.post("/user",status_code=status.HTTP_201_CREATED,response_model=UserCreate)
def creating_user(addd : UserCreate ,db: Session = Depends(get_db)):
    aaa = User(name = addd.name , email = addd.email,password=hash_password(addd.password))
    db.add(aaa)
    db.commit()
    db.refresh(aaa)
    return aaa

@router.get("/address",status_code=status.HTTP_200_OK,response_model=List[AddressCreate])
def get_address(db : Session = Depends(get_db),current_user: User = Depends(get_current_user)):
    outAdress = db.query(Address).filter(Address.address_id == current_user.id).all()
    return outAdress

@router.get("/users/me/", response_model=UserResponse)
async def read_users_me(
    current_user: Annotated[User, Depends(get_current_user)],
):
    return current_user
@router.post("/login")
def creating_login(form_data: OAuth2PasswordRequestForm = Depends(),db: Session = Depends(get_db)):
    user = db.query(User).filter(User.email == form_data.username).first()
    if not user:
        raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED,detail="Incorrect username or password")

    if not verify_password(form_data.password, user.password):
        raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED,detail="password")
    access_token_expires = timedelta(minutes=15)
    access_token = create_access_token(
        data={"sub": form_data.username}, expires_delta=access_token_expires
    )
    return {"access_token": access_token, "token_type": "bearer"}






# get  e actually user depenecy use krte hbe










