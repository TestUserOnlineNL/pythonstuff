# kladblok.py

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