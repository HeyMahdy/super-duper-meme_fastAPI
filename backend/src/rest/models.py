from typing import Optional

from pydantic import BaseModel
from sqlalchemy import String, ForeignKey, TIMESTAMP, text
from sqlalchemy.orm import Mapped, mapped_column, relationship
from database_config.Config import Model1Base

class User(Model1Base):
    __tablename__ = "users"

    id: Mapped[int] = mapped_column(primary_key=True)
    name: Mapped[str] = mapped_column(String, nullable=False ,index=True)
    email: Mapped[str] = mapped_column(String, nullable=False,unique=True, index=True)
    password: Mapped[str] = mapped_column(String,nullable=False)
    created_at: Mapped[str] = mapped_column(TIMESTAMP(timezone=True), nullable=False ,server_default=text('now()'))

class Address(Model1Base):
    __tablename__ = "addresses"

    id: Mapped[int] = mapped_column(primary_key=True)
    street: Mapped[str] = mapped_column(String)
    city: Mapped[str] = mapped_column(String, index=True)
    zip_code: Mapped[str] = mapped_column(String, index=True)
    address_id: Mapped[Optional[int]] = mapped_column(ForeignKey("users.id"))
    address: Mapped["User"] = relationship("User")




class AddressCreate(BaseModel):
    street: str
    city: str
    zip_code: str
    model_config = {
        'from_attributes': True  # Use from_attributes in Pydantic v2 instead of orm_mode
    }

class UserCreate(BaseModel):
    name: str
    email: str
    password: str
    model_config = {
        'from_attributes': True  # Use from_attributes in Pydantic v2 instead of orm_mode
    }
class UserLogin(BaseModel):
    email: str
    password: str

class Token(BaseModel):
    access_token: str
    token_type: str


class TokenData(BaseModel):
    username: str | None = None

class UserResponse(BaseModel):
    name: str
    email: str

    model_config = {
        'from_attributes': True  # Allows conversion from SQLAlchemy model
    }
class getAddresses(BaseModel):
    name : str
