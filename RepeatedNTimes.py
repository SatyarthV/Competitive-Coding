class Solution:
    def repeatedNTimes(self, A):
        """
        :type A: List[int]
        :rtype: int
        """
        
        A.sort()
        for i in range(0,len(A)):
            if(A[i+1]-A[i] == 0):
                return(A[i])
                