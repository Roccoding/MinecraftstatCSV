# -*- coding: utf-8 -*-
"""
Display Minecraft Statistics in a less terrible way than the game does
rename file found in  .minecraft\saves\yoursave\stats 
to mc.json and run program 

@author: Mike Rocco
"""

#parse json file renamed to mc.json using built in json reader
import json
file_obj=open("mc.json", "r")
jsobj=json.load(file_obj)

#dump to a readable text document using built in dumps
with open('mcstats.txt', 'w') as f:
    print (json.dumps(jsobj["stats"], indent=3, sort_keys=True ), file=f)
    
#move set of dicts to betterview for cleaner looking code    
betterview=dict(jsobj["stats"])

#find all items with values using picked_up as most likely to have the most values
allitems=dict(betterview["minecraft:picked_up"])

#add item to allitems, value does not matter
def consolidateitems(alldict, dict2):
    for i, (k, v) in enumerate(dict2.items()):
        if k not in alldict:
            alldict[k]=0
            
#these are the things shown on the stats screen 
#in minecraft in addition to picked_up
try:
    consolidateitems(allitems, betterview["minecraft:mined"])
except:
    print("nothing here")
try:
    consolidateitems(allitems, betterview["minecraft:broken"])
except:
    print("nothing here") 
try:
    consolidateitems(allitems, betterview["minecraft:crafted"])
except:
    print("nothing here")    
try:
    consolidateitems(allitems, betterview["minecraft:used"])
except:
    print("nothing here")    
try:
    consolidateitems(allitems, betterview["minecraft:dropped"])
except:
    print("nothing here")



#print each item, in alphabetical order, 
#as well as each way it's been interacted with to file
#same order as displayed in minecraft stats
with open('mcstats.csv', 'w') as f:
    print("item,mined,broken,crafted,used,picked_up,dropped", file=f)
    for i, (k, v) in enumerate(sorted(allitems.items())):
        print(k, end=",", file=f)     

        try:
            print(betterview["minecraft:mined"][k], end=",", file=f)
        except:
            print("0", end=",", file=f)

        try:
            print(betterview["minecraft:broken"][k], end=",", file=f)
        except:
            print("0", end=",", file=f)           

        try:
            print(betterview["minecraft:crafted"][k], end=",", file=f)
        except:
            print("0", end=",", file=f)          

        try:
            print(betterview["minecraft:used"][k], end=",", file=f)
        except:
            print("0", end=",", file=f)         

        try:
            print(betterview["minecraft:picked_up"][k], end=",", file=f)
        except:
            print("0", end=",", file=f)      

        try:
            print(betterview["minecraft:dropped"][k], end=",", file=f)
        except:
            print("0", end=",", file=f)
        
        print("", file=f)

        
        
