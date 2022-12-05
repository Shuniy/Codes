# Time : O(n)
# Space : O(1)

def reverse_linked_list(head):
    if head is None or head.next is None:
        return head

    p1 = None
    p2 = head

    while p2 is not None:
        p3 = p2.next 
        p2.next = p1
        p1 = p2
        p2 = p3

    head = p1

    return head    