import sys
n=int(input())
lst=[int(sys.stdin.readline()) for i in range(n)]
res=[]
first=0

for idx,val in enumerate(lst):
    if idx%2==0:
        first+=val
    else:
        first-=val
res.append(first//2)

for i in range(n-1):
    res.append(lst[i]-res[i])

for i in res:
    print(i)
