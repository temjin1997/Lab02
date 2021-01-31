import json

jsonstr = """{"people":[ { "id" : 1, "FN" : "Ben", "LN" : " Finkel", "Email" : " ben.finkel@ab.com", "Active" : true }, 
    { "id" : 2, "Name" : ["Jame","Doe"], "Email" : " jame.doe@ab.com", "Active" : false }, 
    { "id" : 3, "FN" : "Pat", "LN" : " Smith", "Email" : " pat.smith@ab.com", "Active" : true } ]}"""

#print(type(jsonstr))

jsonstr = json.loads(jsonstr)

#print(jsonstr)
#print(type(jsonstr))
#print(type(jsonstr['people']))

for i in jsonstr['people']:
    print(i)

jsonstr = json.load(open('sample.json'))

print(type(jsonstr))

for i in jsonstr['People']:
    print(i)