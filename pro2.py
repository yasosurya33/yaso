from itertools import combinations
sam, nam=map(int, input().split())
l=len(str(sam))
lst=list(combinations(str(sam), l - nam))
lst=sorted(lst)
print(*lst[0],sep='')
