import json

# Opening JSON file
f = open(r"POC\responsebody.json", "r")

# returns JSON object as a dictionary
data = json.load(f)
# print(data)

def func(data):
    
    a = data["data"]
    new_data = a["fieldGroups"] 

    for field in new_data:
        print("fields are ", field)
        if new_data[field].get("type") == "array":
            fieldtemp = new_data[field]
            new_data[field] = []
            new_data[field].append(fieldtemp)

    print (new_data)

#calling the function
func(data)


# The get() method returns the value of the item with the specified key.
