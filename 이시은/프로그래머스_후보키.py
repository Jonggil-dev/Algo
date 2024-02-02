from itertools import combinations as comb

def isExist(index_list, key):
    for k in key:
        if set(k) < set(index_list):
            return True
        
    return False

def get_multiple_element(my_list, index):
    return [my_list[i] for i in index]

def solution(relation):
    n_col = len(relation[0])
    org = list(range(n_col))

    key = []
    n = 1
    while n <= n_col:
        # print(org)
        for index_list in list(comb(org, n)):
            if isExist(index_list, key):
                continue
            else:
                # print(index_list)
                SET = set()
                for row in relation:
                    SET.add(''.join(get_multiple_element(row, index_list)))

                # print(SET)
                if len(SET) == len(relation):
                    key.append(index_list)

            # print("key:", key)
        n += 1

    return len(key)

relation = [["100","ryan","music","2"],["200","apeach","math","2"],["300","tube","computer","3"],["400","con","computer","4"],["500","muzi","music","3"],["600","apeach","music","2"]]

print(solution(relation))