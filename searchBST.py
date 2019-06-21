def searchBST(root, val):
    
    def printSubTree(root):
        if(root is not None):
            a.append(root.val)
            printSubTree(root.left)
            printSubTree(root.right)
            return
        
    def search_BST(root,val):
        if(root != None):
            if(root.val == val):
                printSubTree(root)
                return
            print(root.val)
            search_BST(root.left,val)
            search_BST(root.right,val)
    
            return a
        else:
            return []
        
    a = []
    b = search_BST(root,val)
    return b


def searchBST(self, root, val):
        
    if root is not None and val < root.val: 
        return self.searchBST(root.left, val)
    elif root is not None and val > root.val: 
        return self.searchBST(root.right, val)
    return root
