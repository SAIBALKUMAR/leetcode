class Solution(object):
    def restoreIpAddresses(self, s):
        """
        :type s: str
        :rtype: List[str]
        """
        k=len(s)//4
        if k==0:
            return []
        i=0
        res=[]
        ans=[]
        
        def check(i,k,res):
            if k>=4:
                if len("".join(res))==len(s):
                    ans.append(res)
                    return 
                else:
                    return 
            if i+3<=len(s) and int(s[i:i+3])<256 and int(s[i:i+1])!=0:
                check(i+3,k+1,res+[str(s[i:i+3])])
            if i+2<=len(s) and int(s[i:i+2])<256 and int(s[i:i+1])!=0:
                check(i+2,k+1,res+[str(s[i:i+2])])
            if i+1<=len(s) and int(s[i:i+1])<256:
                check(i+1,k+1,res+[str(s[i:i+1])])
        
        check(0,0,[])
        for i in range(len(ans)):
            ans[i]=".".join(ans[i])
        return ans
        
            
                
            