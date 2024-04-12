N=int(input())
li=list(map(int,input().split()))
K=int(input())
r=0
while K>0 and r<N:
    m=li.index(max(li[r:r+K+1]))
    if m!=r:
        li[m],li[m-1]=li[m-1],li[m]
        K-=1
    else:
        r+=1
print(*li)