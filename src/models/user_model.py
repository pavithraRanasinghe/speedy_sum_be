from pydantic import BaseModel
from typing_extensions import Annotated
from pydantic.functional_validators import BeforeValidator

PyObjectId = Annotated[str, BeforeValidator(str)]

class User(BaseModel):
    id: int
    name: str
    email: str
    type: str
    password: str