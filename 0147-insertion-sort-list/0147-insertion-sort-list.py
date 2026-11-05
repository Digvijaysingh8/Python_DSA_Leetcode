# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def insertionSortList(self, head: ListNode | None) -> ListNode | None:
        if not head or not head.next:
            return head
        dummy=ListNode(0)
        dummy.next=head

        prev=head
        cur=head.next

        while cur:
            next_node=cur.next

            if prev.val <= cur.val:
                prev=cur

            else:

                temp=dummy
                while temp.next.val < cur.val:
                    temp=temp.next

                cur.next=temp.next

                temp.next=cur  
                prev.next=next_node  
            cur=next_node
        return dummy.next           
        