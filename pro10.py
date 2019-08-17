num1 = int(input())
num = [int(o) for o in input().split(" ")]
num2 = 0
for i in range(num1):
    for j in range(i):
        if (num[j] < num[i]):
            num2 += num[j]
print(num2)
