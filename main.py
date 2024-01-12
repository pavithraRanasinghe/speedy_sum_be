from fastapi import Body, FastAPI, status

from src.models.user_model import User
import src.services.user_service as user_service;

app = FastAPI()

@app.post("/save", response_description="Save new User", status_code=status.HTTP_201_CREATED, response_model=User)
async def save(user: User = Body(...)):
   res = await user_service.saveUser(user)
   return res