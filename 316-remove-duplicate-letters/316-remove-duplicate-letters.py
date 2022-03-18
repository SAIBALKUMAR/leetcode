class Solution(object):
    def removeDuplicateLetters(self, s):
        dix={char: indx for indx, char in enumerate(s)}
        
        res = []
        
        for indx, char in enumerate(s):
            if char not in res:
                while res and indx < dix[res[-1]] and char<res[-1] :
                    res.pop()
                res.append(char)
        return "".join(res)
            
            
                
                