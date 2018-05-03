class Solution:
    def myAtoi(self, s):
        """
        :type str: str
        :rtype: int
        """
        
        res = 0
        resflag = False
        nepo = 1
        for c in s:
            if c > '9' or c < '0':
                if resflag:
                    break
                if c == '-':
                    nepo = -1
                    resflag = True
                elif c == '+':
                    nepo = 1
                    resflag = True
                elif c != ' ':
                    break
            elif c <= '9' and c >= '0':
                res = res * 10 + int(c)
                if not resflag:
                    resflag = True
        res *= nepo
        if res > (2 ** 31 - 1):
            return 2 ** 31 - 1
        if res < -(2 ** 31):
            return -(2**31)
        return res
        
        

            
                    
