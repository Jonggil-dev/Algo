def solution(h1, m1, s1, h2, m2, s2):
    answer = 0
    st=h1*3600+m1*60+s1
    end=h2*3600+m2*60+s2
    if st==0 or st==12*3600:
        answer+=1
    while st<end:
        h=st/120%360
        m=st/10%360
        s=st*6%360
        hnext=360 if not (st+1)/120%360 else (st+1)/120%360
        mnext=360 if not (st+1)/10%360 else (st+1)/10%360
        snext=360 if not (st+1)*6%360 else (st+1)*6%360
        if s<h and snext>=hnext:
            answer+=1
        if s<m and snext>=mnext:
            answer+=1
        if snext==hnext and snext==mnext:
            answer-=1
        st+=1
    return answer