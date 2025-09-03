from pydantic import BaseModel
from typing import Optional

class User(BaseModel):
    id: int
    name: str
    age: int
    address: Optional[str] = None

obj = User(id=1, name="John", age="20",address="")