 
from passlib.context import CryptContext # Python library that handles secure password hashing. never store plain text passwords
from app.features.login.services.security_service_interface import SecurityServiceInterface

class SecurityService(SecurityServiceInterface):
    def __init__(self):
        self.pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")

    def hash_password(self, password: str) -> str:
        return self.pwd_context.hash(password)

    def verify_password(self, plain_password: str, hashed_password: str) -> bool:
        return self.pwd_context.verify(plain_password, hashed_password)

