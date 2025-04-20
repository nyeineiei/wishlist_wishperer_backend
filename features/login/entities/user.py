from dataclasses import dataclass

@dataclass
class UserEntity:
    email: str
    hashed_password: str