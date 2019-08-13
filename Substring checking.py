a,b=input().split()
dub1=[]
dub=[]
for i in a:
    dub.append(i)
for i in b:
    dub1.append(i)
lab=0
for i in dub1:
    if not i in dub:
        lab=1
if not lab==1:
    print("yes")
else:
    print("no")
