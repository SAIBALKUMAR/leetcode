class Solution(object):
    def findSubstringInWraproundString(self, p):
        """
        :type p: str
        :rtype: int
        """
#         if len(p)==1:
#             return 1
#         dp=set()
#         def check(string):
#             if len(string)==1:
#                 return True
#             res=[]
            
#             for i in string:
#                 if len(res)>0 and (res[-1]+1!=ord(i)-ord('a') or (res[-1]==25 and i!='a')) :
#                     return False
#                 res.append(ord(i)-ord('a'))
#             return True
            
#         for i in range(len(p)):
#             for j in range(i+1,len(p)+1):
#                 string=p[i:j]
#                 print(string)
#                 if check(string) and string not in dp:
#                     dp.add(string)
#         print(dp)   
#         return len(dp)
        d = defaultdict(int)
        last, cnt = p[0], 0
        for char in p:
            d[last] = max(d[last], cnt)
            if ord(char)-ord(last)==1 or last+char=='za':                
                cnt+=1
            else:
                cnt=1
            last = char
        d[last] = max(d[last], cnt)
        #print(d)
        
        ans = sum(d[letter] for letter in d)
        return ans