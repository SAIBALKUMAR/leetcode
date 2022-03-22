class Solution(object):
    def minSwapsCouples(self, row):
        """
        :type row: List[int]
        :rtype: int
        """
        dix={}
        for i in range(len(row)):
            dix[row[i]]=i
        i=0
        count=0
        while i<len(row)-1:
            if row[i]%2==0:
                if row[i+1]==row[i]+1:
                    i+=2
                else:
                    temp=dix[row[i]+1]
                    row[i+1],row[dix[row[i]+1]]=row[dix[row[i]+1]],row[i+1]
                    dix[row[i+1]]=i+1
                    dix[row[temp]]=temp
                    i+=2
                    count+=1
            else:
                if row[i+1]==row[i]-1:
                    i+=2
                else:
                    temp=dix[row[i]-1]
                    row[i+1],row[dix[row[i]-1]]=row[dix[row[i]-1]],row[i+1]
                    dix[row[i+1]]=i+1
                    dix[row[temp]]=temp
                    i+=2
                    count+=1
        return count       
        
                    