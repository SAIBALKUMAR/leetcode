class Solution(object):
    def findRepeatedDnaSequences(self, s):
        """
        :type s: str
        :rtype: List[str]
        """
        dix={}
        i=0
        res=set()
        while i+10<=len(s):
            if s[i:i+10] not in dix:
                dix[s[i:i+10]] =1
                # if (s[i:i+10]=="AAAAAAAAAA" or s[i:i+10] == "CCCCCCCCCCC" or s[i:i+10] == "GGGGGGGGGG" or s[i:i+10] == "TTTTTTTTTT") :
                #     res.add(s[i:i+10])
            else:
                dix[s[i:i+10]]+=1
                res.add(s[i:i+10])
            i+=1
        return res