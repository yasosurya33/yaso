a,b=map(int,input().split())
sam=list(map(int,input().split()))[:a]
sam1=list(map(int,input().split()))[:b]
sam1.sort()
sam1.reverse()
sam.sort()
sam.reverse()
for i in sam:
    sam1.append(i)
sam1.sort()
sam1.reverse()
print(sam1[:b])
