def rangeSumBST(root, L, R):
    def sum_Tree(root,L,R,total):
        if(root.left != None):
            sum_Tree(root.left,L,R,total)
        
        if(root.val >= L and root.val <= R):
            total.append(root.val)
        
        if(root.right != None):
            sum_Tree(root.right,L,R,total)
    
        return total
    total = []
    return sum(sum_Tree(root,L,R,total))

