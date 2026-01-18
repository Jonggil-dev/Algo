N=int(input())

die=[0]*21
die[4]=1
li=[0]*21
li[1]=1

for i in range(2,21):
    now=li[i-1]
    li[i]=li[i-1]*2-die[i]
    if i%2:
        if i+3<=20:
            die[i+3]+=now
    else:
        if i+4<=20:
            die[i+4]+=now
print(li[N])