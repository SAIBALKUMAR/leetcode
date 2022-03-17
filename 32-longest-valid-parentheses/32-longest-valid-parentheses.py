class Solution(object):
    def longestValidParentheses(self, s):
        """
        :type s: str
        :rtype: int
        """
        stack=[-1]
        res=0
        for i in range(len(s)):
            if (s[i] == "("):
                stack.append(i)
            else:
                stack.pop()
                if len(stack) == 0:
                    stack.append(i)
                else:
                    res = max(res, (i - stack[-1]))
        return res 