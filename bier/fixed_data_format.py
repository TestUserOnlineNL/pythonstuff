biermerken = [["amstel pilsener",12,6],["heineken premium pilsener",5,1],["bavaria",4,2],["klok",0,6],["lander bräu premium",6,0],["grolsch premium pilsner",6,0]]

def columns_width(bieren):
    columns = [0] * 3

    for row in bieren:
        for i, item in enumerate(row):
            columns[i] = max(columns[i],len(str(item)))
        
    return columns


def columns_data(bieren,max_width):
    data_store = []
    for row in bieren:
        regel = ""
        for i, item in enumerate(row):
            text = str(item).ljust(max_width[i])
            regel = regel + text
        data_store.append(regel)
    return data_store

def show_fixed_data():
    sizes = columns_width(biermerken)
    fixed_data = columns_data(biermerken,sizes)

    for textline in fixed_data:
        print(textline)

show_fixed_data()