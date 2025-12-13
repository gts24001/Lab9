import jwt # PY JWT
import datetime
import uuid

from datetime import datetime, timedelta

four_hours_from_now = datetime.now() + timedelta(hours=4)

SECRET_KEY = "secret"
uuid = str(uuid.uuid1())

print("uuid = ",uuid)

payload = {"jti": uuid, "user_id": 1, "exp": four_hours_from_now }
token = jwt.encode(payload, SECRET_KEY, algorithm="HS256")
print(token)

print("------------------")

decoded = jwt.decode(token, SECRET_KEY, algorithms=["HS256"])
print(decoded)