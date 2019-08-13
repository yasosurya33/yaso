n=int(input())
sam=[]
for i in range(n):
    sam.append(input())
org=["k","a","b","a","l","i"]
org.sort()
dub=[]
lab=0
for i in sam:
    for j in i:
        dub.append(j)
    dub.sort()
    if dub==org:
        lab+=1
    dub.clear()
print(lab)
