
import json

# # Opening JSON file
# f = open('POC\data.json', 'r')

# returns JSON object as a dictionary
data = json.load(dict)

# Iterating through the json list
tempvar = []
for value ,key in data.items():
    # print(data.items())
    # print(key)
    # print(type(value))
    if (key.get("type") == "array") == False:
        for field in key.keys():
            tempvar.append(key)
        
    else:
        tempvar.append(key)
	
print(tempvar)

f.close()
