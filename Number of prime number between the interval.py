a, b = map(int, input().split())
sam = 0
lab = 0
for i in range(a, b+1):
    for j in range(2, i):
        if i % j == 0:
            lab = 1
            break
    else:
        sam+=1
print(sam)
