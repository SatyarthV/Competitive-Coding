class Solution:
    def minDeletionSize(self, A: 'List[str]') -> 'int':
        r = []
        for i in range(len(A)):
            r.append(list(A[i]))

        count = 0

        if(len(A) == 2):
            if(ord(A[0]) > ord(A[1])):
                count += 1
            return count
        
        else:
            
            for j in range(len(r[0])):
                for i in range(len(r)-1):
                    if(ord(r[i][j]) > ord(r[i+1][j])):
                        count += 1
                        break
            return count
