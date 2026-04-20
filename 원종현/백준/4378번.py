import sys
tmp = ['=-0987654321`','\\][POIUYTREWQ', "';LKJHGFDSA", '/.,MNBVCXZ']
d={}
for i in tmp:
    for j in range(1,len(i)):
        d[i[j-1]]=i[j]
d[' '] = ' '
S=sys.stdin
for i in S:
    print(''.join(d[i] for i in i.rstrip()))