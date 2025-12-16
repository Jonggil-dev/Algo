N=int(input())
li=[int(input()) for _ in range(N)]
res=0
s=set(li)

for i in s:
    tmp=[]
    for j in li:
        if j!=i:
            tmp.append(j)
    v=0
    for j in range(len(tmp)):
        if j==0 or tmp[j]==tmp[j-1]:
            v+=1
        else:
            v=1
        res=max(res,v)
print(res)