def hasPathSum(self, root, sum):
    if root is None:
        return False
    if root.right == None and root.left == None and root.val == sum:
        return True
    sum = sum - root.val
    return self.hasPathSum(root.left, sum) or self.hasPathSum(root.right,sum)