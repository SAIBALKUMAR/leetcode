from copy import deepcopy
class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        if len(s1)>len(s2):
            return False
        dixs1={}
        k=len(s1)
        for i in range(len(s1)):
            if s1[i] not in dixs1:
                dixs1[s1[i]]=1
            else:
                dixs1[s1[i]]+=1
        dixs2={}
        count=0
        for i in range(len(s2)):
            count+=1
            if s2[i] not in dixs2:
                dixs2[s2[i]]=1
            else:
                dixs2[s2[i]]+=1
            if count==len(s1):
                shared_items = {k: dixs1[k] for k in dixs1 if k in dixs2 and dixs1[k] == dixs2[k]}
                if len(shared_items)==len(dixs1):
                    return True
                else:
                    dixs2[s2[i-count+1]]-=1
                count-=1
        return False
        