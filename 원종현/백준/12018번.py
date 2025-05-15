N,M=map(int,input().split())
res=0
li=[]
for i in range(N):
    p,l=map(int,input().split())
    po=list(map(int,input().split()))
    po.sort(reverse=True)
    if p<l:
        li.append(1)
    else:
        li.append(po[l-1])
li.sort()
for i in li:
    if M-i>=0:
        res+=1
        M-=i
print(res)