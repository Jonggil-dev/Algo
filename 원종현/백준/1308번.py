from datetime import *

t=list(map(int,input().split()))
d=list(map(int,input().split()))
if t[0]+1000<d[0] or (t[0]+1000==d[0] and (t[1],t[2])<=(d[1],d[2])):
    print('gg')
else:
    t=date(*t)
    d=date(*d)
    print("D-"+str(d.toordinal()-t.toordinal()))