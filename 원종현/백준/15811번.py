from itertools import permutations
import sys
input=sys.stdin.readline


a,b,c=input().rstrip().split()
li=sorted([*set(a+b+c)])


d={}
for word,i in [(a,1),(b,1),(c,-1)]:
    for j,char in enumerate(reversed(word)):
        d[char]=d.get(char,0)+i*(10**j)
chars=[*d.keys()]
weights=[d[i] for i in chars]

if len(chars)>10:
    print('NO')
    exit()

for i in permutations(range(10),len(chars)):
    val=0
    for j in range(len(chars)):
        val+=i[j]*weights[j]
    if val==0:
        print('YES')
        exit()
print('NO')
