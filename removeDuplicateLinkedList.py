"""
Remove Dups! Write code to remove duplicates from an unsorted linked list.
FOLLOW UP
How would you solve this problem if a temporary buffer is not allowed?
Hints:  # 9, #40

"""
# time : O(n) | space : O(n)
# create a hashset
def removeDuplicates(head):
    prev = None
    temp = head
    setValues = set()
    while temp:
        if temp.value in setValues:
            prev.next = temp.next
        else:
            setValues.add(temp.value)
            prev = temp

        temp = temp.next
    return 

# Another way is to use two loops that will save space but complexity will be O(n**2)
def removeDuplicates(head):
    slow = head
    fast = slow

    while slow:
        while fast:
            if slow.value == fast.next.value:
                fast.next = fast.next.next
            else:
                fast = fast.next
        slow = slow.next

print(removeDuplicates(head))