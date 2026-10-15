


trasectionlist = ["james,10,sf", "bonine,50,ny","james,60,ny"] 

parts =[]

for trs in trasectionlist: 
    parts.append(trs.split(","))

for i in parts:
    print (i[0])

 