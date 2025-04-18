from collections import deque
N=int(input())
li=list(map(int,input().split()))
li.reverse()

q=deque()
for i in range(N):
    if li[i]==1:
        q.appendleft(i+1)
    elif li[i]==2:
        q.insert(1,i+1)
    elif li[i]==3:
        q.append(i+1)
print(*q,sep="\n")