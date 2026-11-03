# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def rotateRight(self, head: ListNode | None, k: int) -> ListNode | None:
        if not head or not head.next:
            return head

        len=1
        tail=head

        while tail.next:
            tail=tail.next
            len+=1

        k=k%len

        if k==0:
            return head

        tail.next=head

        steps=len-k-1
        new_tail=head

        for i in range(steps):
            new_tail=new_tail.next

        new_head=new_tail.next

        new_tail.next=None

        return new_head               