import sys
input = sys.stdin.readline

def dfs(num,arr):
    arr[num]=-2
    for i in range(len(arr)):
        if num==arr[i]:
            dfs(i,arr)

n=int(input())
arr=list(map(int, input().split()))
k=int(input())
res=0

dfs(k, arr)
count = 0
for i in range(len(arr)):
    if arr[i]!=-2 and i not in arr:
        res+=1
print(res)