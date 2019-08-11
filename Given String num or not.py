t=input()
lab=0
for i in t:
    if i.isalpha():
        print("no")
        break
    else:
        lab=1
if lab==1:
    print("yes")
