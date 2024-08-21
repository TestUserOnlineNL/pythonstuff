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