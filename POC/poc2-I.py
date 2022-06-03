dictionary = {"a":{"b":{"type":"array","c1":"d1","c2":"d2","c3":"d3"},"b2":{"c2":"d2"}}}
fieldgroups = dictionary["a"]
# print(fieldgroups)
# print(fieldgroups["b"]["type"])

for fieldgroup in fieldgroups:
    # print(fieldgroup)
    # print(fieldgroups[fieldgroup])
    if (fieldgroups[fieldgroup].get("type")=="array") == True:
        print("'type :array' found")
        fieldgrouptemp = fieldgroups[fieldgroup]
        print(fieldgroups[fieldgroup])
        fieldgroups[fieldgroup] = []
        fieldgroups[fieldgroup].append(fieldgrouptemp)

print(fieldgroups)