# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def swapPairs(self, head: ListNode | None) -> ListNode | None:
        dummy=ListNode(0)
        dummy.next=head
        prev=dummy

        while prev.next and prev.next.next:
            f=prev.next
            s=f.next


            #swap logic
            f.next=s.next
            s.next=f
            prev.next=s

            prev=f

        return dummy.next    
        