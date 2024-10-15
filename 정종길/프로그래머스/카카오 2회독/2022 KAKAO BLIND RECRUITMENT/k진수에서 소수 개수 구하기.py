def solution(n, k):
    answer = 0
    nums = convert(n, k).replace("0", " ").split()
    
    for num in nums:
        if check_prime(int(num)):
            answer += 1
            
    return answer

def convert(n, k):
    q, r = divmod(n, k)
    if q == 0:
        return str(r)
    return convert(q, k) + str(r)

def check_prime(num):
    if num <= 1:
        return False
    
    if num == 2:
        return True
    
    if num % 2 == 0:
        return False
    
    for i in range(3, int(num ** 0.5 + 1), 2):
        if num % int(i) == 0:
            return False
    return True