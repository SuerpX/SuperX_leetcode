class Solution:
    def reverse(self, x):
        """
        :type x: int
        :rtype: int
        """
        n = 1
        if x < 0:
            n = -1
            x *= -1
        res = int(str(x)[::-1]) * n
        if res < -(2 ** 31) or res > (2 ** 31 - 1):
            return 0
        return res
        
