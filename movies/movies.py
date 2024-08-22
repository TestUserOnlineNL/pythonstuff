# imports
import json
import re as rgx
from dicttoxml import dicttoxml
from xml.dom.minidom import parseString


# headers / field names
cols = ["id","title","year"]


# read data from file
filename = r"movies_data.txt"
regex = r"^(.+)\s\(([0-9]+)\)$"
ln = 0
collection = []

with open(filename,"r",encoding="UTF8") as data_in:
    for data_line in data_in:
        ln = ln + 1
        filtered_line = rgx.split(regex, data_line)
        if(len(filtered_line) == 4):
            line_out = ([ln,filtered_line[1],int(filtered_line[2])])
            collection.append(line_out)
        else:
            filtered_line.insert(0,ln)
            filtered_line[1] = filtered_line[1].strip()
            filtered_line.insert(2,0)
            collection.append(filtered_line)

# process data from memory
r = 0; stapel = {}
while r < len(collection):
    test = collection[r]
    
    v = 0; coll = {};
    while v < len(test):
        coll[cols[v]] = test[v]
        v = v + 1
 
    movie = "movie" + str(r + 1)
    stapel[movie] = coll
    r = r + 1

# export to json file
with open("movies.json","w",encoding="UTF8") as json_movies_file:
    json.dump(stapel, json_movies_file, indent = 4 )


# export to csv file
with open("movies.csv","w",encoding="UTF8") as csv_movies_file:
    for value in stapel.values():
        csv_movies_file.writelines(f'{value["id"]},"{value["title"]}",{value["year"]}\n')


# export to tab delimited file
with open("movies.tab","w",encoding="UTF8") as tab_movies_file:
    for value in stapel.values():
        tab_movies_file.writelines(f'{value["id"]}\t"{value["title"]}"\t{value["year"]}\n')


# export to xml file
def export_xml(kv):
    xml = dicttoxml(kv, custom_root='movies',ids = False, attr_type = False, return_bytes=False)
    dom = parseString(xml)
    with open("movies.xml","w",encoding="UTF8") as xml_movies_file:
        xml_movies_file.writelines(dom.toprettyxml())

export_xml(stapel)


def export_sdf():
    pass