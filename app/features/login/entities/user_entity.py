# Pydantic model. Used to validate/serialize JSON input/output (API request/response)
from dataclasses import dataclass

@dataclass
class UserEntity:
    email: str
    hashed_password: str