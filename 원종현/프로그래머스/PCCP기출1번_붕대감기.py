def solution(bandage, health, attacks):
    answer=0
    max_health=health
    attacks_dict=dict()
    for t,d in attacks:
        attacks_dict[t]=d

    t=0
    cnt=0
    while t<attacks[-1][0]:
        t+=1
        if t in attacks_dict:
            health-=attacks_dict[t]
            cnt=0
            if health<=0:
                health=-1
                break
        else:
            health=min(health+bandage[1],max_health)
            cnt+=1
            if cnt==bandage[0]:
                health=min(health+bandage[2],max_health)
                cnt=0
    return health
