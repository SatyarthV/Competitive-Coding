def increasingBST(self, root):
    def inorderTraversal(root):
    			res = []    
    			if root:   
    				res = inorderTraversal(root.left)      
    				res.append(root.val)        
    				res = res + inorderTraversal(root.right)        
    			return res
    			
    nodes = inorderTraversal(root)
    result = TreeNode(nodes[0])
    node = result
    
    for i in range(1,len(nodes)):
        node.right = TreeNode(nodes[i])
        node = node.right
    
    return result