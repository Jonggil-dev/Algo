def solution(numbers):
    answer = []
    
    for num in numbers:
        bin_num = make_FBT(num)
        
        if check_valid(bin_num, True):
            answer.append(1)
        else:
            answer.append(0)
        
    return answer

def check_valid(bin_num, flag):
    n = len(bin_num)
    
    if not flag and bin_num[n // 2] == '1':
        return False
    
    if n == 1:
        return True
    
    if bin_num[n // 2] == '0':
        flag = False

    if not check_valid(bin_num[ : n // 2 ], flag):
        return False
    
    if not check_valid(bin_num[n // 2 + 1 : ], flag):
        return False
    
    return True
    
def make_FBT(num):
    tmp = bin(num)[2:]
    n = len(tmp)
    
    i = 1
    check = 1
    while check < n:
        i += 1
        check = 2 ** i - 1
        
    return "0" * (check - n) + tmp