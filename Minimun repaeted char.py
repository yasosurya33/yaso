n=int(input())
nam=input().split()[:n]
dub=[]
for i in nam:
    dub.append([nam.count(i),i])
dub.sort()
print(dub[0][-1])
