import math
X,Y=map(int,input().split())
print(math.trunc(X+Y+min(X,Y)/10))