# kladblok.py

import json
from dicttoxml import dicttoxml
from xml.dom.minidom import parseString

# setting things ready
data_file = r"movies_data.txt"
column_names = ["id", "title", "year"]
collection = []


def import_text_data(filename, cols):
    # read data from file
    with open(filename, "r", encoding="UTF8") as data_in:
        for ln, data_line in enumerate(data_in, 1):
            filtered_line = [ln] + data_line.rstrip(')\n').split(' (')
            if (len(filtered_line) == len(cols)):
                collection.append(filtered_line)
            else:
                filtered_line.append("---ERROR---")
                collection.append(filtered_line)


# combining two lists to a dictionary
def two_lists_to_dict(list1=[], list2=[]):
    resultDict = {}
    if len(list1) == len(list2):
        for n, f in enumerate(list1):
            resultDict.update({f: list2[n]})

    return resultDict


# transform list to dictionary
def transform_list_to_dict():
    kv = dict()
    for i,rule in enumerate(collection,1):
        hk = f"movie{i}"
        kv[hk] = two_lists_to_dict(column_names,rule)

    return kv


# export to fixed width format
def columns_width(data_in):
    columns = [0] * 3

    for row in data_in:
        for i, item in enumerate(row):
            columns[i] = max(columns[i], len(str(item)))
    return columns


def columns_fixing(data_in, max_width):
    store = []
    for row in data_in:
        regel = ""
        for i, item in enumerate(row):
            text = str(item).ljust(max_width[i])
            regel = regel + text
        store.append(regel)
    return store


def export_to_fwf(data_in):
    sizes = columns_width(data_in)
    fixed_data = columns_fixing(data_in, sizes)
    with open("movies.fwf.txt", "w", encoding="UTF8") as output:
        for line in fixed_data:
            output.writelines(f'{line}\n')


# export to csv file
def export_to_csv(data_in):
    with open("movies.csv", "w", encoding="UTF8") as csv_movies_file:
        for i, row in enumerate(data_in):
            csv_movies_file.writelines(f'{str(row[0])},"{row[1]}",{row[2]}\n')


# export to tab delimited file
def export_to_tab(data_in):
    with open("movies.tab.txt", "w", encoding="UTF8") as tab_movies_file:
        for i, row in enumerate(data_in):
            tab_movies_file.writelines(f'{str(row[0])}\t"{row[1]}"\t{row[2]}\n')

# export to json file
def export_to_json(data_in):
    with open("movies.json", "w", encoding="UTF8") as json_movies_file:
        json.dump(data_in, json_movies_file, indent=4)


# export to xml file
def export_to_xml(data_in):
    with open("movies.xml", "w", encoding="UTF8") as xml_movies_file:
        xml = dicttoxml(data_in, custom_root='movies', ids=False, attr_type=False, return_bytes=False)
        dom = parseString(xml)
        xml_movies_file.writelines(dom.toprettyxml())


if __name__ == '__main__':

    import_text_data(data_file,column_names)
    export_to_fwf(collection)
    export_to_csv(collection)
    export_to_tab(collection)
    export_to_json(transform_list_to_dict())
    export_to_xml(transform_list_to_dict())