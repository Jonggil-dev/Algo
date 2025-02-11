import sys,math
input=sys.stdin.readline
N,L=map(int,input().split())
li=[]
for i in range(N):
    a,b=map(int,input().split())
    li.append((a,b-1))
li.sort(key=lambda x:(x[0],-x[1]))
print(li)
res=0
now=0
for a,b in li:
    if b<=now:
        continue
    elif now<a:
        val=math.ceil((b-a+1)/L)
        res+=val
        now=a+val*L-1
    elif a<=now and now<b:
        val=math.ceil((b-now)/L)
        res+=val
        now=now+val*L
    print(f'a,b:{a,b}, now:{now}, res:{res}')
print(res)
