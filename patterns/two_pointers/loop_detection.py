"""
Loop Detection: Given a circular linked list, implement an algorithm that returns the node at the 
beginning of the loop. 
DEFINITION 
Circular linked list: A (corrupt) linked list in which a node's next pointer points to an earlier node, so 
as to make a loop in the linked list. 
EXAMPLE 
Input:  A  ->  B  ->  C  ->  D  ->  E  ->  C [the same C as earlier] 
Output:  C 
Hints: #50, #69, #83, #90
"""

# time : O(n) : space : O(1)
def loopDetection(head):
    slow = fast = head 

    while fast and fast.next:
        slow = slow.next 
        fast = fast.next.next
        if slow == fast:
            # loop found return or stay
            break  

    if fast is None or fast.next is None:
        return False

    slow = head
    while slow != fast:
        slow = fast 
        fast = fast.next 

    return fast