M, N = map(int,input().split())
Arr = [0] * (N+1)
Arr[1] = 1

for i in range(2,N+1):
    if not Arr[i]:
        for j in range(2,N+1):
            if i * j > N:
                break
            Arr[i*j] = 1
    else:
        continue

for k in range(M,N+1):
    if not Arr[k]:
        print(k)
