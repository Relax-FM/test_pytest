from enum import Enum
from pydantic import BaseModel, field_validator


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




input_json = """
{
  "id": 1,
  "category": {
    "id": 0,
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

try:
    pet = Pet.parse_raw(input_json)
except ValueError as e:
    print('Ex : ', e)
else:
    print(pet.json())