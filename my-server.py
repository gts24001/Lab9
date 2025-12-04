import uuid
from flask import Flask, request

app = Flask(__name__)

uuid = "45e02918-cfa9-11f0-aba5-7ced8ddab084"

@app.route("/")
def hello():
   return " you called \n"

# curl -d "text=Hello!&param2=value2" -X POST http://localhost:5000/echo
@app.route("/echo", methods=['POST'])
def echo():
   return "You said: " + request.form['text']

# curl -d "uuid=xxxx" -X POST http://localhost:5000/uuid
@app.route("/uuid", methods=['POST'])
def idCheck():
   myUuid = str(request.form['uuid'] )
   if (myUuid == uuid): 
      print("Yes!")
   else: 
      print("Failed identifier")
   return "done:  " + uuid + " \n "

if __name__ == "__main__":
   app.run(host='0.0.0.0')