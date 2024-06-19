import sys
N = int(sys.stdin.readline().rstrip())

arr = list(map(int, sys.stdin.readline().rstrip().split()))

arr.sort()

print(arr[(N - 1) // 2])