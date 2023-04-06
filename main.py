import requests

# Define the SAMPLE API endpoint to test
url = "https://api.perqara.com/api/search/lawyer"

# Set the headers
headers = {
    "Content-Type": "application/json"
}

# Define the request payload
payload = {
    "location": "Jakarta",
    "practiceArea": "",
    "language": "",
    "gender": "",
    "rating": "",
    "page": 1,
    "size": 10
}

# Make a POST request to the API endpoint
response = requests.post(url, json=payload, headers=headers)

# Verify the response status code is 200 (OK)
assert response.status_code == 200

# Extract the response body as a JSON object
response_body = response.json()

# Verify that the response contains the expected keys
assert "total" in response_body
assert "items" in response_body

# Verify that the "items" key is a list with at least one element
assert isinstance(response_body["items"], list)
assert len(response_body["items"]) > 0

# Verify that each item in the list has the expected keys
for item in response_body["items"]:
    assert "id" in item
    assert "name" in item
    assert "slug" in item
    assert "location" in item
    assert "rating" in item
    assert "practiceAreas" in item
    assert "languages" in item
    assert "price" in item
    assert "profileImage" in item
