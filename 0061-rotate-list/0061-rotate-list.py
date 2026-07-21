class Solution:
    def rotateRight(self, head, k):
        if not head or not head.next or k==0:
            return head
        n=1
        tail=head
        while tail.next:
            tail=tail.next
            n+=1
        k%=n
        if k==0:
            return head
        tail.next=head
        steps=n-k-1
        newTail=head
        for _ in range(steps):
            newTail=newTail.next
        newHead=newTail.next
        newTail.next=None
        return newHead