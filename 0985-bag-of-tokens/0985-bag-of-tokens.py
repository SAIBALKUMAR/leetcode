class Solution:
    def bagOfTokensScore(self, tokens: List[int], power: int) -> int:
        left, right = 0, len(tokens) - 1
        tokens.sort()
        res = 0
        score = 0
        while left <= right:
            print(score, power, left,right)
            if power >= tokens[left]:
                power -= tokens[left]
                score += 1
                res = max(res, score)
                left += 1
            elif score > 0:
                score -= 1
                power += tokens[right]
                right -= 1
            else:
                break
            
            
        return res

