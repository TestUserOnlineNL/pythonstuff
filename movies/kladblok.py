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


# convert list to dictionary in memory
stapel = {}
for r,row in enumerate(collection, 1):
    coll = {};
    for v,element in enumerate(row):
        coll[cols[v]] = row[v]

    movie = "movie" + str(r)
    stapel[movie] = coll


# export to fixed width format
def columns_width(bieren):
    columns = [0] * 3

    for row in bieren:
        for i, item in enumerate(row):
            columns[i] = max(columns[i],len(str(item)))
    return columns


def columns_fixing(bieren,max_width):
    store = []
    for row in bieren:
        regel = ""
        for i, item in enumerate(row):
            text = str(item).ljust(max_width[i])
            regel = regel + text
        store.append(regel)
    return store


def show_fixed_data():
    sizes = columns_width(collection)
    fixed_data = columns_fixing(collection,sizes)

    for textline in fixed_data:
        print(textline)

show_fixed_data()