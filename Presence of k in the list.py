bad=list(map(int,input().split()))[:2]
good=list(map(int,input().split()))[:4]
b=good.count(bad[1])
if b==0:
    print("no")
else:
    print("yes")

