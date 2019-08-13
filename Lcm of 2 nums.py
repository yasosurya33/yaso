def lcm(x,y):
    if x>y:
        g=x
    else:
        g=y
    while True:
        if g%x==0 and g%y==0:
            ans=g
            break
        g+=1
    return g


a,b=map(int,input().split())
print(lcm(a,b))
