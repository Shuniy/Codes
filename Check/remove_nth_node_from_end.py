# Time : O(n)
# Space : O(1)
def remove_nth_node_from_end(head, n):
    
    if n >= 0 and head is None:
        return None

    counter = 1

    first = head
    second = head
    header = head

    while counter <= n:
        second = second.next
        counter += 1

    if second is None:
        head.value = head.next.value
        head.next = head.next.next
        return header

    while second.next is not None:
        second = second.next
        first = first.next

    first.next = first.next.next

    return header


    