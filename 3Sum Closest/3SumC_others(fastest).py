class Solution:
    def threeSumClosest(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        nums.sort()
        length = len(nums)
        closest = []
        
        for i, num in enumerate(nums[0:-2]):
            l,r = i+1, length-1
						
            # different with others' solution
						
            if num+nums[r]+nums[r-1] < target:
                closest.append(num+nums[r]+nums[r-1])
            elif num+nums[l]+nums[l+1] > target:
                closest.append(num+nums[l]+nums[l+1])
            else:
                while l < r:
                    closest.append(num+nums[l]+nums[r])
                    if num+nums[l]+nums[r] < target:
                        l += 1
                    elif num+nums[l]+nums[r] > target:
                        r -= 1
                    else:
                        return target
                    
        closest.sort(key=lambda x:abs(x-target))
        return closest[0]
#         if len(nums) < 4:
#             return sum(nums)
#         nums.sort()
#         res = float('inf')
#         for i in range(len(nums) - 2):
#             left = i
#             mid = i + 1
#             right = len(nums) - 1
#             while mid < right:
#                 mid_ans = nums[left] + nums[mid] + nums[right]
#                 if abs(mid_ans - target) < abs(res - target):
#                     res = mid_ans
#                     if res == target:
#                         return target
                
                
#                 if nums[left] + nums[mid] + nums[right] < target:
#                     mid += 1
#                 elif nums[left] + nums[mid] + nums[right] > target:
#                     right -= 1
#         return res
        
        
        
        
        
        
        
        
        
        
        
        

        
        
#         nums.sort(reverse = True)
#         # print(nums)
#         res = float('inf')
#         for i in range(len(nums) - 2):
#             left = nums[i]
#             for j in range(i + 1, len(nums) - 1):
#                 right = nums[j]
#                 need = target - (left + right)
#                 #use binary search here to reduce time
                
                
#                 # k = j + 1
#                 # while k < len(nums) and nums[k] > need:
#                 #     k += 1
#                 # k = min(k, len(nums) - 1)
#                 # # print(j + 1, k)
#                 # if k == j + 1:
#                 #     mid = left + right + nums[k] 
#                 #     if abs(mid - target) < abs(res - target):
#                 #         res = mid
#                 # else:
#                 #     mid1 = left + right + nums[k]
#                 #     mid2 = left + right + nums[k - 1]
#                 #     if abs(mid1 - target) < abs(res - target):
#                 #         res = mid1
#                 #     if abs(mid2 - target) < abs(res - target):
#                 #         res = mid2
                
#         return res
                    
        # nums.sort()
        # if len(nums) <= 3:
        #     return sum(nums)
        # ans = sum(nums[:3])
        # for i in range(0, len(nums) - 2):
        #     j = i + 1
        #     k = len(nums) - 1
        #     while j < k:
        #         mid = nums[i] + nums[j] + nums[k]
        #         if abs(target - ans) > abs(target - mid):
        #             ans = mid
        #             if ans == target:
        #                 return ans
        #         if mid > target:
        #             k -= 1
        #         else:
        #             j += 1
        # return ans            
        
         
