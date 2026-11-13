class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def getIntersectionNode(self, headA, headB):

        pA = headA
        pB = headB

        while pA != pB:

            if pA is None:
                pA = headB
            else:
                pA = pA.next

            if pB is None:
                pB = headA
            else:
                pB = pB.next

        return pA