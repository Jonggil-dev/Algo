N=int(input())
crain=sorted(list(map(int,input().split())),reverse=True)
M=int(input())
box=sorted(list(map(int,input().split())),reverse=True)
if crain[0]<box[0]:
    print(-1)
else:
    r=0
    while 0<len(box):
        for i in crain:
            for j in box:
                if i>=j:
                    box.remove(j)
                    break
        r+=1
    print(r)