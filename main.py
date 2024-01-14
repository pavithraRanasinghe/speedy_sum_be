from fastapi import Body, FastAPI, status
from fastapi.middleware.cors import CORSMiddleware

from src.models.user_model import User
import src.services.user_service as user_service;

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins={"*"},
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.post("/save", response_description="Save new User", status_code=status.HTTP_201_CREATED, response_model=User)
async def save(user: User = Body(...)):
   res = await user_service.saveUser(user)
   return res