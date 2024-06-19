import sys
N = int(sys.stdin.readline().rstrip())

arr = []
for i in range(N):
    arr.append(list(sys.stdin.readline().rstrip().split()))
    arr[i][1] = int(arr[i][1])
    arr[i][2] = int(arr[i][2])
    arr[i][3] = int(arr[i][3])

arr.sort(key = lambda x : x[0])
arr.sort(key = lambda x : x[3], reverse = True)
arr.sort(key = lambda x : x[2])
arr.sort(key = lambda x : x[1],  reverse = True)

for i in arr:
    print(i[0])

