N=int(input())
li=list(map(int,input().split()))
s=set()
s.add(li[0]+li[0])

res=0
for i in range(1,N):
    for j in range(i):
        if li[i]-li[j] in s:
            res+=1
            break
    for j in range(i+1):
        s.add(li[i]+li[j])
print(res)