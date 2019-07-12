class Node:
    def __init__(self, val, children):
        self.val = val
        self.children = children

class Solution:
    def levelOrder(self, root):
        stack = [(root, 0)]
        res = []
        #print(type(root.children))
        while stack:
            node, level = stack.pop()
            if node:
                if len(res) < level+1:
                    res.insert(len(res), [])
                res[(level)].append(node.val)
                for i in node.children[::-1]:
                    stack.append((i,level+1))
        
        return res
