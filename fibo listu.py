Number = 10
i = 0
fir = 0
sec = 1
listu = []
while (i < Number):
    if (i <= 1):
        Next = i
    else:
        Next = fir + sec
        fir = sec
        sec = Next
    listu.append(Next)
    i=i+1
print (listu)
