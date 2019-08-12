a, b = list(input().split())
a1=[]
b2=[]
for i in a:
    a1.append(i)
for i in b:
    b2.append(i)
l=len(a1)
lab=0
for i in range(l):
    if not a1[i] in b2:
        lab+=1
if lab == 1:
    print("yes")
else:
    print("no")
