num = int(input())
i = 1
fir = 0
sec = 1
listu = []
while (i <= num):
    if (i <= 1):
        Next = i
    else:
        Next = fir + sec
        fir = sec
        sec = Next
    print(Next,end=" ")
    i+=1
