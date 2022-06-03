List = [("{'state': 'BIHAR', 'city': 'DARBHANGA'}",)]
jsonvar = [{'attribute': "{'state': 'BIHAR', 'city': 'DARBHANGA'}"}]

dbResp = [("{'state': 'BIHAR', 'city': 'DARBHANGA'}",)]

# result list initialization
attributeList = []

for t in dbResp:
	for x in t:
		attributeList.append(x)

print(attributeList)
print(type(attributeList))