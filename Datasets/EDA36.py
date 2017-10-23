import json


with open('EDA36-Percentage_of_persons.json') as json_data:
    DATA = json.load(json_data)
    VALUE = DATA["dataset"]["value"]

    LABEL = DATA["dataset"]["dimension"]["Sex"]
    print(LABEL)
