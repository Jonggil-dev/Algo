def solution(n, arr1, arr2):
    answer = []
    for i in range(n):
        txt = bin(arr1[i] | arr2[i])[2:]
        if len(txt) <= n:
            txt = "0" * (n-len(txt)) + txt
        txt = txt.replace("0"," ")
        txt = txt.replace("1", "#")
        answer.append(txt)
        
    return answer