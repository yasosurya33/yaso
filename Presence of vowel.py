s=input()
vow=["a","e","i","o","u"]
lab=0
for i in s:
    for j in vow:
        if(i==j):
            lab=1
if lab==1:
    print("yes")
else:
    print("no")
