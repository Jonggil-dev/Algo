def solution(k, room_number):
    answer = []
    post_dict, visited = {}, set()
    
    for num in room_number:
        if num not in post_dict:
            post_dict[num] = num + 1
            answer.append(num)
        else:
            tmp = []
            while num in post_dict:
                tmp.append(num)
                num = post_dict[num]
            post_dict[num] = num + 1
            for renew in tmp:
                post_dict[renew] = num + 1
            answer.append(num)
            
    return answer