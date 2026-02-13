from pymongo import MongoClient

client = MongoClient("mongodb://localhost:27017/")
db = client["company_db"]
collection = db["c2"]

new_employee = {
    "name": "BALA",
    "age":23,
    "salary": 75000,

}



insert_result = collection.insert_one(new_employee)
print(f"\nInserted new employee with ID: {insert_result.inserted_id}")

employee = collection.find_one({"_id": insert_result.inserted_id})
print(f"\nDetails of inserted employee: {employee}")