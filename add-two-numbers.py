# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        li1=[]
        li2=[]
        num1=0
        p=l1
        p2=l2
        while p:
            li1.append(p.val)
            p=p.next
        while p2:
            li2.append(p2.val)
            p2=p2.next           
        li1.reverse()
        li2.reverse()
        num1=int("".join(map(str, li1)))
        num2=int("".join(map(str, li2)))
        num2+=num1
        s =[int(i) for i in str(num2)]
        s.reverse()
        sol=ListNode()
        p=sol
        for i in range(len(s)):
            p.val=s[i]
            if i!=len(s)-1:
                p.next=ListNode()
                p=p.next
        return sol