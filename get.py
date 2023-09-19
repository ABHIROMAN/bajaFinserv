import requests

url = "http://127.0.0.1:5000"
response = requests.get(url)

if response.status_code == 200:
    data = response.json()  # Assuming the response is in JSON format
    print(data)
else:
    print("Request failed with status code:", response.status_code)
