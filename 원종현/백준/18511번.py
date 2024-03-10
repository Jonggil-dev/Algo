N,K=map(int,input().split())
li=list(map(int,input().split()))
r=0
def func(now):
    global r
    if len(now) and int(now)>N:
        return
    if len(now):
        r=max(int(now),r)
    for i in li:
        func(str(int(now+str(i))))
func('')
print(r)