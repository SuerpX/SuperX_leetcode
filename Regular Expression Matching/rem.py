class Solution(object):
    def isMatch(self, s, p):
        dp = {}
        ls = len(s)
        lp = len(p)
        def _isMatch(i, j):
            if (i, j) in dp:
                return dp[i,j]
            if j == lp:
                dp[i,j] = i == ls
                return dp[i,j]
            match = i < ls and (s[i] == p[j] or p[j] == '.')
            if match:
                res = _isMatch(i + 1,j + 1)
                if j + 1 < lp and p[j + 1] == '*':
                    res = res or _isMatch(i, j + 2) or _isMatch(i + 1, j)
            else:
                res = False
                if j + 1 < lp and p[j + 1] == '*':
                    res = _isMatch(i, j + 2)
            dp[i,j] = res
            return dp[i,j]
        res = _isMatch(0,0)
#        print(dp)
        return res
#print(Solution().isMatch("mississippi", "mis*is*p*."))
