import json


labels = ["id","naam","aantal","verbruik"]
items = [[1,"amstel pilsener",6,0],[2,"heineken premium plisener",5,1],[3,"bavaria",4,2],[4,"klok",0,6],[5,"lander bräu premium",6,0],[6,"grolsch premium pilsner",6,0]]


r = 0; stapel = {}
while r < len(items):
    test = items[r]
    
    v = 0; coll = {};
    while v < len(test):
        coll[labels[v]] = test[v]
        v = v + 1
 
    bier = "bier" + str(r + 1)
    stapel[bier] = coll
    r = r + 1


with open("bier.json","w",encoding="UTF8") as bier_file:
    json.dump(stapel, bier_file, indent = 4 )

###
bier_data = items[0]
print([fv for fv in zip(labels,bier_data)])
