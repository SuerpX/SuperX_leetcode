class Solution(object):
    def threeSum(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        visited = set()
        numDict = {}
        res = []
        nums = sorted(nums)
        left = 0
        r = len(nums) - 1
        print(nums)
        visited = set()
        last = None
        for i, n1 in enumerate(nums[:]):
            left = 0
            right = r
            if n1 not in visited:
                if n1 == last:
                    visited.add(n1)
                while left < right and left < i and right >i:
                    m = (nums[left] + nums[right]) * -1
              #      print(nums[left], n1, nums[right])
                    if m < n1:
                        right -= 1
                    elif m > n1:
                        left += 1
                    elif m == n1:
                        if (nums[left], n1, nums[right]) not in visited:
                            res.append([nums[left], n1, nums[right]])
                            visited.add((nums[left], n1, nums[right]))
                        right -= 1
                        left += 1
            last = n1
                
        return res
