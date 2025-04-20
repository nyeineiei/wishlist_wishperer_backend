# Generate and decode JWT tokens
from datetime import datetime, timedelta
from jose import jwt, JWTError
from typing import Dict
from fastapi import HTTPException, status

# TODO: move these into env/config later
SECRET_KEY = "your-secret-key"
ALGORITHM = "HS256"

class TokenService:
    def create_access_token(self, data: Dict, expires_in_minutes: int = 60) -> str:
        to_encode = data.copy()
        expire = datetime.utcnow() + timedelta(minutes=expires_in_minutes)
        to_encode.update({"exp": expire})
        return jwt.encode(to_encode, SECRET_KEY, algorithm=ALGORITHM)

    def decode_access_token(self, token: str) -> Dict:
        try:
            payload = jwt.decode(token, SECRET_KEY, algorithms=[ALGORITHM])
            return payload
        except JWTError:
            raise HTTPException(
                status_code=status.HTTP_401_UNAUTHORIZED,
                detail="Invalid token"
            )