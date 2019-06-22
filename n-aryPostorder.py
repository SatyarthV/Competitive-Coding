def nary_postorder(self, root):
        
        if(root == None):
            return None
        res = []
        def recursive(root,res):
            for i in root.children:
                recursive(i,res)
            res.append(root.val)
            
        recursive(root,res)
        return res

nary_postorder(root)
