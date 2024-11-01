class Solution:
    def hIndex(self, citations: List[int]) -> int:
        numOfCitations = len(citations)
        paperCounts = [0] * (numOfCitations+1)

        for c in citations: 
            paperCounts[min(c,numOfCitations)] += 1
        
        hIndex = numOfCitations
        papers = paperCounts[numOfCitations] 

        while papers < hIndex:
            hIndex -=1
            papers += paperCounts[hIndex]
        return hIndex


