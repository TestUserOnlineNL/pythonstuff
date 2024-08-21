# get max data width per element
def column_width(dl):
	el = 0
	while el < len(dl):
		cw = len(dl[el])
		if columns[el] < cw:
			columns[el]=cw
		el += 1

	return columns


# fill-up column
def column_stuffing(data, data_width):
	col_fill = "." * data_width
	cw = len(col_fill)
	dw = len(data)
	f = cw - dw
	if f >= 0:
	    return col_fill[0:f]+data
	else:
		return "Error"


# read csv file
with open("movies.csv","r",encoding="UTF8") as test_data:

	for line in test_data:
		line_list = line.split(",")
		columns = [0] * len(line_list)
		show = column_width(line_list)
		print(show)
		print(line_list[1].strip('"'),len(line_list[1].strip('"')))