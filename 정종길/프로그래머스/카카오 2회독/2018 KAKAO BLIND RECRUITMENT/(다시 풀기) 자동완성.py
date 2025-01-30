class Trie:
    def __init__(self):
        self.child = {}
        self.child_cnt = 0
        
    def insert(self, text):
        node = self
        for t in text:
            if t not in node.child:
                node.child[t] = Trie()
            node = node.child[t]
            node.child_cnt += 1
    
    def min_search(self, text):
        cnt = 0
        node = self
        
        for t in text:
            cnt += 1
            node = node.child[t]
            
            if len(node.child) == 0 or node.child_cnt == 1:
                break
                
        return cnt
    
    def printt(self):
        print(self.child_cnt, self.child.keys()) 
        for k, v in self.child.items():
            v.printt()
    
def solution(words):
    answer = 0
    trie = Trie()
    
    for word in words:
        trie.insert(word)
    
    for word in words:
        answer += trie.min_search(word)
        
    return answer