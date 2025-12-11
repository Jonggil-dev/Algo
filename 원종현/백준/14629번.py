N=int(input())
li=[]
res=[0,10**11]
if N>=9876543210:
    print(9876543210)
    exit()
def func(v,now):
    global res
    if now and res[1]==abs(int(now)-N) and int(res[0])>int(now):
        res=[now,abs(int(now)-N)]
    elif now and res[1]>abs(int(now)-N):
        res=[now,abs(int(now)-N)]
        #print(res)
    for i in range(10):
        if v[i]:
            continue
        v[i]=1
        func(v,now+str(i))
        v[i]=0

func([0]*10,'')
print(int(res[0]))