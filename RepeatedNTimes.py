class Solution:
    def repeatedNTimes(self, A):
        A.sort()
        for i in range(0,len(A)):
            if(A[i+1]-A[i] == 0):
                return(A[i])
                
