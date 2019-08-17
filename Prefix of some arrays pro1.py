num=int(input())
sam=[]
for i in range(num):
    sam.append(input())
dub=[]
for i in zip(*sam):
    if i.count(i[0])==len(i):
        dub.append(i[0])
    else:
        break
print(''.join(dub))
