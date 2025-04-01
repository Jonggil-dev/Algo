N,K=map(int,input().split())
li=list(map(int,input().split(',')))
res=[]
for i in range(K):
    tmp=[]
    for j in range(len(li)-1):
        tmp.append(li[j+1]-li[j])
    li=tmp
print(*li,sep=',')