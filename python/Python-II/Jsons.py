'''

Python	JSON
dict	object
list,   tuple	array
str	    string
int,    float, int- & float-derived Enums	number
True	true
False	false
None	null


'''
# Python Dictionaries to JSON strings
import json
student = {"101": {"class": 'V', "Name": 'ajit',  "Roll_no": 7},
           "102": {"class": 'V', "Name": 'aj7t',  "Roll_no": 8},
           "103": {"class": 'V', "Name": 'azit', "Roll_no": 12}
           }
print(json.dumps(student))

