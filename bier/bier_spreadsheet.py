# bier_spreadsheet.py
sheet = []
with open('./bier.csv') as csv_file:
	for ln,line in enumerate(csv_file,1):
		mylist=(line.strip("\n").split(","))
		sheet.append(mylist)


print(sheet)