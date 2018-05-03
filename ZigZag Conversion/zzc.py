class Solution(object):
    def convert(self, s, numRows):
        """
        :type s: str
        :type numRows: int
        :rtype: str
        """
        '''
        l = len(s)
 #       res = ""
 #       print(l)
        #print(x, end="")
        for i in range(numRows):
            for j in range(l // (numRows * 2 - 2) + 1):
                if j * (numRows * 2 - 2) + i < l:
                    print(s[j * (numRows * 2 - 2) + i], end = '')
                if i == 0 or i == numRows - 1:
                    print("   " * (numRows - 2), end = '')
                elif j * (numRows * 2 - 2) + i + (numRows - i - 1) * 2 < l:
                    print("   " * (numRows - 2 - i), end = '')
                    print(" " + str(s[j * (numRows * 2 - 2) + i + (numRows - i - 1) * 2] ) + " ", end = '')
                    print("   " * (i - 1), end = '')
            print("")
          '''
        if numRows == 1:
            return s
        l = len(s)
        res = ""
        for i in range(numRows):
            for j in range(l // (numRows * 2 - 2) + 1):
                if j * (numRows * 2 - 2) + i >= l:
                    break
                res += s[j * (numRows * 2 - 2) + i]
                if i == 0 or (i == numRows - 1):
                    continue
                if j * (numRows * 2 - 2) + i + (numRows - i - 1) * 2 >= l:
                    break
                res += s[j * (numRows * 2 - 2) + i + (numRows - i - 1) * 2]
        return res
        
        
        
s = Solution()
print(s.convert("PAYPALISHIRING", 3))
