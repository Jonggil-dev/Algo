N=int(input())
li=[float(input()) for _ in range(N)]
for i in range(1,N):
    li[i]=max(li[i],li[i]*li[i-1])
print('%0.3f'%max(li))