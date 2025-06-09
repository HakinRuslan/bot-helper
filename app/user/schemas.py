from pydantic import BaseModel, ConfigDict, Field
from typing import Optional
from datetime import date

class UserBaseInDB(BaseModel):
    telegram_id: int

    model_config = ConfigDict(from_attributes=True)

class Usersch(UserBaseInDB):
    username: Optional[str] = Field(None)
    name: str