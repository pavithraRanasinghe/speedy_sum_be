from fastapi import  FastAPI
from fastapi.middleware.cors import CORSMiddleware

from src.routers import user_route,service_route

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins={"*"},
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.get("/")
def read_root():
    # res= summarize()
    # print(res)
    return {"Hello": "World"}

app.include_router(user_route.router)
app.include_router(service_route.router)