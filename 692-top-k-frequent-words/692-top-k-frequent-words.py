class Solution(object):
    def topKFrequent(self, words, k):
        """
        :type words: List[str]
        :type k: int
        :rtype: List[str]
        """
        heap,res,dix,length = [],[],defaultdict(int),k
        
        for word in words:
            dix[word]+=1
        
        for k,v in dix.items():
            heapq.heappush(heap,(-v,k)) # -v for max heap implementation
            
        while length>0:
            res.append(heapq.heappop(heap)[1])
            length-=1
        return res
        
        