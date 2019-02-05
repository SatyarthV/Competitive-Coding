class Solution:
    def judgeCircle(self, moves: 'str') -> 'bool':
        e = list(moves)
        mov = [0,0]

        for i in range(0,len(e)):
            if(e[i] == 'L'):
                mov[0] = mov[0] - 1
            if(e[i] == 'R'):
                mov[0] = mov[0] + 1
            if(e[i] == 'U'):
                mov[1] = mov[1] + 1
            if(e[i] == 'D'):
                mov[1] = mov[1] - 1

        if(mov[0] == 0 and mov[1] == 0):
            return True
        else:
            return False
