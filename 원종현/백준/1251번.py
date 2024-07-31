S=input()
words=[]

for i in range(1,len(S)-1):
    for j in range(i+1,len(S)):
        front=S[:i]
        mid=S[i:j]
        back=S[j:]
        words.append(front[::-1]+mid[::-1]+back[::-1])
words.sort()
print(words[0])