i = int(input())
lam = 0
if(i>2):
    for c in range(2,i):
        if(i%c==0):
            lam = 1
            break
else :
    print('yes')
if(lam==0):
    print('yes')
else :
    print('no')
