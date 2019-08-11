sam=input()
l=int(len(sam))
i=0
lab=0
while i<(l//2):
    if(sam[i]==sam[l-1-i]):
        lab=1
        i+=1
    else:
        break
if lab==1:
    print("yes")
else:
    print("no")
