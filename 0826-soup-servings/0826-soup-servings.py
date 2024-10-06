class Solution:
    def soupServings(self, n: int) -> float:
        if (n > 5000):
            return 1
        
        n = n // 25 + (1 if n %25 else 0)

        visited = defaultdict(int)
        def dp(soup_a, soup_b):
            if (soup_a <=0):
                if (soup_b <=0):
                    return 0.5 
                else:
                    return 1
            if (soup_b <= 0):
                return 0
            if (soup_a,soup_b) in visited:
                return visited[(soup_a, soup_b)]
            visited[(soup_a, soup_b)] = 0.25 * (dp(soup_a - 4, soup_b) + dp(soup_a - 3, soup_b-1) + dp(soup_a -2, soup_b -2) + dp(soup_a -1, soup_b-3))

            return visited[(soup_a, soup_b)]
        return dp(n,n)
