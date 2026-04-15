def gcd(a,b):
    while b:
        a,b=b,a%b
    return a

def lcm(a,b):
    return abs(a*b)//gcd(a,b)

def solution(signals):
    answer = 0

    li=[sum(i) for i in signals]
    v=li[0]
    for i in range(1,len(li)):
        v=lcm(v,li[i])
    q=[[0,0] for _ in range(len(signals))]
    for i in range(1,v+1):
        f=0
        for j in range(len(signals)):
            if signals[j][q[j][1]]==q[j][0]:
                q[j][1]=(q[j][1]+1)%3
                q[j][0]=1
            else:
                q[j][0]+=1
            if q[j][1]!=1:
                f=1
        if not f:
            return i
    return -1