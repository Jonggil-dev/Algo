import sys
input=sys.stdin.readline
S=input().rstrip()
N=int(input())
alp={}
words=[]
for i in range(N):
    word=input().rstrip()
    words.append(word)
    alp[word]={}
    for j in word:
        if j in alp[word]:
            alp[word][j]+=1
        else:
            alp[word][j]=1
dp=[10**9]*(len(S)+1)
dp[0]=0

for st in range(len(S)):
    for end in range(st,len(S)):
        tmp={}
        comp=S[st:end+1]
        for i in comp:
            if i in tmp:
                tmp[i]+=1
            else:
                tmp[i]=1
        for word in words:
            if alp[word]!=tmp:
                continue
            cnt=0
            for j in range(len(word)):
                if word[j]!=comp[j]:
                    cnt+=1
            dp[end+1]=min(dp[end+1],dp[st]+cnt)
print(dp[-1] if dp[-1] != 10**9 else -1)
print(dp)
print(alp)