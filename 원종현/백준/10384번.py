import sys
input=sys.stdin.readline
N=int(input())
for i in range(N):
    S=input().rstrip().lower().replace(' ','')
    li=[0]*26
    for j in S:
        if 97<=ord(j)<=122:
            li[ord(j)-97]+=1
    print(f'Case {i+1}: ',end="")
    if min(li)==0:
        print('Not a pangram')
    elif min(li)==1:
        print('Pangram!')
    elif min(li)==2:
        print('Double pangram!!')
    elif min(li)==3:
        print('Triple pangram!!!')