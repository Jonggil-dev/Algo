import sys
input=sys.stdin.readline

N,X=map(int,input().split())
li=sorted([list(map(int,input().split())) for _ in range(N)],key=lambda x:(x[0]-x[1]),reverse=True)
X-=N*1000
res=sum([i[1] for i in li])
for x,y in li:
    if X>=4000 and x>y:
        res+=x-y
        X-=4000
    else:
        break
print(res)