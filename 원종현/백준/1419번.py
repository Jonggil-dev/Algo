L=int(input())
R=int(input())
K=int(input())
if K==2:
    print(max(0,R-max(L,3)+1))
elif K==3:
    print(max(0,R//3-(max(L,6)-1)//3))
elif K==4:
    print(max(0,R//2-(max(L,14)-1)//2)+(L<=10<=R))
else:
    print(max(0,R//5-(max(L,15)-1)//5))
