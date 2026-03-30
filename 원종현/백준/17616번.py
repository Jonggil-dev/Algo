import sys
input=sys.stdin.readline

t=int(input())
for _ in range(t):
    N=int(input())
    res=1
    li=[input().rstrip() for _ in range(N)]
    li.sort()
    for i in range(N-1):
        if len(li[i])<=len(li[i+1]):
            if li[i]==li[i+1][:len(li[i])]:
                res=0
                break
    print("YES"if res else "NO")