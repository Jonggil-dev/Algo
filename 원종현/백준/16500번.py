import sys
input=sys.stdin.readline

S=input().rstrip()
li=list(S)
N=int(input())
dp=[0]*(len(li)+1)
dp[0]=1
words=[]

for i in range(N):
    tmp=input().rstrip()
    words.append(tmp)

for i in range(len(li)+1):
    for word in words:
        wlen=len(word)
        if i>=wlen and dp[i-wlen]==1 and li[i-wlen:i]==list(word):
            dp[i]=1

if dp[len(li)]:
    print(1)
else:
    print(0)