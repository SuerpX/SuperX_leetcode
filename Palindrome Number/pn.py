class Solution(object):
    def isPalindrome(self, x):
        """
        :type x: int
        :rtype: bool
        """
        '''
        s = str(x)
        return s[::-1] == s
        '''
        return x == int(str(x)[::-1]) if x >= 0 else False;
        
        

            
                    
