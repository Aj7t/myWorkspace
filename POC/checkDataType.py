

import json
data = {
    "name": "ajit",
    "Role": "developer",
    "company": "1silverbullet  ",
}

data2 ={
    "firstName": "Jane",
    "lastName": "Doe",
    "hobbies": ["running", "sky diving", "singing"],
    "age": 35,
    "children": [
        {
            "firstName": "Alice",
            "age": 6
        },
        {
            "firstName": "Bob",
            "age": 8
        }
    ]
}

data3 = {
    "customers": [
        {
            "customer1": {
                "id": "1",
                "customerName": "Customer Alpha",
                "customerID": " custA",
                "customerAddress": " Alpha Way",
                "customerCity": " Alpha",
                "customerState": " AL",
                "customerZip": "91605"
            }
        },
        {
            "customer2": {
                "id": "2",
                "customerName": "Customer Beta",
                "customerID": " CustB",
                "customerAddress": " Beta Street",
                "customerCity": " Beta",
                "customerState": " BE",
                "customerZip": "91605"
            }
        }
    ]
}



def checkDataType(field):
    if type(field) == dict:
        return (checkDataType(next(field)))
    

tempvar = []
for field in data3['customers']:
    checkDataType(field)
    if ['id'] == '1':
     tempvar.append(field)

print(tempvar)


# print(type(data))
# print(type(data2))
print(type(data3))





