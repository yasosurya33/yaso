num=int(input())
lab=0
if num >1:
    for i in range(2,num):
        if num%i ==0:
            lab=1
            break
else :
    print("yes")
if lab==0:
    print("yes")
else :
    print("no")
