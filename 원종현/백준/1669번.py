import math
X,Y=map(int,input().split())
diff=Y-X
if diff==0:
    print(0)
else:
    diff_s=int(math.sqrt(diff))
    res=2*diff_s-1
    if diff_s**2==diff:
        print(res)
    else:
        mod=diff-diff_s**2
        print(res+mod//diff_s if mod%diff_s==0 else res+mod//diff_s+1)