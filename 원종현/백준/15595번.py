from collections import defaultdict
import sys
input=sys.stdin.readline
N=int(input())
success=set()
total=defaultdict(int)
for _ in range(N):
    li=input().rstrip().split()
    if li[1]!='megalusion':
        if li[2]=='4':
            success.add(li[1])
        else:
            if li[1] not in success:
                total[li[1]]+=1

c=len(success)+sum([v for k,v in total.items() if k in success])
print(len(success),c)
if c==0:
    print(0)
else:
    print(f'{len(success)/c*100:.9f}')