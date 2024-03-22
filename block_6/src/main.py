from enum import Enum
from pydantic import BaseModel, field_validator


class Status(BaseModel):
    status: str


class Category(BaseModel):
    id: int
    name: str


class Tag(BaseModel):
    id: int
    name: str


class Pet(BaseModel):
    id: int
    category: Category
    name: str
    photoUrls: list[str]
    tags: list[Tag]
    status: str

    @field_validator('status')
    def valid_status(cls, v: str) -> str:
        if v.lower() not in ['available', 'pending', 'sold']:
            raise ValueError('Error: Please, select only \'available\', \'pending\', \'sold\'')
        return v




base_json = """
{
  "id": 5556665565,
  "category": {
    "id": 1,
    "name": "string"
  },
  "name": "doggie",
  "photoUrls": [
    "string"
  ],
  "tags": [
    {
      "id": 0,
      "name": "string"
    }
  ],
  "status": "available"
}
"""

base_pet = Pet.parse_raw(base_json)
base_header = {"Content-Type": "application/json", "accept": "application/json"}
base_status = Status(status = 'sold')