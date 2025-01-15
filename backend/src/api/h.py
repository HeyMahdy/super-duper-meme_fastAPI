from fastapi import APIRouter

from models.base import  SimpleModel

router = APIRouter()

@router.get("/h")
def heh():
    # Create an instance of SimpleModel
    model_instance = SimpleModel(name="example", value=42)
    return {"model": model_instance.display()}
