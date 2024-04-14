N=int(input())
li=[]
for i in range(N):
    a,b=map(int,input().split())
    li.append(b-a)
li.sort()

r=0
if len(li)%2==0:
    st=len(li)//2-1
    r=li[st+1]-li[st]+1
else:
    r=1
print(r)