def partition(head, tail, new_head, new_tail):
    pivot = tail
    prev = None
    curr = head
    end = tail
    while curr != pivot:
        if curr.data < pivot.data:
            if new_head == None:
                new_head = curr
            prev = curr
            curr = curr.next
        else:
            if prev:
                prev.next = curr.next
            temp = curr.next
            curr.next = None
            end.next = curr
            end = curr
            curr = temp
    if new_head == None:
        new_head = pivot
    new_tail = end
    return pivot, new_head, new_tail


def Tail(head):
    curr = head
    while curr != None and curr.next != None:
        curr = curr.next
    return curr


def quickSortRecur(head, tail):
    if head == None or head == tail:
        return head
    new_head = None
    new_tail = None

    pivot, new_head, new_tail = partition(head, tail, new_head, new_tail)

    if new_head != pivot:
        temp = new_head
        while temp.next != pivot:
            temp = temp.next
        temp.next = None
        new_head = quickSortRecur(new_head, temp)
        temp = Tail(new_head)
        temp.next = pivot

    pivot.next = quickSortRecur(pivot.next, new_tail)
    return new_head


def quickSort(head):
    #return head after sorting
    temp = quickSortRecur(head, Tail(head))
    return temp
