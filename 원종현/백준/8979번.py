import sys
input=sys.stdin.readline

N,K=map(int,input().split())
li=[list(map(int,input().split()))for _ in range(N)]
li.sort(key=lambda x:(-x[1],-x[2],-x[3]))
print(*li,sep="\n")
cnt=0
cnt2=0
tmp=[-1,-1,-1]
a=0
while a<N:
    print(f'now:{tmp},{cnt}, {li[a]}')
    if tmp[0]!=li[a][1] or tmp[1]!=li[a][2] or tmp[2]!=li[a][3]:
        cnt+=1+cnt2
        tmp=li[a][1:]
        cnt2=0
    else:
        cnt2+=1
    if li[a][0]==K:
        print(cnt)
        break
    a+=1