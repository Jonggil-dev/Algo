while True:
    try:
        a=input()
        b=input()
        a_s=set(a)
        b_s=set(b)
        c_s=a_s&b_s
        res=[]
        for i in c_s:
            res.append(i*min(a.count(i),b.count(i)))
        res.sort()
        print(''.join(res))
    except:
        break