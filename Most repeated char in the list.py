nam=input()
dub=[]
for i in nam:
    dub.append([nam.count(i),i])
dub.sort()
print(dub)
print(dub[-1][-1])
