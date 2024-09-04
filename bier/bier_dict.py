# Python program to demonstrate
# Conversion of JSON data to
# dictionary

# importing the module
import json

# Opening JSON file
with open(./'bier.json') as json_file:
    data = json.load(json_file)


    # Print the data of dictionary
    for i,j in data.items():
        print(i)
        for k,l in j.items():
            print(k,"->",l)