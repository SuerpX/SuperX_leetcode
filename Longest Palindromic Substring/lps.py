class Solution(object):
    def longestPalindrome(self, s):
        """
        :type s: str
        :rtype: str
        """
        maxS = 0
        maxE = 0
        longest = -1
        l = len(s)
        for i in range(l):
            '''
            if i == 0 or i == l - 1:
                continue
            '''
            p1 = i - 1
            p2 = i + 1
            long = 1
            while p1 >= 0 and p2 < l and s[p1] == s[p2]:
                long += 2
                p1 -= 1
                p2 += 1
            if longest < long:
                longest = long
                maxS = p1 + 1
                maxE = p2 - 1
            p1 = i
            p2 = i + 1
            long = 0
            while p1 >= 0 and p2 < l and s[p1] == s[p2]:
                long += 2
                p1 -= 1
                p2 += 1
            if longest < long:
                longest = long
                maxS = p1 + 1
                maxE = p2 - 1
        return s[maxS:maxE + 1]
            
