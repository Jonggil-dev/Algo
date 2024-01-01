N = int(input())
ls = list(input().split())
now = [1,1]
for i in ls:
    if i == "L" and now[1]>1:
        now[1] -= 1
    elif i == "R" and now[1]<N:
        now[1] += 1
    elif i == "U" and now[0]>1:
        now[0] -= 1
    elif i == "D" and now[0]<N:
        now[0] += 1
print(now)