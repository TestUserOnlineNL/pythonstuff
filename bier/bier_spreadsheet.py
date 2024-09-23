# bier_spreadsheet.py
dict_sheet_row = {}
with open('./bier.csv') as csv_file:
	for ln,line in enumerate(csv_file,1):
		
		mylist=(line.strip("\n").split(","))
		# print(len(mylist))
		dict_sheet_row.update({f'row {ln}':mylist})


print(dict_sheet_row)