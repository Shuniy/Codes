"""
2.3  Delete Middle Node: Implement an algorithm to delete a node in the middle (i.e., any  node but 
the first and last node, not necessarily the exact middle) of a singly linked list, given only access to 
that node. 
EXAMPLE 
input:the node c from the linked list a->b->c->d->e->f 
Result: nothing is returned, but the new linked list looks like a - >b- >d- >e- >f 
"""

# since we don't have the head node so, only way is to delete the node and copy the next node

def middleNode(head):
    if head is None or head.next is None:
        return None

    nextNode = head.next
    head.data = nextNode.data
    head.next = nextNode.next 
    return True
