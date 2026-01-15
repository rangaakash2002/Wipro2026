import json
data={
    "name":"Akash",
    "age":20,
    "height":80,
    "weight":70,
    "id":["java","py"]
}
with open("data.json","w") as f:
    json.dump(data,f)