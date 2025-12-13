import httpx

url = "http://localhost:5000/"

# Get JWT token
response = httpx.get(url + "token")
token = response.json()["token"]
print("JWT received:", token, "\n")

# Use JWT to access secure endpoint
headers = {"Authorization": f"Bearer {token}"}
secure_response = httpx.get(url + "secure", headers=headers)

print("Secure endpoint response:")
print(secure_response.status_code)
print(secure_response.text)

