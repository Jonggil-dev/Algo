N=int(input())
res=0
li=[int(input()) for _ in range(N)]
for i in range(N-2,-1,-1):
    if li[i]>=li[i+1]:
        res+=li[i]-li[i+1]+1
        li[i]=li[i+1]-1
print(res)