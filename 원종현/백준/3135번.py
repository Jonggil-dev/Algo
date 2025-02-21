a,b=map(int,input().split())
N=int(input())
li=[int(input()) for i in range(N)]
tmp=[]
for i in range(len(li)):
    tmp.append(abs(li[i]-b))
if abs(a-b)<=min(tmp):
    print(abs(a-b))
else:
    print(min(tmp)+1)