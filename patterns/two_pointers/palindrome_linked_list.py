class Node:
    def __init__(self, value, next = None):
        self.value = value
        self.next: Node = next

def reverseLinkedList(head: Node) -> Node:
    prev = None
    while head:
        nxt = head.next
        head.next = prev
        prev = head
        head = nxt
    return prev

def is_palindromic_linked_list(head: Node):
    if head is None or head.next is None:
        return True
    
    slow, fast = head, head
    while fast and fast.next:
        slow = slow.next
        fast = fast.next.next

    head_second_half = reverseLinkedList(slow)
    copy_head_second_half = head_second_half

    while head and head_second_half:
        if head.value != head_second_half.value:
            break

        head = head.next
        head_second_half = head_second_half.next
    
    reverseLinkedList(copy_head_second_half)

    if head is None or head_second_half is None:
        return True
    
    return False

def main():
    head = Node(2)
    head.next = Node(4)
    head.next.next = Node(6)
    head.next.next.next = Node(4)
    head.next.next.next.next = Node(2)

    print("Is palindrome: ", is_palindromic_linked_list(head))

    head.next.next.next.next.next = Node(2)
    print("Is palindrome: ", is_palindromic_linked_list(head))

main()