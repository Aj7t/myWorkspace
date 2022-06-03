
dictionary = {"a": {"b": {"type": "array", "c1": "d1", "a": {
    "b": {"type": "array", "c1": "d1", }, "b2": {"type": "array", "c2": "d2"}}}, "b2": {"type": "array", "c2": "d2"}}}

def func(dictionary):

    fieldgroups = dictionary["a"]
    # print(fieldgroups)
    # print(fieldgroups["b"]["type"])

    for fieldgroup in fieldgroups:
        # print(fieldgroup)
        # print(fieldgroups[fieldgroup])

        if "a" in fieldgroups[fieldgroup]:
            func(fieldgroups[fieldgroup])

        if fieldgroups[fieldgroup].get("type") == "array":
            fieldgrouptemp = fieldgroups[fieldgroup]
            fieldgroups[fieldgroup] = []
            fieldgroups[fieldgroup].append(fieldgrouptemp)

    print(fieldgroups)


func(dictionary)
