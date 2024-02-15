# 2751
import sys
T = int(input())
num_ls=[]
for _ in range(T):
    num_ls.append(int(sys.stdin.readline()))
num_ls.sort()
for i in num_ls:
    print(i)
