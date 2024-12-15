N=int(input())

def func(s):
    for i in range(len(s)):
        if s[i:]==s[i:][::-1]:
            if i==0:
                break
            s+=s[i-1::-1]
            break
    return s

for _ in range(N):
    print(func(input()))