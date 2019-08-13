num=int(input())
sam=(input().split())[:num]
dub=sam.copy()
sam.sort()
if dub==sam:
    print("yes")
else:
    print("no")
