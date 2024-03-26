N,S,P=map(int,input().split())
if N==0:
    print(1)
else:
    li=list(map(int,input().split()))
    if N==P and li[-1]>=S:
        print(-1)
    else:

        r=N+1
        for i in range(N):
            if li[i]<=S:
                r=i+1
                break
        print(r)