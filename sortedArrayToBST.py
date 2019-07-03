def sortedArrayToBST(nums):
    
    if not nums: 
        return None
    mid = (len(nums)) // 2
    root = TreeNode(nums[mid]) 
    root.left = sortedArrayToBST(nums[:mid]) 
    root.right = sortedArrayToBST(nums[mid+1:]) 
    return root 

lis = [-10,-3,0,5,9]

a = sortedArrayToBST(lis)
