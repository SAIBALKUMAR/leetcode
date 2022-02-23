class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        
        minheap=[]
        for i in range(len(points)):
            minheap.append([points[i][0]**2 + points[i][1]**2,points[i][0],points[i][1]])
        
        heapq.heapify(minheap)
        res=[]
        while len(res)<k:
            dist,x,y=heapq.heappop(minheap)
            res.append([x,y])
        return res