num=int(input())
lab=0
for i in range(2,num):
    if num%i==0:
        lab=1
if lab==1:
    print("yes")
else:
    print("no")
