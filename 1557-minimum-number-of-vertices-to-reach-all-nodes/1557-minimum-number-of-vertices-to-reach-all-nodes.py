class Solution(object):
    def findSmallestSetOfVertices(self, n, edges):
        """
        :type n: int
        :type edges: List[List[int]]
        :rtype: List[int]
        """
        check={}
        ans=[]
        for i,j in edges:
            check[j]=False
        for i in range(n):
            if i not in check:
                ans.append(i)
        return ans
        
        