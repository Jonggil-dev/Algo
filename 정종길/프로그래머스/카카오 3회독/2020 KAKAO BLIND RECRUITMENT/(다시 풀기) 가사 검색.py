'''
풀이 2가지
1. 트라이 사용 -> 현재 풀이 -> 다시 풀어보기
2. 이분 탐색 사용 -> 이걸로도 다시 풀어보기
'''

from collections import defaultdict

def solution(words, queries):
    answer = []
    
    straight, reverse = defaultdict(dict), defaultdict(dict)
    
    for word in words:
        make_Trie(word, straight)
        make_Trie(word[::-1], reverse)
    
    for q in queries:
        if q[0] == "?" and q[-1] == "?":
            if "cnt" not in straight[len(q)]:
                answer.append(0)
            else:
                answer.append(straight[len(q)]["cnt"])
            
        elif q[-1] == "?":
            answer.append(find(q, straight))
        else:
            answer.append(find(q[::-1], reverse))
            
    return answer

def make_Trie(word, trie):
    trie = trie[len(word)]
    
    if "cnt" not in trie:
        trie["cnt"] = 1
    else:
        trie["cnt"] += 1
            
    for w in word:
        if w not in trie:
            trie[w] = {}
            
        trie = trie[w]
        if "cnt" not in trie:
            trie["cnt"] = 1
        else:
            trie["cnt"] += 1
        
def find(q, trie):
    trie = trie[len(q)]
    for txt in q:
        if txt == "?":
            cnt = trie["cnt"]
            break
            
        if txt not in trie:
            return 0

        trie = trie[txt]
        
    return cnt