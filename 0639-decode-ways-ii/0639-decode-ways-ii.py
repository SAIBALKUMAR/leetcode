class Solution:
    def numDecodings(self, s: str) -> int:
        ## 681*7236*4178
        MOD = 10**9 + 7
        def findCount(index):
            if (index == len(s)):
                return 1
            if index in obj:
                return obj[index]
            if (s[index] == '0'):
                return 0
            result = 0
            if (s[index] == "*"):
                result += 9 * findCount(index + 1)
            else:
                result += findCount(index+1)

            if (index < len(s) -1):
                if (s[index] == '*'):
                    if (s[index+1] == '*'):
                        result += 15 * findCount(index+2)
                    elif s[index+1] in "0123456":
                        result += 2 * findCount(index+2)
                    else: 
                        result += findCount(index+2)
                elif s[index] == '1':
                    if (s[index+1] == '*'):
                        result += 9 * findCount(index+2)
                    else:
                        result += findCount(index+2)
                elif s[index] == '2':
                    if (s[index+1] == '*'):
                        result += 6 * findCount(index+2)
                    elif s[index+1] in "0123456":
                        result += findCount(index+2)
            
            obj[index] = result % MOD
            return obj[index]
        
        obj = {}
        return findCount(0)


            
                
        