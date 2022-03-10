class Solution(object):
    def numOfMinutes(self, n, headID, manager, informTime):
        """
        :type n: int
        :type headID: int
        :type manager: List[int]
        :type informTime: List[int]
        :rtype: int
        """
        head=headID
        res=[head]
        informedTime={}  
        dix=defaultdict(list)
        for i in range(len(manager)):
            dix[manager[i]].append(i)
            informedTime[i]=0
            
        while len(res)>0:
            head=res.pop(0)
            for i in dix[head]:
                informedTime[i]=informTime[head] + informedTime[head]
                res.append(i)
        return max(informedTime.values())
            
                
        
                
        
        
                
                
        