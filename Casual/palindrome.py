"""
Palindrome: Implement a function to check if a linked list is a palindrome. 
Hints:#5, #13, #29, #61, #101
"""

# It is easy if doubly linked list
# Time : O(n) : Space : O(1)

# if single linked list
# Solution 1 is to reverse the linked list and then compare
# time: O(n) : Space : O(n)

# iterative
def reverseLinkedList(head):
    if head is None:
        return head

    prev = None
    while head:
        nxt = head.next 
        head.next = prev 
        prev.next = nxt 
        prev = head

    return prev 

def reverseLinkedListRecursive(head):
    if head is None or head.next is None:
        return head

    nxt = reverseLinkedListRecursive(head.next)
    head.next.next = head
    head.next = None

    return nxt

# another way is to use the stack
# we can find the length and push the first half of the linked list in the stack
# and then pop the stack and compare it with the second half

def palindromeLinkedList(head):
    stack = []

    length = 0
    while temp:
        length += 1
        temp = temp.next 

    slow = fast = head
    while fast and fast.next:
        stack.append(slow.value)
        slow = slow.next 
        fast = fast.next 

    # if odd 
    if fast is not None:
        slow = slow.next 

    while slow:
        top = stack.pop()
        if slow.value != top:
            return False

        slow = slow.next

    return True
    
    
