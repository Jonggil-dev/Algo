from collections import defaultdict

def solution(fees, records):
    answer = []
    infos = defaultdict(list)
    
    for record in records:
        time, car, _ = record.split()
        infos[car].append(to_min(time))
    
    
    for key in sorted(infos.keys()):
        infos[key].sort()
        tot = cal_parking(infos[key])
        answer.append(cal_fee(tot, fees))
        
    return answer

def to_min(time):
    return int(time[:2]) * 60 + int(time[3:])

def cal_fee(tot, fees):
    fee = fees[1]
    
    if tot <= fees[0]: return fee
    
    q, r = divmod(tot - fees[0], fees[2])
    fee += (q * fees[3]) if r == 0 else ((q + 1) * fees[3])
    return fee
    
def cal_parking(info):
    t = 0
    if len(info) % 2 == 1:
        info.append(23*60 + 59)
        
    for i in range(0, len(info), 2):
        t += info[i + 1] - info[i]
    
    return t
        