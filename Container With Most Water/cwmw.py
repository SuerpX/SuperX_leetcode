class Solution(object):
    def maxArea(self, height):
        """
        :type height: List[int]
        :rtype: int
        """


        l = len(height)
        maxC = -1
        p1 = 0
        p2 = l - 1
        isReverse = False
        while p2 > p1:
            if not isReverse:
                if height[p2] > height[p1]:
                    isReverse = True
                    c = height[p1] * (p2 - p1)
                    p1 += 1
                else:
                    c = height[p2] * (p2 - p1)
                    p2 -= 1
                
            else:
                if height[p1] > height[p2]:
                    isReverse = False
                    c = height[p2] * (p2 - p1)
                    p2 -= 1
                else:
                    c = height[p1] * (p2 - p1)
                    p1 += 1
            if c > maxC:
                maxC = c
        return maxC
                
        '''
        l = len(height)
        maxC = -1
        currL = -1
        currR = -1
        for i in range(l - 1):
            if height[i] > currL:
                currR = -1
                currL = height[i]
                for j in range(l - 1, i, -1):
  #                  print(currR, currL)
                    if currR >= currL:
 #                       print(111)
                        break
                        
                    currR = height[j]
                    h = min(currL, currR)
                    w = j - i
                    if h * w > maxC:
                        maxC = h * w
        return maxC
        '''
print(Solution().maxArea([1,2,3,4,5,6,7,8,9]))
