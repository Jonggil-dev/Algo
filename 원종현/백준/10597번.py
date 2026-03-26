def func(now,li):
    if now==len(S):
        print(*li)
        exit()

    num=int(S[now])
    if not visit[num]:
        visit[num]=1
        li.append(num)
        func(now+1,li)
        visit[num]=0
        li.pop()

    if now+1<len(S):
        num=int(S[now:now+2])
        if num<=N and not visit[num]:
            visit[num]=1
            li.append(num)
            func(now+2,li)
            visit[num]=0
            li.pop()

S=input()
N=len(S) if len(S)<10 else (len(S)-9)//2+9
print(N)

visit=[0]*(N+1)
func(0,[])