num1, num2 = [int(i) for i in input().split()]
sum = []
dub = [int(i) for i in input().split()]
for _ in range(num2):
    l, k = [int(i) for i in input().split()]
    sum.append(min(dub[l - 1:k]))
for i in sum:
    print(i)
