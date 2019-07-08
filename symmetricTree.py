def isSymmetric(self, root: TreeNode):
        
    if root is None:
        return True
    
    res = []
    def preOrder(root):
        if root is None:
            return None

        res.append(root.val)

        if root.left is not None and root.right is not None:
            preOrder(root.left)
            preOrder(root.right)

        if root.left is None and root.right is not None:
            #print("HI")
            res.append(None)
            preOrder(root.right)

        if root.right is None and root.left is not None:
            preOrder(root.left)
            res.append(None)
    
    result = []
    def preOrderv(root):
        if root is None:
            return None

        result.append(root.val)

        if root.left is not None and root.right is not None:
            preOrderv(root.right)
            preOrderv(root.left)

        if root.right is None and root.left is not None:
            result.append(None)
            preOrderv(root.left)

        if root.left is None and root.right is not None:
            preOrderv(root.right)
            result.append(None)
    
    preOrder(root.left)
    preOrderv(root.right)
    print (res)
    print(result)
    if(res == result):
        return True
    else:
        return False