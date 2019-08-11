bad=list(map(int,input().split()))[:2]
good=list(map(int,input().split()))[:4]
rep=[]
sum=0
a=good.count(0)
b=good.count(1)
if a>b:
    print(a)
else:
    print(b)

