def solution(numbers):
    answer = []
    
    for num in numbers:
        bin_str = pharse_bin(num)
        root = bin_str[len(bin_str) // 2]
        
        if root == "0":
            answer.append(0)
        else:
            answer.append(is_valid(bin_str))
            
    return answer

def is_valid(bin_str):

    if len(bin_str) == 1:
        return 1

    mid = len(bin_str) // 2
    left_sub = bin_str[:mid]
    right_sub = bin_str[mid + 1:]
    
    if bin_str[mid] == "0":
        if left_sub[len(left_sub) // 2] == "1" or right_sub[len(right_sub) // 2] == "1":
            return 0
        
    if not is_valid(left_sub) or not is_valid(right_sub):
        return 0
    
    return 1

def pharse_bin(num):
    check = 2
    lev = 1
    bin_str = bin(num)[2:]

    while len(bin_str) > (check ** lev - 1):
        lev += 1
    
    bin_str = "0" * (check ** lev - 1 - len(bin_str)) + bin_str
    return bin_str