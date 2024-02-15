N = int(input())
Arr = list(map(int,input().split()))
speed = [0]*N
now = 0
for i in range(N-1,-1,-1):
    now += 1
    if Arr[i] < now:
        now = Arr[i]
    speed[i] = now
print(sum(speed))