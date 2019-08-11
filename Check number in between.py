s=int(input())
a,b=input().split()
lab=0
for i in range(int(a)+1,int(b)):
    if i==s:
        lab=1
if lab==1:
    print("yes")
else:
    print("no")

