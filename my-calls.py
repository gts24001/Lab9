import httpx
import uuid


#url = "https://cautious-doodle-pjpjx694jxvcr944-5000.app.github.dev/"

url = "http://localhost:5000/"


response = httpx.get(url)
print(response.status_code)
print(response)

uuid = "45e02918-cfa9-11f0-aba5-7ced8ddab084"

response = httpx.get(url)
print(response.status_code)
print(response.text)

mydata = {
    "uuid": uuid,
    "text": "Hello Prof!",
    "param2": "Making a POST request",
    "body": "my own value"
}

# A POST request to the API
response = httpx.post(url + "echo", data=mydata)
# Print the response
print(response.status_code)
print(response.text) 

response = httpx.post(url + "uuid", data=mydata)
# Print the response
print(response.status_code)
print(response.text)
