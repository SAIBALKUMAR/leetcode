class Solution(object):
    def maxScore(self, cardPoints, k):
        """
        :type cardPoints: List[int]
        :type k: int
        :rtype: int
        """
#         res=[]
#         l=0
#         sumMax=max(sum(cardPoints[:k]),sum(cardPoints[-k:]))
#         r=len(cardPoints)
#         def sumiscore(cardPoints,k,sumi,l,r):
#             if k==0 or l>=r or sumi>=sumMax:
#                 res.append(sumi)
#                 return 
#             sumiscore(cardPoints[1:],k-1,sumi+cardPoints[0],l+1,r) 
#             sumiscore(cardPoints[:-1],k-1,sumi+cardPoints[-1],l,r-1) 
            
#         sumiscore(cardPoints,k,0,l,r)
#         return max(res)

        
        i=0
        sumTotal=sum(cardPoints)
        res=sumTotal
        n=len(cardPoints)
        sumi = sum(cardPoints[:n-k])
        for i in range(len(cardPoints)-(n-k)+1):
            if sumi<res:
                res=sumi
            if i+n-k <n:
                sumi=sumi-cardPoints[i]+cardPoints[i+n-k]
                
        return sumTotal-res
            
            