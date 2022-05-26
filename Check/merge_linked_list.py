class LinkedList:
    def __init__(self, data) -> None:
        self.data = data
        self.next = None

# Time : O(n + m)
# Space : O(n + m)

def merge_linked_list_recursive(head1, head2):
    if head1 is None:
        return head2

    if head2 is None:
        return head1

    if head1.data < head2.data:
        head1.next = merge_linked_list_recursive(head1.next, head2)
        return head1
    else:
        head2.next = merge_linked_list_recursive(head1, head2.next)
        return head2

# Time : O(n + m)
# Space : O(n + m)
def merge_linked_list_extraspace(head1, head2):
    if head2 is None:
        return head1

    if head1 is None:
        return head2
    
    node1 = head1
    node2 = head2

    new_ll = new_head = LinkedList(0)

    while node1 is not None and node2 is not None:
        if node1.data < node2.data:
            new_ll.next = node1
            new_ll = new_ll.next 
            node1 = node1.next 
        else:
            new_ll.next = node2
            new_ll = new_ll.next 
            node2 = node2.next 

    if node1 is not None:
        new_ll.next = node1 
    elif node2 is not None:
        new_ll.next = node2

    return new_head.next


# Time : O(n + m)
# Space : O(1)

def merge_linked_list(head1, head2):
    p1 = head1
    p1_prev = None
    p2 = head2

    while p1 is not None and p2 is not None:
        if p1.data < p2.data:
            p1_prev = p1
            p1 = p1.next 
        else:
            if p1_prev is not None:
                p1_prev.next = p2 
            
            p1_prev = p2
            p2 = p2.next
            p1_prev.next = p1
    
    if p1 is None:
        p1_prev.next = p2
    
    return head1 if head1.data < head2.data else head2