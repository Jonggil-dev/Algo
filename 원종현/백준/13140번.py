from itertools import permutations
N=int(input())
c=0
for s in permutations([i for i in range(10)],7):
    d,e,h,l,o,r,w=s
    if 0 in [h,w]:
        continue
    if (h+w)*10000+e*1000+l*120+o*1001+r*100+d==N:
        print('  ',h,e,l,l,o,sep="")
        print('+ ',w,o,r,l,d,sep="")
        print('-------')
        print('' if N>10**5 else ' ',N)
        c=1
        break
if not c:
    print("No Answer")