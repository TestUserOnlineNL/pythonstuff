# setting stuff
columns = [0] * 3
csv_file = "/home/pi/GitHub/pythonstuff/bier/test.csv"

# get data width per element
def column_max_width_scan(dl):
    el = 0
    while el < len(dl):
        cw = len(dl[el])
        if columns[el] < cw:
            columns[el] = cw
        el += 1
    return

# read csv file for max data width per column
def csv_max_data_width():
    with open(csv_file, "r", encoding="UTF8") as test_data:
        for line in test_data:
            ln = line.strip("\n").split(",")
            if len(ln) == len(columns):
                column_max_width_scan(ln)

    return columns


# fill-up row data
def column_stuffing(data, data_width):
    col_fill = " " * data_width
    cw = len(col_fill)
    dw = len(data)
    f = cw - dw
    if f >= 0:
        return col_fill[0:f] + data
    else:
        return "Error"


# fixed column width
def column_fixing():
    with open(csv_file, "r", encoding="UTF8") as test_data:
        sizes = csv_max_data_width()
        for lijn in test_data:
            schoon = lijn.strip("\n").split(",")
            samen = ""
            i = 0
            while i < len(sizes):
                uit = column_stuffing(schoon[i], sizes[i])
                i += 1
                samen = samen + uit
            print(samen)


# start
column_fixing()