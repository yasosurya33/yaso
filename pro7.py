num=int(input())
num1=[]
num2=0
for i in range (0, num + 1):
    num2=abs((2 ** i) - num)
    num1.append(num2)
sum=min(num1)
print(sum)
