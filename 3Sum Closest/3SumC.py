class Solution(object):
    def threeSumClosest(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """

 #       print(nums)
        numsDict = {}
        numsResDict = {}
       # print(numsDict)
        tclosest = 1000
        
        
        for i, n1 in enumerate(nums):
            if n1 not in numsDict:
                numsDict[n1] = 0
            numsDict[n1] += 1
            for n2 in nums[i + 1 :]:
                numsResDict[n1, n2] = n1 + n2
  #      print(numsResDict)


        for (n1, n2) in numsResDict:
            if tclosest == target:
                return tclosest
            n12 = numsResDict[n1,n2]
            numsDict[n1] -= 1
            numsDict[n2] -= 1
            
            for d in range(0, abs(tclosest - target)):
 #               print(d, (n12 - (target + d)) * -1, (n12 - (target - d)) * -1)
                r = (n12 - (target + d)) * -1 
                if r in numsDict and numsDict[r] > 0 :
                    tclosest = target + d
                    break
                l = (n12 - (target - d)) * -1
                if l in numsDict and numsDict[l] > 0 :
                    tclosest = target - d
                    break
            numsDict[n1] += 1
            numsDict[n2] += 1

        '''
        for i, n1 in enumerate(nums):
            numsDict[n1] -= 1
            for n2 in nums[i + 1 :]:
 #               print(n2)
                if numsDict[n2] > 0:
                    numsDict[n2] -= 1
                    diff = target - tclosest
                    s = 0
                    e = 0
                    if diff > 0:
                        s = tclosest
                        e = target + diff + 1
                    else:
                        s = target + diff
                        e = tclosest
 #                   print(s,e)
 #                   print(n1,n2)
                    for d in range(s, e):
                        n3 = -1 * (n1 + n2 - d)
#                        print(n1, n2, d)
                        if n3 in numsDict and numsDict[n3] > 0:
                            tclosest = d
                    numsDict[n2] += 1
            numsDict[n1] += 1
        '''
        return tclosest
    
print(Solution().threeSumClosest([1,1,1,0], 100))

#print(Solution().threeSumClosest([1,1,2,5,1,6], 100))
