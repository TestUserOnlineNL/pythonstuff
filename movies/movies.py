import json
import re as rgx


cols = ["id","title","year"]


# read data from file

filename = r"movies_data.txt"
regex = r"^(.+)\s\(([0-9]+)\)$"
no = 0
collection = []
with open(filename,"r",encoding="UTF8") as data_in:
    for data_line in data_in:
        filtered_line = rgx.split(regex, data_line)
        if(len(filtered_line) == 4):
            no = no + 1
            line_out = ([no,filtered_line[1],int(filtered_line[2])])
        collection.append(line_out)


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

with open("movies.json","w",encoding="UTF8") as movies_file:
    json.dump(stapel, movies_file, indent = 4 )
