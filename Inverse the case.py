nam=input()
dub=[]
for i in nam:
    if i.isupper():
        dub.append(i.lower())
    else:
        dub.append(i.upper())
for i in dub:
    print(i,end="")
