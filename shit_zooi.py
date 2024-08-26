bier = [["amstel pilsener",6,0],["heineken premium pilsener",5,1],["bavaria",4,2],["klok",0,6],["lander bräu premium",6,0],["grolsch premium pilsner",6,0]]

def columns_data(bieren):
    columns = [0] * 3

    for row in bieren:
        for i, item in enumerate(row):
            columns[i] = max(columns[i],len(str(item)))
        
    return columns


print(columns_data(bier))