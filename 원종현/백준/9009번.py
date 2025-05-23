import sys
input=sys.stdin.readline
li=[0,1]
for i in range(2,46):
    li.append(li[i-2]+li[i-1])

for _ in range(int(input())):
    N=int(input())
    res=[]
    for i in range(45,0,-1):
        if li[i]<=N:
            res.append(li[i])
            N-=li[i]
            if N==0:
                res.sort()
                print(*res)