from fastapi.encoders import jsonable_encoder
from src.db_config import db
from src.models.user_model import User

users_collection = db.get_collection("users")


# Save user
async def saveUser(user: User):
    user = jsonable_encoder(user)
    result = await users_collection.insert_one(user)
    res = await users_collection.find_one(
        {"_id": result.inserted_id}
    )
    return res
