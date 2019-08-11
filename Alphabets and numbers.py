s=input()
lab=0
for i in s:
    if i.isnumeric():
        lab=1
if lab==1:
    print("Yes")
else:
    print("No")
