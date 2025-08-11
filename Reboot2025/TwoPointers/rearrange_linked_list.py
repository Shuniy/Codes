from __future__ import print_function

class Node:
    def __init__(self, value, next = None):
        self.value = value
        self.next: Node = next

    def print_list(self):
        temp = self
        while temp:
            print(str(temp.value) + " ", end='')
            temp = temp.next
        print()

def reorder(head: Node):
    if head is None or head.next is None:
        return
    
    slow, fast = head, head
    while fast and fast.next:
        slow = slow.next
        fast = fast.next.next

    head_second_half = reverse(slow)
    head_first_half = head

    while head_first_half and head_second_half:
        temp = head_first_half.next
        head_first_half.next = head_second_half
        head_first_half = temp

        temp = head_second_half.next
        head_second_half.next = head_first_half
        head_second_half = temp
    
    if head_first_half:
        head_first_half.next = None


def reverse(head: Node) -> Node:
    prev = None
    while head:
        nxt = head.next
        head.next = prev
        prev = head
        head = nxt
    return prev

def main():
    head = Node(2)
    head.next = Node(4)
    head.next.next = Node(6)
    head.next.next.next = Node(8)
    head.next.next.next.next = Node(10)
    head.next.next.next.next.next = Node(12)
    reorder(head)
    head.print_list()

main()
