d=[-1,0,1,0]
r1,c1,r2,c2 = map(int,input().split())
li = [[0 for _ in range(c2-c1+1)] for _ in range(r2-r1+1)]
total = (c2-c1+1)*(r2-r1+1)
dir = 1
x = 0
y = 0
cnt = 1
l = 1
while total > 0:
    for _ in range(2):
        for _ in range(l):
            if r1<=x<=r2 and c1<=y<=c2:
                li[x - r1][y - c1] = cnt
                total -= 1
                m = cnt
            x += d[dir]
            y += d[3-dir]
            cnt += 1
        dir = (dir-1) % 4
    l += 1
max_len = len(str(m))
for i in range(r2-r1+1):
    for j in range(c2-c1+1):
        print(str(li[i][j]).rjust(max_len),end=" ")
    print()