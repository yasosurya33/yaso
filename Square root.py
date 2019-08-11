import math

a,b=input().split()
num=int(a)*int(b)
i=math.sqrt(num)
if num==i*i:
    print("yes")
else:
    print("no")
