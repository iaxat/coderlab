import json

def addStrawberry():
    with open('fake_fruit.json', 'r') as f:   
        data = json.load(f)                   
        dict0 = {'Name': 'Strawberry', 'Colour': 'Red'}
        data['Fruit'].append(dict0)

    with open ('fake_fruit.json', 'w') as f:
        json.dump(data, f, indent=4)        

    with open('fake_fruit.json', 'r') as f:
        print(f.read()) 

    print(data)
    # return data

addStrawberry()
