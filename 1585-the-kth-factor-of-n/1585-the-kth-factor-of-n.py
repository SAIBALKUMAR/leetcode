class Solution:
    def kthFactor(self, n: int, k: int) -> int:
        if (k == 0): 
            return 1
        factors = [1]
        if (n==1 and k==1):
             return 1
        for i in range(2, n+1):
            if (n%i == 0):
                factors.append(i)
            if (len(factors) >= k):
                return factors[k-1]
        return -1
        




            

