import requests

BASE_URL = "http://127.0.0.1:5010/api/patients"

# POST patient
response = requests.post(BASE_URL, json={
    "name": "AKASH",
    "age": 23,
    "disease": "FEVER",
    "doctor": "Dr. Smith"
})
print("POST:", response.status_code, response.json())

# GET all patients
response = requests.get(BASE_URL)
print("GET:", response.json())

# Negative test
response = requests.post(BASE_URL, json={})
print("NEGATIVE:", response.status_code)