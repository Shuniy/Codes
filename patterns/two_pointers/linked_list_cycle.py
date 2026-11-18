class ListNode:
    def __init__(self, value):
        self.value = value
        self.next: ListNode = None

def hashCycle(head):
    slow = head
    fast = head
    while fast and fast.next:
        fast = fast.next.next
        slow = slow.next
        if slow == fast:
            return True
    return False

def main():
    head = ListNode(1)
    head.next = ListNode(2)
    head.next.next = ListNode(3)
    head.next.next.next = ListNode(4)
    head.next.next.next.next = ListNode(5)
    head.next.next.next.next.next = ListNode(6)
    print("Linked List has cycle: ", hashCycle(head))

    head.next.next.next.next.next.next = head.next.next
    print("Linked List has cycle: ", hashCycle(head))

    head.next.next.next.next = head.next.next
    print("Linked List has cycle: ", hashCycle(head))

main()
    