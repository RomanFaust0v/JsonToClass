import json

def stringToJSON(string):
    json_dict =  json.loads(string)
    class_object = list()
    for key, value in json_dict.items():
        if "_" in key:
            class_object.append("\t\nProperty "+"\"" + key +"\"" +" As %String(MAXLEN = \"\");")
        else:
            class_object.append( "\t\nProperty "+ key + " As %String(MAXLEN = \"\");\n")
    return class_object
