import requests

url = "https://jsonplaceholder.typicode.com/users/1"

response = requests.get(url)

print("Status Code:", response.status_code)

if response.status_code == 200:
    data = response.json()

    print("ID:", data["id"])
    print("Name:", data["name"])
    print("Username:", data["username"])
else:
    print("Request failed")