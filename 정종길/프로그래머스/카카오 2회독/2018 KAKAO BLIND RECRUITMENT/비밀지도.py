def solution(n, arr1, arr2):
    answer = []
    for i in range(n):
        bin_str = bin(arr1[i] |arr2[i])[2:]
        bin_str = "0" * (n - len(bin_str)) + bin_str if len(bin_str) < n else bin_str
        answer.append(bin_str.replace("0", " ").replace("1", "#"))
    
    return answer