chk=[1]*(100001)
for i in range(2,int(100001**0.5)+1):
    if chk[i]:
        for j in range(i+i,100001,i):
            chk[j]=0
so=[i for i in range(2,100001) if chk[i]]

while True:
    S=input()
    if S=='0':
        break
    for i in so[::-1]:
        if str(i) in S:
            print(i)
            break