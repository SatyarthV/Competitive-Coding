class Solution:
    def sumEvenAfterQueries(self, A: 'List[int]', queries: 'List[List[int]]') -> 'List[int]':
        
        res = []
        count = sum(num for num in A if not num%2)
        for j in range(len(queries)):
            a = A[queries[j][1]] + queries[j][0]
            #b = queries[j][1]
            if(a%2 == 0 and A[queries[j][1]]%2 == 0):
                count += queries[j][0]

            if(a%2 == 0 and A[queries[j][1]]%2 != 0):
                count += a

            if(a%2 != 0 and A[queries[j][1]]%2 == 0):
                count -= (A[queries[j][1]])

            A[queries[j][1]] = a
            res.append(count)
        return(res)

        
        
        