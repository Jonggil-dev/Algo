N=int(input())
li=[]
res=0

a=list(map(int,input().split()))
b=list(map(int,input().split()))
for i in range(N):
    li.append([a[i],b[i]])
li.sort(key=lambda x:[x[1]])

for i in range(N):
    res+=li[i][0]+(i*li[i][1])
print(res)