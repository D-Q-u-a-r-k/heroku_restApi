import json

def read():
    data = None
    # read file
    with open('resources/data.json', 'r') as myfile:
        data=myfile.read()    
    # parse file
    obj = json.loads(data)
    return obj

def  write(obj):
    with open('resources/data.json', 'w') as outfile:
        json.dump(obj, outfile)