class Solution(object):
    def threeSum(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        dic = {}
        for ele in nums:
            if ele not in dic:
                dic[ele] = 0
            dic[ele] += 1

        if 0 in dic and dic[0] > 2:
            rst = [[0, 0, 0]]
        else:
            rst = []

        pos = [p for p in dic if p > 0]
        neg = [n for n in dic if n < 0]

        for p in pos:
            for n in neg:
                inverse = -(p + n)
                if inverse in dic:
                    if inverse == p and dic[p] > 1:
                        rst.append([n, p, p])
                    elif inverse == n and dic[n] > 1:
                        rst.append([n, n, p])
                    elif inverse < n or inverse > p or inverse == 0:
                        rst.append([n, inverse, p])

        return rst
        
