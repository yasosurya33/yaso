a,b=input().split()
dub=[]
dub1=[]
for i in a:
    for j in a:
        if i==j:
            dub.append(1)
        else:
            dub.append(2)
    break
for i in b:
    for j in b:
        if i==j:
            dub1.append(1)
        else:
            dub1.append(2)
    break
if dub==dub1:
    print("yes")
else:
    print("no")
