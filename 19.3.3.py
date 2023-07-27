import kwargs as kwargs
import requests

status = 'available'

# res = requests.get(f"https://petstore.swagger.io/v2/pet/findPetsByStatus={status}", headers={'accept':
# 'application/json'})


res = requests.get(f"https://petstore.swagger.io/v2/pet/findByStatus", params={'status': 'available'},
                   headers={'accept': 'application/json'})

if 'application/json' in res.headers['Content-Type']:
    res.json()
else:
    res.text
print(res.status_code)
print(res.text)
print(res.json())
print(type(res.json()))

res = requests.post(f"https://petstore.swagger.io/v2/pet", headers={'accept': 'application/json'},
                    json={
                        "id": 1223333,
                        "category": {
                            "id": 0,
                            "name": "dadatongs"
                        },
                        "name": "doggie",
                        "photoUrls": [
                            "string"
                        ],
                        "tags": [
                            {
                                "id": 0,
                                "name": "gogo"
                            }
                        ],
                        "status": "available"
                    })
print(res.status_code)
print(res.text)
print(res.json())
print(type(res.json()))

res = requests.delete(f"https://petstore.swagger.io/v2/pet/petId")

print(res.status_code)

res = requests.put(f"https://petstore.swagger.io/v2/pet", data={
    "id": 50002,
    "category": {
        "id": 0,
        "name": "string"
    },
    "name": "doggie",
    "photoUrls": [
        "string"
    ],
    "tags": [
        {
            "id": 0,
            "name": "joba"
        }
    ],
    "status": "available"
})
print(res.status_code)
