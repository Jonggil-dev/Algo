import math
def solution(arrayA, arrayB):
    answer = 0
    gcd_a = arrayA[0]
    gcd_b = arrayB[0]
    for i in range(len(arrayA)):
        gcd_a = math.gcd(gcd_a, arrayA[i])
        gcd_b = math.gcd(gcd_b, arrayB[i])
    if gcd_a != 1:
        f = 1
        for b in arrayB:
            if b % gcd_a == 0:
                f = 0
                break
        if f and answer < gcd_a:
            answer = gcd_a
            
    
    if gcd_b != 1:
        f = 1
        for a in arrayA:
            if a % gcd_b == 0:
                f = 0
                break
        if f and answer < gcd_b:
            answer = gcd_b
    return answer
