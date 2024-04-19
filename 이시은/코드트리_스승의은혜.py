#코드트리 스승의 은혜
N, B = map(int, input().split())

lst = []

for _ in range(N):
    p, s = map(int, input().split())

    lst.append((p, s))

lst.sort(key=lambda x: (sum(x), x[0]))

cnt = 0
SUM = 0
for p, s in lst:
    if SUM + (p + s) <= B:
        SUM += (p+s)
        cnt += 1
    else:
        if SUM + (p/2 + s) <= B:
            SUM += (p/2+s)
            cnt += 1
        break

print(cnt)

