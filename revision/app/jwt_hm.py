import jwt
from datetime import datetime, timedelta

SECRET_KEY = "secret"

payload = {
    "name": "Heorhii",
    "age": 15,
    "city": "Odesa",
    "exp": datetime.utcnow() + timedelta(seconds=1000)
}

token = jwt.encode(payload, SECRET_KEY, algorithm="HS256")
print(token)

decoded = jwt.decode(token, SECRET_KEY, algorithms=["HS256"])
print(decoded)