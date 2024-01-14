from fastapi import APIRouter,status, Body, HTTPException
from fastapi.encoders import jsonable_encoder
from src.config.db_config import db
from src.models.auth_request import AuthRequest
from src.models.user_model import User

users_collection = db.get_collection("users")

router = APIRouter(
    prefix="/user",
    tags=["user"]
)

@router.post("/", response_description="Save new User", status_code=status.HTTP_201_CREATED, response_model=User)
async def saveUser(user: User = Body(...)):
    user = jsonable_encoder(user)
    result = await users_collection.insert_one(user)
    res = await users_collection.find_one(
        {"_id": result.inserted_id}
    )
    return res

@router.post("/login", response_description="Log in User", status_code=status.HTTP_200_OK, response_model=User)
async def logIn(authRequest: AuthRequest = Body(...)):
    print(authRequest)
    doc = await users_collection.find_one({"email":authRequest.username, "password": authRequest.password})

    if not doc:
        raise HTTPException(status_code=401, detail="Username & Password does not match")
    
    print(doc)
    return doc