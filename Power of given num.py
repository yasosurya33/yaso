a,b=map(int,input().split())
lab=0
for i in range(a):
    if b**i==a:
        lab=1
if lab==1:
    print("yes")
else:
    print("no")
