class Solution(object):
    def intToRoman(self, num):
        """
        :type num: int
        :rtype: str
        """
        '''
        I             1
        V             5
        X             10
        L             50
        C             100
        D             500
        M             1000
        '''
        rn = {1: 'I', 5: 'V', 10 :'X', 50 : 'L', 100 : 'C', 500 : 'D', 1000 : 'M', 4 : 'IV', 9 : 'IX', 40 : 'XL', 90 : 'XC', 400 : 'CD', 900 : 'CM'}
        rm = ""
        k = 1000
        while num > 0:
 #           print(num, k)
            if num >= k:
                n = int(num // k)
                if n == 9 or n == 4:
                    rm += rn[n * k]
                    n = 0
                elif n >= 5:
                    rm += rn[5 * k]
                    n -= 5
                rm += rn[k] * n
            num %= k
            if k == 10:
                k = 1
            else:
                k /= 10
        return rm
print(Solution().intToRoman(1))
