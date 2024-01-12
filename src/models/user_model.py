import uuid
from bson import ObjectId
from typing import Optional
from pydantic import BaseModel, Field
from typing_extensions import Annotated
from pydantic.functional_validators import BeforeValidator

PyObjectId = Annotated[str, BeforeValidator(str)]

class User(BaseModel):
    id: int
    name: str
    email: str
    type: str
    password: str