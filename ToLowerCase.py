class Solution:
    def toLowerCase(self, str):
        e = list(str)
        for i in range(len(e)):
            if(ord(e[i]) >= 65 and ord(e[i])<=90):
                j = ord(e[i]) + 32
                e[i] = chr(j)
        return(''.join(e))
