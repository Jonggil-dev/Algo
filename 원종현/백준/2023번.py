import sys
sys.setrecursionlimit(10**6)
input=sys.stdin.readline

N=int(input())
def func(a):
    for i in range(2,int(a/2+1)):
        if a%i==0:
            return False
    return True

def dfs(num):
    if len(str(num))==N:
        print(num)
    else:
        for i in range(1,10):
            if i%2==0:
                continue
            if func(num*10+i):
                dfs(num*10+i)

dfs(2)
dfs(3)
dfs(5)
dfs(7)