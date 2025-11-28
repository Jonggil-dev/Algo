import sys,math
input=sys.stdin.readline

def func(x):
    if visit[x]:
        return 0
    visit[x]=1

    for i in tmp[x]:
        if check[i]==-1 or func(check[i]):
            check[i]=x
            return 1
    return 0


N=int(input())
li=list(map(int,input().split()))
A,B=[],[]
for i in li:
    if i%2==0:
        A.append(i)
    else:
        B.append(i)

tmp=[[] for _ in range(len(A))]
for i in range(len(A)):
    for j in range(len(B)):
        s=A[i]**2+B[j]**2
        r=int(math.isqrt(A[i]**2+B[j]**2))
        if math.gcd(A[i],B[j])==1 and r*r==s:
            tmp[i].append(j)

check=[-1]*(len(B))
for i in range(len(A)):
    visit=[0]*(len(A))
    func(i)
print(sum([1 for i in check if i!=-1]))