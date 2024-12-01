class Solution:
    def minDistance(self, word1: str, word2: str) -> int:
        dp2dArray = [[float(inf) for i in range(len(word2) +1)] for j in range(len(word1) +1)]

        for i in range(len(word1) + 1):
            dp2dArray[i][len(word2)] = len(word1) - i
        for j in range(len(word2) + 1):
            dp2dArray[len(word1)][j] = len(word2) - j
            
        for i in range(len(word1) -1, -1, -1):
            for j in range(len(word2)-1, -1, -1):
                if word1[i] == word2[j]:
                    dp2dArray[i][j] = dp2dArray[i+1][j+1]
                else:
                    dp2dArray[i][j] = 1 + min(dp2dArray[i+1][j+1], dp2dArray[i][j+1], dp2dArray[i+1][j])

        return dp2dArray[0][0]


        