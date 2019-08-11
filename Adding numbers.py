t=int(input())
sam=list(map(int,input().split()))[:t]
sum=0
for i in sam:
    sum+=int(i)
print(sum)
