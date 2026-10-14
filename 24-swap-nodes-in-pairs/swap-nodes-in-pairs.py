# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def swapPairs(self, head: ListNode | None) -> ListNode | None:
        node=ListNode(0)
        node.next=head
        current=node
        while current.next and current.next.next:
            first=current.next
            second=current.next.next

            first.next=second.next
            second.next=first
            current.next=second

            current=first
        return node.next
