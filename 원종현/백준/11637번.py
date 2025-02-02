for i in range(int(input())):
    N=int(input())
    li=[int(input()) for _ in range(N)]
    maxval=max(li)
    if li.count(maxval)>1:
        print("no winner")
        continue
    idx=li.index(maxval)+1
    print('majority winner',idx) if sum(li)-maxval<maxval else print('minority winner',idx)
