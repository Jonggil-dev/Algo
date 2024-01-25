N=int(input())
r=[0]*10
r[0]=-1
gap=10-N%10-1

def func(x,c):
    if x==0:return
    global r
    gap=10-x%10-1
    for i in range(10):
        r[i]+=((x+gap+1)//10)*(10**c)
    for i in range(9,9-gap,-1):
        r[i]-=1*10**c
    for i in str(x)[:-1]:
        r[int(i)]-=gap*10**c
    if c!=0:
        r[0]-=10**c
    #print(x,c,gap,r)
    func(x//10,c+1)
func(N,0)
print(*r)