"""
Sum Lists: You have two numbers represented by a linked list, where each node contains a single 
digit. The digits are stored in reverse order, such that the 1 's digit is at the head of the list. Write a 
function that adds the two numbers and returns the sum as a linked list. 
EXAMPLE 
Input: (7->  1  -> 6)  + (5  ->  9  ->  2).Thatis,617  +  295. 
Output: 2  ->  1  ->  9. That is, 912. 
FOLLOW UP 
Suppose the digits are stored in forward order. Repeat the above problem. 
EXAMPLE 
lnput:(6  ->  1  ->  7)  + (2  ->  9  ->  5).Thatis,617  +  295. 
Output: 9  ->  1  ->  2. That is, 912. 
Hints: #7, #30, #71, #95, #109
"""

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next


class Solution:
    def reverse_linked_list(self, head):
        current = head
        prev = None
        while current:
            temp = current.next
            current.next = prev
            prev = current
            current = temp

        return prev

    def addTwoNumbers(self, l1: ListNode, l2: ListNode) -> ListNode:

        #r_l1 = self.reverse_linked_list(l1)
        #r_l2 = self.reverse_linked_list(l2)
        r_l1 = l1
        r_l2 = l2

        ans = l = ListNode(0)

        carry = 0
        value = 0

        while not(r_l1 is None and r_l2 is None):
            rl1 = 0
            rl2 = 0
            print
            if r_l1 is None:
                rl1 = 0
            else:
                rl1 = r_l1.val
            if r_l2 is None:
                rl2 = 0
            else:
                rl2 = r_l2.val

            value = rl1 + rl2 + carry
            print(value)
            if value > 9:
                k = value % 10
                carry = value // 10
                value = k
            else:
                carry = 0

            summ_node = ListNode(value)
            ans.next = summ_node
            ans = ans.next
            if r_l1 is not None and r_l1.next:
                r_l1 = r_l1.next
            else:
                r_l1 = None

            if r_l2 is not None and r_l2.next:
                r_l2 = r_l2.next
            else:
                r_l2 = None

        if carry != 0:
            ans.next = ListNode(carry)

        return l.next
