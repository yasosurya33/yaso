num=int(input())
sam=list(input().split())[:num]
sam.sort()
dub=[]
for i in sam:
    dub.append([len(i),i])
dub.sort()
for i in range(num):
    print(dub[i][1],end=" ")
