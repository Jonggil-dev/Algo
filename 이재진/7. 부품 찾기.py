import sys
N = int(sys.stdin.readline())
ls_n = sorted(list(map(int, sys.stdin.readline().split())))
M = int(sys.stdin.readline())
ls_m = list(map(int, sys.stdin.readline().split()))
# for m in ls_m:
#     if m in ls_n:
#         print('yes', end=" ")
#     else:
#         print('no', end=" ")
for m in ls_m:
    flag = 0
    start = 0
    end = N - 1
    while start <= end:
        mid = (start + end) // 2
        if ls_n[mid] == m:
            flag = 1
            break
        elif ls_n[mid] > m:
            end = mid-1
        elif ls_n[mid] < m:
            start = mid+1
    if flag:
        print("yes", end=" ")
    else:
        print("no", end=" ")