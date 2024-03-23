import sys
input=sys.stdin.readline
N=int(input())
sumN=sum(range(1, int(N)))
numbers=input().rstrip()
sumNum=0
temp=""
for num in numbers:
    if num.isdigit():
        temp+=num
    else:
        sumNum+=int(temp)
        temp=""
sumNum += int(temp)
print(sumNum - sumN)