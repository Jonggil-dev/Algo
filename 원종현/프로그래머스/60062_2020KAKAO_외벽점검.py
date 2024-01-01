def solution(n, weak, dist):
    res=len(dist)+1
    dist.sort(reverse=True)
    if dist[-1]>=n:
        return 1
    def bt(we,r,idx):
        nonlocal res
        if not we:
            res=min(res,r)
            return
        if r>=res or idx==len(dist):
            return
        now_dist=dist[idx]
        check=[200,0]
        for j in we:
            we_right=[]
            repair=[]
            for k in we:
                if not ((j<=k<=j+now_dist) if j+now_dist<n else (j<=k<n or 0<=k+n<=(j+now_dist))):
                    we_right.append(k)
                else:
                    repair.append(k)
            if check[0]==200:
                bt(we_right,r+1,idx+1) #시계
            elif (repair[-1]!=check[0] and len(repair)!=check[1]):
                bt(we_right,r+1,idx+1) #시계
            check=[repair[-1] if repair else 200,len(repair)]
    bt(weak,0,0)
    answer = res
    if res==len(dist)+1:
        answer=-1
    return answer