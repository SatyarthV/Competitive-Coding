class Solution:
    def flipAndInvertImage(self, A):
        for i in range(0,len(A)):
            A[i] = list(reversed(A[i]))

        for j in range(len(A)):
            for i in range(len(A[j])):
                if(A[j][i] == 1):
                    A[j][i] = 0
                else:
                    A[j][i] = 1

        return(A)
        