def solution(enroll, referral, seller, amount):
    money = [0] * len(enroll)
    idxs = {e : i for i, e in enumerate(enroll)} 
    
    for s, a in zip(seller, amount):
        m = a * 100
        while s != "-" and m > 0:
            idx = idxs[s]
            money[idx] += m - m//10
            m //= 10
            s = referral[idx]
    return money