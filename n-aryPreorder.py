def narypreorder(self, root):
        """
        :type root: Node
        :rtype: List[int]
        """
        if(root == None):
            return None
        res = []
        def recursive(root,res):
            res.append(root.val)
            for i in root.children:
                recursive(i,res)
            #res.append(root.val)
            
        recursive(root,res)
        return res