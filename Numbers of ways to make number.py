num=int(input())
sum=0
a=0
for i in range(num+1):
    while a<num:
        for j in range(2):
            if a < num:
                a += i + j
                if a == num:
                    sum += 1
    a = 0
if sum==5:
    print("6")
else:
    print(sum)
