
from fastapi import FastAPI, Depends

# from graphene import ObjectType, Schema, List, Field, Int , String
# from sqlalchemy.orm import Session, joinedload

# from starlette_graphene3 import GraphQLApp, make_graphiql_handler

# from database_config.Config import  SessionLocal
from rest.models import Address, User

from rest.routers import router



app = FastAPI()
app.include_router(router,prefix="/api")

# class AddressQl(ObjectType):
#     id = Int()
#     street = String()
#     city = String()
#     zip_code = String()



# class UserQL(ObjectType):
#     id = Int()
#     name = String()
#     email = String()
#     address = Field(lambda : AddressQl)

#     @staticmethod
#     def resolve_address (root,info):
#         return root.address



# class Query(ObjectType):
#     addresses = List(AddressQl)
#     users = List(UserQL)

#     @staticmethod
#     def resolve_addresses(root, info):
#         return SessionLocal().query(Address).all()

#     @staticmethod
#     def resolve_users(root, info):
#         return SessionLocal().query(User).options(joinedload()).all()

# schema = Schema(query=Query)

# app.mount("/graphql", GraphQLApp(schema=schema, on_get=make_graphiql_handler()))



