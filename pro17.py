from itertools import permutations
num, num1 = map(int, input().split())
sam = list(map(int, input().split()))
for i in permutations(sam, 2):
    if sum(i) == num1:
        print('yes')
        break
else:
    print('no')
