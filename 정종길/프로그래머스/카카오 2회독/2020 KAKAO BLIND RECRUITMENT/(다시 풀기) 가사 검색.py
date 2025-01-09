class Trie:
    def __init__(self):
        self.child = dict()
        self.count = 0
    
    def insert(self, word):
        cur = self
        for w in word:
            cur.count += 1
            if w not in cur.child:
                cur.child[w] = Trie()
            cur = cur.child[w]
        cur.count += 1
        
    def search(self, word):
        cur = self
        for w in word:
            if w == "?":
                return cur.count
            if w not in cur.child:
                return 0
            
            cur = cur.child[w]
            
        return cur.count
            
            
def solution(words, queries):
    answer = []
    
    tries = [ Trie() for _ in range(10000) ]
    reverse_tries = [ Trie() for _ in range(10000) ]
    
    for word in words:
        tries[ len(word) - 1 ].insert(word)
        reverse_tries[ len(word) - 1 ].insert(word[::-1])
    
    for q in queries:
        if q[0] == "?":
            answer.append(reverse_tries[len(q) - 1].search(q[::-1]))
        else:
            answer.append(tries[len(q) - 1].search(q))
    return answer