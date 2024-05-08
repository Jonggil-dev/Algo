N=int(input())

def func(x,y):
    if len(x)==N:
        print(*x)
        return
    for i in range(1,N+1):
        if i not in y:
            func(x+[i],y.union(set([i])))
func([],set())