import sys
input=sys.stdin.readline
N=int(input())
li=input().rstrip()
res=[]
res.append(li.rstrip('R').count('R'))
res.append(li.rstrip('B').count('B'))
res.append(li.lstrip('R').count('R'))
res.append(li.lstrip('B').count('B'))
print(min(res))