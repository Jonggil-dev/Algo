N=int(input())
li=list(map(int,input().split()))
cnt=0
if sum(li)%3==0:
    for i in li:
        cnt+=i//2
    if cnt>=(sum(li)/3):
        print('YES')
    else:
        print('NO')
else:
    print('NO')