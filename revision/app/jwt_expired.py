import jwt
import time
from datetime import datetime, timedelta

SECRET_KEY = "a-string-secret-at-least-256-bits-long"
ALGORITHM = "HS256"

payload = {
    "name": "Heorhii",
    "age": 15,
    "city": "Odesa",
    "exp": datetime.utcnow() + timedelta(seconds=10)
}

token = jwt.encode(payload, SECRET_KEY, algorithm=ALGORITHM)
print("JWT token created:")
print(token)

print("\nSleeping for 15 seconds...")
time.sleep(15)

print("\nTrying to decode token...")

decoded = jwt.decode(token, SECRET_KEY, algorithms=[ALGORITHM])
print(decoded)