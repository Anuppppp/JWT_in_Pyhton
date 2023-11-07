import jwt
import datetime

SECRET_KEY = "anup_jwt"

json_data = {
    "sender": "Anup JWT",
    "message": "JWT is awesome. You should try it!",
    "date": str(datetime.datetime.now()),
    'exp': datetime.datetime.utcnow() + datetime.timedelta(seconds=86400)
}

encoded_data = jwt.encode(payload=json_data, key=SECRET_KEY, algorithm="HS256")

print(encoded_data)
