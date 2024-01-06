import sys

input = sys.stdin.readline
n = int(input())
l = []
answer = dict()

maxNum = 0

for i,num in enumerate([*map(int,input().strip().split())]):
    maxNum = max(maxNum,num)
    l.append((i,num))
    answer[num] = 0

l.sort(key=lambda x:x[1])

for li in range(n):
    originPos,num=l[li]

    for target in range(num*2,maxNum+1,num):

        if target in answer :
            answer[num]+=1
            answer[target]-=1

for key, item in answer.items():
    print(item,end=" ")