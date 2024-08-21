hl = ["id","title","year","movie"]
hl2 = ["id","title","year","movie_picture"]
hl3 = ["id","movie_title","year","picture"]
columns = [0] * len(hl)


def column_width(dl=[]):
	el = 0
	while el < len(dl):
		cw = len(dl[el])
		if columns[el] < cw:
			columns[el]=cw
		el += 1

	return columns

print(column_width(hl))
print(column_width(hl2))
print(column_width(hl3))


def column_stuffing(data, data_width):
	col_fill = "." * data_width
	cw = len(col_fill)
	dw = len(data)
	f = cw - dw
	if f >= 0:
	    return (col_fill[0:f]+data)
	else:
		return("Error")


result = column_stuffing("crashtest",12)
print(result)