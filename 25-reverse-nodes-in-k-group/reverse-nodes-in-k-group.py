# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseKGroup(self, head: ListNode | None, k: int) -> ListNode | None:
        node=ListNode(0)
        node.next=head
        group_prev=node
        while True:
            kth=group_prev
            for i in range(k):
                kth=kth.next
                if not kth:
                    return node.next
            group_next=kth.next
            prev=group_next
            current=group_prev.next
            while current != group_next:
                temp=current.next
                current.next=prev
                prev=current
                current=temp
            temp=group_prev.next
            group_prev.next=kth
            group_prev=temp
        return node.next
        