num =int(input())
i=0
while num>0:
    sum=num%10
    if not sum ==0:
        if not sum ==1:
            print("not")
            break
    else:
        i=1
    num=num//10
if i ==1:
    print("yes")
