import yaml
from yaml import load, load_all

stream = open('sample.yaml','r')
doc = load_all(stream, Loader=yaml.FullLoader)

print(type(doc))

for d in doc:
    print (type(d))

    print (d['people'][0])