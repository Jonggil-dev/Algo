import sys
input=sys.stdin.readline

N,K,S=map(int,input().split())
li1,li2=[],[]
for i in range(N):
    a,b=map(int,input().split())
    if a<S:
        li1.append((S-a,b))
    else:
        li2.append((a-S,b))
li1.sort(key=lambda x:x[0])
li2.sort(key=lambda x:x[0])
res=0
def func(li):
    global res
    while li:
        a,b=li.pop()  # 거리, 인원
        cost=a*2
        if K<b:
            cost=b//K*a*2
            if b%K!=0:
                li.append((a,b%K))
        else:
            tmp=0
            li.append((a,b))
            while li:
                a,b=li.pop()
                if tmp+b<K:
                    tmp+=b
                else:
                    if tmp+b>K:
                        li.append((a,b-(K-tmp)))
                    break
        res+=cost

func(li1)
func(li2)
print(res)