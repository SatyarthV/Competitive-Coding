class Solution:
    def sortArrayByParity(self, A):
        even = []
        odd = []
        for i in range(0,len(A)):
            if(A[i]%2 == 0):
                even.append(A[i])
            else:
                odd.append(A[i])
        even = even + odd
        return(even)