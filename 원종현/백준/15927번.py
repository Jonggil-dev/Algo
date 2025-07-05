import sys

def func(n):
    le=word[:len(word)//2-n+(0 if len(word)%2==0 else 1)]
    ri=word[len(word)//2:len(word)-n]
    if le!=ri[::-1]:
        return 1
    else:
        return 0


word=list(map(str,sys.stdin.readline().rstrip()))
if func(0):print(len(word))
elif func(1):print(len(word)-1)
else:print(-1)