def solution(n, k, cmd):
    
    excel = LinkedNode(n, k)
    
    for c in cmd:
        if c[0] == "U":
            _, num = c.split()
            excel.prev(int(num))
            
        elif c[0] == "D":
            _, num = c.split()
            excel.next_(int(num))
            
        elif c == "C":
            excel.delete()
        else:
            excel.restore()
            
    return excel.result()


class LinkedNode:
    
    def __init__(self, size, k):
        self.li = [Node(i, size) for i in range(size)]
        self.stack = []
        self.point = k
        self.size = size

    def prev(self, cnt):
        for _ in range(cnt):
            self.point = self.li[self.point].prev
    
    def next_(self, cnt):
        for _ in range(cnt):
            self.point = self.li[self.point].next_
        
    def delete(self):
        now_node = self.li[self.point]
        
        if now_node.next_ == self.size:
            prev_node  = self.li[now_node.prev]
            prev_node.next_ = now_node.next_
            self.stack.append(self.point)
            self.point = now_node.prev
            
        else:
            prev_node, next_node = self.li[now_node.prev], self.li[now_node.next_]
            prev_node.next_ = now_node.next_
            next_node.prev = now_node.prev
            self.stack.append(self.point)
            self.point = now_node.next_
            
    
    def restore(self):
        re = self.stack.pop()
        re_node = self.li[re]
        
        if re_node.next_ == self.size:
            prev_node = self.li[re_node.prev]
            prev_node.next_ = re
            
        else:
            prev_node, next_node = self.li[re_node.prev], self.li[re_node.next_]
            prev_node.next_ = re
            next_node.prev = re
        
    def result(self):
        answer = ["O"] * self.size
        for idx in self.stack:
            answer[idx] = "X"
        
        return ''.join(answer)
        
        
class Node:
    def __init__(self, num, size):
        if num - 1 < 0:
            self.prev = -1
        else:
            self.prev = num - 1
        
        if num + 1 >= size:
            self.next_ = size
        else:
            self.next_ = num + 1
    
    def __str__(self):
        return f'{self.prev} and {self.next_}'
        