N = int(input())
classes = list(map(int,input().split()))
mainOb, subOb = map(int,input().split())
res = 0
for students in classes:
    res += 1
    students -= mainOb

    if students > 0:
        res += (students + subOb - 1) // subOb

print(res)