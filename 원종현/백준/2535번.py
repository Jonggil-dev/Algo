N=int(input())
li=[]
cnt=0
for i in range(N):
    a,b,c=map(int,input().split())
    li.append((a,b,c))
li.sort(key=lambda x:-x[2])
print(li[0][0],li[0][1])
print(li[1][0],li[1][1])
if li[0][0]==li[1][0]:
    cnt=1
for i in range(2,N):
    if not cnt or li[1][0]!=li[i][0]:
        print(li[i][0],li[i][1])
        break
