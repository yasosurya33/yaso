nam=input().split()
sam=[]
dub = ""
for i in nam:
    for j in i[0]:
        dub+=j.upper()
    for j in i[1:]:
        dub+=j
    sam.append(dub)
    dub=""
for i in sam:
    print(i,end=" ")
