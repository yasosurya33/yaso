nam=input()
l=len(nam)
dup=[]
for i in nam:
    dup.append(i)
even=[]
odd=[]
for i in range(l):
    if i%2==0:
        even.append(dup[i])
    else:
        odd.append(dup[i])
for i in range(l//2):
    print(f'{odd[i]}{even[i]}',end="")
