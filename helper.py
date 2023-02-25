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
