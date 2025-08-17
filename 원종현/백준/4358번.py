import sys
input=sys.stdin.readline
d={}
cnt=0
while True:
    s=input().rstrip()
    if s=='':
        break
    cnt+=1
    if s in d:
        d[s]+=1
    else:
        d[s]=1
d=dict(sorted(d.items()))

for i in d:
    print('%s %.4f'%(i,(d[i]/cnt*100)))
