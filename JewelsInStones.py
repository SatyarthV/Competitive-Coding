@author: satyarthvaidya
"""

class Solution:
    
    def numJewelsInStones(J, S):
        
        j_contents = list(J)
        count = 0
        for i in j_contents:
            count = count + S.count(i)
        return count
