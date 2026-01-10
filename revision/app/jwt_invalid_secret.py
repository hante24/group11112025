import jwt
from datetime import datetime, timedelta

SECRET_KEY = "a-string-secret-at-least-256-bits-long"

WRONG_SECRET_KEY = "wrong-secret-key"

ALGORITHM = "HS256"

payload = {
    "name": "Heorhii",
    "age": 15,
    "city": "Odesa",
    "exp": datetime.utcnow() + timedelta(seconds=500)
}

token = jwt.encode(payload, SECRET_KEY, algorithm=ALGORITHM)
print("JWT token created:")
print(token)

print("Trying to decode token with wrong secret key")

decoded = jwt.decode(
    token,
    WRONG_SECRET_KEY,
    algorithms=[ALGORITHM]
)

print(decoded)