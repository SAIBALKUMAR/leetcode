class Solution(object):
    def numTilings(self, n):
        """
        :type n: int
        :rtype: int
        """
        A=[0]*(n+1)
        A[0]=1
        A[1]=1
        if n<2:
            return A[n]
        A[2]=2
        
            
        for i in range(3,n+1):
            A[i]=2*A[i-1]+A[i-3]
        return A[n]%(10**9+7)
        