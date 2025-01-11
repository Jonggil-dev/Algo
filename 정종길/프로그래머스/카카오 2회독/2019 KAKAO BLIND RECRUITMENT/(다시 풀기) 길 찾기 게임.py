import sys
sys.setrecursionlimit(10000)

class Node:
    def __init__(self, idx, x, y):
        self.idx = idx
        self.x = x
        self.y = y
        self.left = None
        self.right = None

class BinaryTree:
    global answer
    
    def __init__(self, root):
        self.root = root
        
    def insert(self, node, idx, x, y):
        if x < node.x:
            if node.left == None:
                node.left = Node(idx, x, y)
            else:
                self.insert(node.left, idx, x, y)
        else:
            if node.right == None:
                node.right = Node(idx, x, y)
            else:
                self.insert(node.right, idx, x, y)
    
    def preorder(self, node):
        answer[0].append(node.idx)
        
        if node.left:
            self.preorder(node.left)
        
        if node.right:
            self.preorder(node.right)
        
    def postorder(self, node):
        if node.left:
            self.postorder(node.left)
        
        if node.right:
            self.postorder(node.right)
            
        answer[1].append(node.idx)
        

def solution(nodeinfo):
    global answer
    
    answer = [[],[]]
    
    for i in range(len(nodeinfo)):
        nodeinfo[i].append(i + 1)
    
    nodeinfo.sort(key= lambda x : -x[1])
    root_node = Node(nodeinfo[0][2], nodeinfo[0][0], nodeinfo[0][1])
    bin_tree = BinaryTree(root_node)
    
    for j in range(1, len(nodeinfo)):
        x, y, idx = nodeinfo[j]
        bin_tree.insert(root_node, idx, x, y)
    
    bin_tree.preorder(root_node)
    bin_tree.postorder(root_node)
    
    
    return answer