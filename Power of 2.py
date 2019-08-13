num=int(input())
lab=0
for i in range(num):
    if 2**i==num:
        lab=1
if lab==1:
    print("yes")
else:
    print("no")
