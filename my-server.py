import jwt
import datetime
import uuid
from flask import Flask, request, jsonify

app = Flask(__name__)

SECRET_KEY = "secret"

@app.route("/")
def home():
    return "Server is running\n"

@app.route("/token")
def generate_token():
    payload = {
        "jti": str(uuid.uuid4()),
        "user_id": 1,
        "exp": datetime.datetime.utcnow() + datetime.timedelta(minutes=5)
    }
    token = jwt.encode(payload, SECRET_KEY, algorithm="HS256")
    return jsonify({"token": token})

@app.route("/secure")
def secure():
    auth_header = request.headers.get("Authorization")

    if not auth_header:
        return "Missing Authorization header", 401

    try:
        token = auth_header.split(" ")[1]
        decoded = jwt.decode(token, SECRET_KEY, algorithms=["HS256"])
        return f"Access granted for user {decoded['user_id']}\n"
    except Exception as e:
        return f"Invalid token: {str(e)}", 401

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
