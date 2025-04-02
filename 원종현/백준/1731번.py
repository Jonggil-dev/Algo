N=int(input())
li=[int(input()) for _ in range(N)]

r=li[1]-li[0]
c=0
if li[2]-li[1]==li[1]-li[0]:
    print(li[-1]+li[1]-li[0])
else:
    print(li[0]*(li[1]//li[0])**N)