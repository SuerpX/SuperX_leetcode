class Solution(object):
    def isMatch(self, s, p):
        """
        :type s: str
        :type p: str
        :rtype: bool
        """
        st = [False] * (len(s) + 1)
        st[0] = True
        
        i = 0
        while i < len(p):
            if i < len(p) - 1 and p[i+1] == '*':
                prev = False
                for j in xrange(0, len(s)+1):
                    st[j] = st[j] or (prev and (s[j-1] == p[i] or '.' == p[i]))
                    prev = st[j]
                i += 2
            else:
                for j in xrange(len(s), 0, -1):
                    st[j] = st[j-1] and (s[j-1] == p[i] or '.' == p[i])
                st[0] = False
                i += 1
        return st[-1]
