import sys
from collections import deque
input=sys.stdin.readline
N,M,K=map(int,input().split())
card=sorted(list(map(int,input().split())))
nodes={card[i]:card[i+1] for i in range(M-1)}
check_card= {i:1 for i in card}
def func(num):
    st,end=0,M
    while st<end:
        mid=(st+end)//2
        if card[mid]>num:
            end=mid
        else:
            st=mid+1
    return end
def check(num):
    if check_card[num]:
        check_card[num]=0
        return num
    return check(nodes[num])
for i in list(map(int,input().split())):
    r=func(i)
    print(check(card[r]))
