# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def addTwoNumbers(self, l1, l2, plusOne = 0, res = None):
        """
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        """
        if res is None:
            res = []
        if l1 is None and l2 is None:
            if plusOne == 1:
                res.append(plusOne)
            return res
        
        if l1 is not None and l2 is not None:
            sum = l1.val + l2.val + plusOne
        elif l1 is not None:
            sum = l1.val + plusOne
        elif l2 is not None:
            sum = l2.val + plusOne
        plusOne = sum // 10
        res.append(sum % 10)
        return  self.addTwoNumbers((l1.next if l1 is not None else None), (l2.next if l2 is not None else None), plusOne,res)
