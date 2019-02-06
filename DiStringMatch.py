class Solution:
    def diStringMatch(self, S: 'str') -> 'List[int]':
        i = list(S)
        b = len(i) 
        f = 0
        res = [0]*(len(i)+1)
        for j in range(len(i)):
            if(i[j] == 'I'):
                res[j] = f
                f+=1
            else:
                res[j] = b
                b-=1

        if(i[j] == 'I'):
            res[j+1] = f
        else:
            res[j+1] = b
            
        return(res)
