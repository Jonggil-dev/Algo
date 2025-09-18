N=int(input())
d={'Z':0,'G':8,'X':6,'W':2,'U':4,'F':5,'H':3,'I':9,'V':7,'O':1}
for i in range(1,N+1):
    S=input()
    c={d[j]: S.count(j) for j in 'ZGXWUHFIVO'}
    c[3]-=c[8]
    c[5]-=c[4]
    c[7]-=c[5]
    c[9]-=c[5]+c[6]+c[8]
    c[1]-=c[0]+c[2]+c[4]
    print(f"Case #{i}: {''.join(str(j)*c[j] for j in sorted(c.keys()))}")
