class Solution(object):
    def longestPalindrome(self, s):
        """
        :type s: str
        :rtype: str
        """
        maxS = 0
        maxE = 0
        longest = 1
        l = len(s)
        for i in range(l):
            '''
            if i == 0 or i == l - 1:
                continue
            '''
        #    print(i,s[i - (longest - 1) // 2 - 1 : i],s[i + (longest - 1) // 2 + 1: i : -1 ] , longest)
            if s[i - (longest - 1) // 2 - 1 : i] == s[i + (longest - 1) // 2 + 1: i : -1 ]: 
              #  print(p1,p2,longest)
                p1 = i - (longest - 1) // 2 - 2
                p2 = i + (longest - 1) // 2 + 2
          #      long = longest + 2
                if longest % 2 == 0:
                    long = longest + 1
                else:
                    long = longest + 2
                while p1 >= 0 and p2 < l and s[p1] == s[p2]:
                    long += 2
                    p1 -= 1
                    p2 += 1
                if longest < long:
                    longest = long
                    maxS = p1 + 1
                    maxE = p2 - 1
         #   print(s[i - longest // 2 : i + 1],s[ i + longest // 2 + 1 : i : -1], longest, "2222")
            if s[i - longest // 2 : i + 1] == s[i + longest // 2 + 1 : i : -1]:
                p1 = i - longest // 2
                p2 = i + longest // 2 + 1
                if longest % 2 == 0:
                    long = longest
                else:
                    long = longest - 1
                while p1 >= 0 and p2 < l and s[p1] == s[p2]:
                    long += 2
                    p1 -= 1
                    p2 += 1
            #    print(longest, long)
                if longest < long:
                    longest = long
                    maxS = p1 + 1
                    maxE = p2 - 1
        return s[maxS:maxE + 1]
