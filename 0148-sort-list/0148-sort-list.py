# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def sortList(self, head: ListNode | None) -> ListNode | None:

        if head is None or head.next is None:
            return head

        slow = head
        fast = head
        prev = None


        while fast and fast.next:
            prev=slow
            slow=slow.next
            fast=fast.next.next
        prev.next=None


        left = self.sortList(head)
        right = self.sortList(slow)

        return self.merge(left,right)

    def merge(self, left: Optional[ListNode], right: Optional[ListNode]) -> Optional[ListNode]:
        dummy = ListNode(0)
        tail = dummy

        while left and right:
            if left.val<right.val:
                tail.next=left
                left=left.next
                
            else:
                tail.next=right
                right=right.next

            tail=tail.next
        if left:
            tail.next=left
        else:
            tail.next=right
        return dummy.next                
                           
        