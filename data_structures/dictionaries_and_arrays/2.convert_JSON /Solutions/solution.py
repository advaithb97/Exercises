import json
def convert(dict):
    data=json.dumps(dict)
    return data
my_dict = {"students":[{"firstName": "A", "lastName": "B"},
               {"firstName": "C", "lastName": "D"},
               {"firstName": "E ", "lastName": "F"}],
"teachers":[{"firstName": "T1", "lastName": "T2"},
         {"firstName": "T3", "lastName": "T4"}]}
         
result = convert(my_dict)
print(result)

