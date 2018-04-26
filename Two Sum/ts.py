class Solution(object):
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        tempnums = sorted(nums)
        p1 = 0
        p2 = len(tempnums) - 1
        while p1 < p2:
            if tempnums[p1] + tempnums[p2] < target:
                p1 += 1
            elif tempnums[p1] + tempnums[p2] > target:
                p2 -= 1
            elif tempnums[p1] + tempnums[p2] == target:
                num1 = tempnums[p1]
                num2 = tempnums[p2]
                break
        res1 = -1
        res2 = -1
        for i,n in enumerate(nums):
            if num1 == n and res1 == -1:
                res1 = i
            elif num2 == n and res2 == -1:
                res2 = i
        return [res1,res2]
        
        
        """
        for i, p1 in enumerate(nums[:-1]):
            for j, p2 in enumerate(nums[i + 1:]):
                if p1 + p2 == target:
                    return [i,i + j + 1]
        """
