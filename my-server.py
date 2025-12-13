import uuid
import jwt
import datetime
from flask import Flask, request

app = Flask(__name__)

SECRET_KEY = "secret"

my_uuid = "45e02918-cfa9-11f0-aba5-7ced8ddab084"

@app.route("/")
def hello():
   return " you called \n"

# curl -d "text=Hello!&param2=value2" -X POST http://localhost:5000/echo
@app.route("/echo", methods=['POST'])
def echo():
   return "You said: " + request.form['text']

# curl -d "my_uuid=xxxx" -X POST http://localhost:5000/my_uuid
@app.route("/my_uuid", methods=['POST'])
def idCheck():
   myUuid = str(request.form['my_uuid'] )
   if (myUuid == my_uuid): 
      print("Yes!")
   else: 
      print("Failed identifier")
   return "done:  " + my_uuid + " \n "

@app.route("/token")
def get_token():
    payload = {
        "jti": str(uuid.uuid4()),
        "user_id": 1,
        "exp": datetime.datetime.estnow() + datetime.timedelta(minutes=5)
    }
    token = jwt.encode(payload, SECRET_KEY, algorithm="HS256")
    return token

@app.route("/secure")
def secure():
    auth = request.headers.get("Authorization")
    token = auth.split(" ")[1]
    decoded = jwt.decode(token, SECRET_KEY, algorithms=["HS256"])
    return "Access granted"



if __name__ == "__main__":
   app.run(host='0.0.0.0')