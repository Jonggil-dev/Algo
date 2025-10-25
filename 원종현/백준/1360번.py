import sys
input=sys.stdin.readline

N=int(input())
q=[]
now=''
for _ in range(N):
    check=0
    a,b,c=input().rstrip().split()
    c=int(c)
    if a=='type':
        now+=b
        q.append((now,c))
    else:
        b=int(b)
        for i in range(len(q)-1,-1,-1):
            if q[i][1]>=c-b:
                continue
            check=1
            now=q[i][0]
            q.append((now,c))
            break
        if not check:
            now=''
            q.append((now,c))
print(q[-1][0])