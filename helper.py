import json

def stringToJSON(string):
    json_dict =  json.loads(string)
    class_object = ""
    for key, value in json_dict.items():
        if "_" in key:
            class_object += "\nProperty "+"\"" + key +"\"" +" As %String(MAXLEN = \"\");\n"
        else:
            class_object += "\nProperty "+ key + " As %String(MAXLEN = \"\");\n"
    return class_object

def jsonToEnsemble(json_data):
    with open('object.txt', 'w', encoding='iso-8859-8') as f:
        for key, value in json_data.items():
            key = key.title()
            if "_" in key:
               key = key.replace("_", "")
            f.write("\nProperty "+ key + " As %String(MAXLEN = \"\");\n")