# imports
import json
from dicttoxml import dicttoxml
from xml.dom.minidom import parseString


# setting things ready
filename = r"movies_data.txt"
cols = ["id","title","year"]
collection = []

# read data from file
with open(filename,"r",encoding="UTF8") as data_in:
    for ln, data_line in enumerate(data_in, 1):
        filtered_line = [ln] + data_line.rstrip(')\n').split(' (')
        if(len(filtered_line) == 3):
            collection.append(filtered_line)
        else:
            filtered_line.append("---ERROR---")
            collection.append(filtered_line)

# convert list to dictionary
stapel = {}
for r,row in enumerate(collection, 1):
    coll = {};
    for v,element in enumerate(row):
        coll[cols[v]] = row[v]

    movie = "movie" + str(r)
    stapel[movie] = coll


# export to csv file
with open("movies.csv","w",encoding="UTF8") as csv_movies_file:
    for value in stapel.values():
        csv_movies_file.writelines(f'{value["id"]},"{value["title"]}",{value["year"]}\n')


# export to tab delimited file
with open("movies.tab","w",encoding="UTF8") as tab_movies_file:
    for value in stapel.values():
        tab_movies_file.writelines(f'{value["id"]}\t"{value["title"]}"\t{value["year"]}\n')


# export to sdf
#


# export to json file
with open("movies.json","w",encoding="UTF8") as json_movies_file:
    json.dump(stapel, json_movies_file, indent = 4 )


# export to xml file
with open("movies.xml","w",encoding="UTF8") as xml_movies_file:
    xml = dicttoxml(stapel, custom_root='movies',ids = False, attr_type = False, return_bytes=False)
    dom = parseString(xml)
    xml_movies_file.writelines(dom.toprettyxml())


#export to database
#