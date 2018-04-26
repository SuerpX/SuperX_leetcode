class Solution(object):
    def lengthOfLongestSubstring(self, s):
        """
        :type s: str
        :rtype: int
        """
        '''
        tempres = {}
        longest = float('-inf')
        lres = {}
        for i, c1 in enumerate(s):
            tempres = {}
            tempres[c1] = True
            for c2 in s[i + 1:]:
                if c2 in tempres:
                    break
                tempres[c2] = True
            if len(tempres) > longest:
                longest = len(tempres)
                lres = tempres
        return "".join(r for r in lres)
        '''
        start = 0
        visited = {}
        longest = 0
        for i, c in enumerate(s):
            if c in visited and start <= visited[c]:
                start = visited[c] + 1
            else:
                longest = max(longest, i - start + 1)
            visited[c] = i
            
        return longest
                
print(Solution().lengthOfLongestSubstring("abcabcbb"))

