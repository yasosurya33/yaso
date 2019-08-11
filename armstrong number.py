num = int(input())
sum=0
temp = num
while(temp>0):
    a=temp%10
    sum+=a**3
    temp//=10
if(num==sum):
    print("yes")
else:
    print("no")
