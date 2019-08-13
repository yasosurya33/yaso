a,b=input().split()
dub=[]
dub1=[]
for i in a:
    dub.append(i)
for i in b:
    dub1.append(i)
lam=0
for i in dub:
    if i in dub1:
        lam=1
if lam==1:
    print("yes")
else:
    print("no")
