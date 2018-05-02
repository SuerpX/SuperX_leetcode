class Solution(object):
    def findMedianSortedArrays(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: float
        """
        n = len(nums1)
        m = len(nums2)
        half_len = (m + n + 2) // 2
        pa = 0
        pb = 0
        count = 0
        newNum = []
        while count < half_len and pa < n and pb < m:
            if nums1[pa] <= nums2[pb]:
                newNum.append(nums1[pa])
                pa += 1
            else:
                newNum.append(nums2[pb])
                pb += 1
            count += 1
     #   print(newNum,count,half_len)
        while count < half_len :
            if pa < n:
                newNum.append(nums1[pa])
                pa += 1
            elif pb < m:
                newNum.append(nums2[pb])
                pb += 1
            count += 1
       # print(newNum,count,(m + n) % 2,newNum[count - 1] + newNum[count - 2])
        if (m + n) % 2 == 1:
            return newNum[count - 1]
        else:
            return (newNum[count - 1] + newNum[count - 2]) / 2.0
