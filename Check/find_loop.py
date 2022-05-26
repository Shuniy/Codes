# Time : O(n) //It traverse exactly N+1 nodes and not about n nodes.
# Space : O(1)

def find_loop(head):
    if head is None or head.next is None:
        return head

    first = head
    second = head.next.next

    while first != second:
        first = first.next
        second = second.next.next 

    first = head
    while first != second:
        first = first.next 
        second = second.next 

    return first
    