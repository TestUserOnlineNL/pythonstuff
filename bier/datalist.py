dl = ["id","title","year","picture"]
columns = [0] * len(dl)

def column_width(dl=[]):
	el = 0
	while el < len(dl):
		cw = len(dl[el])
		columns[el]=cw
		el += 1

	return columns

print(column_width(dl))