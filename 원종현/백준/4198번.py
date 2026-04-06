import sys,bisect
input=sys.stdin.readline

N=int(input())
li=[int(input()) for _ in range(N)]

res=0
for i in range(N):
    a,b=[li[i]],[-li[i]]
    for j in range(i+1,N):
        x,y=bisect.bisect_left(a,li[j]),bisect.bisect_left(b,-li[j])
        if x:
            if len(a)!=x:
                a[x]=li[j]
            else:
                a.append(li[j])
        if y:
            if len(b)!=y:
                b[y]=-li[j]
            else:
                b.append(-li[j])
    res=max(res,len(a)+len(b)-1)
print(res)