while True:
    try:
        N=int(input())
        res='1'
        while True:
            if int(res)%N==0:
                print(len(res))
                break
            res+='1'
    except:
        break