num1=int(input())
num2=list(map(int, input().split()))
sam= [1] * num1
for i in range(num1):
    if i==0:
        if num2[i]>num2[i + 1]:
            sam[i]= sam[i] + sam[i + 1]
    elif i>0:
        if num2[i]>num2[i - 1]:
            sam[i]= sam[i] + sam[i - 1]
print(sum(sam))
