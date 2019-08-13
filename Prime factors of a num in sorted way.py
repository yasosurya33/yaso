num=int(input())
for i in range(2,num+1):
    if num%i==0:
        lab = 0
        for j in range(2, i):
            if i % j == 0:
                lab = 1
        if not lab == 1:
            print(i,end=" ")
