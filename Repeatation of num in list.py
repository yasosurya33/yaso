bad=list(map(int,input().split()))[:2]
good=list(map(int,input().split()))[:4]
rep=[]
sum=0
a=good.count(bad[0])
b=good.count(bad[1])
if a>b:
    print(a)
else:
    print(b)

