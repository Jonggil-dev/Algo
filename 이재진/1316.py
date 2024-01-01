import copy

T = int(input())
num = copy.copy(T)
for _ in range(T):
    s = input()
    alp_ls = list()
    for alp in s:
        if (len(alp_ls) == 0) | (alp not in alp_ls):
            alp_ls.append(alp)
        elif alp == alp_ls[-1]:
            pass
        elif alp in alp_ls:
            num -= 1
            break
print(num)
