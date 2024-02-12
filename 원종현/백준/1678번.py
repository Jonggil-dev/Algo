T,M,N=map(int,input().split())
now=0
train=[]
times=[]
for i in range(T):
    train_name,*time=input().split()
    for i in time[:-1]:
        times.append((int(i),train_name))
times.sort(key=lambda x:x[0])
for i in times:
    if i[0]<M:
        continue
    else:
        if N>0:
            N-=1
        else:
            now=i[1]
N%=len(times)
if now:
    print(now)
else:
    print(N,len(times),times[N-1][1])