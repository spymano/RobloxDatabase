'''
from os import read


import json

file = open("/Users/spyridonmanolidis/Desktop/Coding/Python/RobloxDatabase/main.json","r")

importedJson = json.loads(file.read())

print(importedJson["name"])
# # # # #
a = input("Hey there! Enter something: ")
importedJson["something"] = a

e = json.dumps(importedJson)

file = open("/Users/spyridonmanolidis/Desktop/Coding/Python/RobloxDatabase/main.json","w")

file.write(e)
'''

from os import read
import json

while True:
    option = input("Please make your selection (Read/Write): ")
    if option.lower() == "read":
        option = input("What to read (All/User): ")
        if option.lower() == "all":
            jsonFile = open("/Users/spyridonmanolidis/Desktop/Coding/Python/RobloxDatabase/main.json","r")
            importedJson = json.loads(jsonFile.read())
            print(importedJson)
        elif option.lower() == "user":
            option = input("Enter the username of the user: ")
            jsonFile = open("/Users/spyridonmanolidis/Desktop/Coding/Python/RobloxDatabase/main.json","r")
            importedJson = json.loads(jsonFile.read())
            print(importedJson[option])
        else:
            print("Error 1 | Invalid Option, please try again.")
    elif option.lower() == "write":
        option = input("Please enter the name of the user: ")
        jsonFile = open("/Users/spyridonmanolidis/Desktop/Coding/Python/RobloxDatabase/main.json","r")
        importedJson = json.loads(jsonFile.read())
        importedJson[option] = {}
        importedJson[option]['Exploiter'] = input("Is the player exploiting: ")
        importedJson[option]['Skid'] = input("Is the player a skid: ")
        importedJson[option]['Tags'] = input("Tags: ")
        exportedJson = json.dumps(importedJson)
        jsonFile = open("/Users/spyridonmanolidis/Desktop/Coding/Python/RobloxDatabase/main.json","w")
        jsonFile.write(exportedJson)
    else:
        print("Error 1 | Invalid Option, please try again.")