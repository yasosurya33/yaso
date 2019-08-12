num=int(input())
sam=input()
vow=["a","e","i","o","u"]
dup=[]
for i in sam:
    if not i in vow:
        dup.append(i)
dup.reverse()
for i in dup:
    print(i,end="")
