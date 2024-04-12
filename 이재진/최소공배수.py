def solution(arr):
    answer = 1
    res = {}
    def prime_dic(n):
        dic = {}
        num = 2
        while num <= n:
            if n % num == 0:
                if num in dic:
                    dic[num] += 1
                else:
                    dic[num] = 1
                n //= num
            else:
                 num += 1
        return dic
    for i in arr:
        tmp = prime_dic(i)
        for j in tmp:
            if j in res:
                if res[j] < tmp[j]:
                    res[j] = tmp[j]
            else:
                res[j] = tmp[j]
    for i in res:
        answer *= i**res[i]
    return answer
