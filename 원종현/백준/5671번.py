import sys
input=sys.stdin.readline
while True:
    li=input().rstrip()
    if not li:
        break
    res=0
    a,b=li.split()
    for i in range(int(a),int(b)+1):
        if len(set(str(i)))==len(str(i)):
            res+=1
    print(res)