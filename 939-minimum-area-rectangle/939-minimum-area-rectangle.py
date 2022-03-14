class Solution(object):
    def minAreaRect(self, points):
        """
        :type points: List[List[int]]
        :rtype: int
        """
        length = len(points)
        
        if length < 4:
            return 0
        
        minimumArea = float("inf")
        
        hashSet = {}
        
        for x1, y1 in points:
            for x2, y2 in hashSet:
                if ((x2, y1) in hashSet and (x1, y2) in hashSet):
                    area = abs(y2-y1)*abs(x2-x1)
                    
                    if area and  area < minimumArea:
                        minimumArea = area
            hashSet[(x1,y1)]= (x1, y1)
                        
        return minimumArea if minimumArea != float('inf') else 0
    
        
        