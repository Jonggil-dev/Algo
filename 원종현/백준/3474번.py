import sys
input=sys.stdin.readline

T=int(input())
for i in range(T):
    N=int(input())
    res=0
    idx=5
    while idx<=N:
        res+=N//idx
        idx*=5
    print(res)