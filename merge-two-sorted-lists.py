class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        merged = ListNode(0)
        if list1 is None:
            merged = list2
        elif list2 is None:
            merged = list1
        elif list1.val < list2.val:
            list1.next = self.mergeTwoLists(list1.next, list2)
            merged = list1        
        else:
            list2.next = self.mergeTwoLists(list1, list2.next)
            merged = list2
        return merged