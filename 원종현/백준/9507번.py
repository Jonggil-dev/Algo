li=[0]*(68)
li[0]=1
li[1]=1
li[2]=2
li[3]=4
def func(n):
    if n<=3 or li[n]!=0:
        return li[n]
    li[n]=func(n-1)+func(n-2)+func(n-3)+func(n-4)
    return li[n]
func(67)
for i in range(int(input())):
    n=int(input())
    print(li[n])