import requests

url = "https://api.example.com/data"

token = "YOUR_TOKEN"

headers = {
    "Authorization": f"Bearer {token}"
}
try:
    response = requests.get(
        url,
        headers=headers,
        timeout=5
    )
    response.raise_for_status()

    data = response.json()

    print(data)

except requests.exceptions.Timeout:
    print("The request timed out.")

except requests.exceptions.HTTPError:
    print("HTTP error:", response.status_code)

except requests.exceptions.RequestException as error:
    print("Request failed:", error)