num=int(input())
num1=list(map(int, input().split()))
num3=0
for i in range(0, num - 2):
	for j in range(1, num - 1):
		for k in range(2, num):
			if(num1[i]<num1[j] and num1[j]<num1[k]):
				num3+=1
print(num3)
