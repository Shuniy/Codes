"""

Intersection:  Given two(singly) linked lists, determine if the two lists intersect. Return the inter­
secting node. Note that the intersection is defined based on reference, not value. That is, if the kth
node of the first linked list is the exact same node(by reference) as the jth node of the second
linked list, then they are intersecting.
Hints:  # 20, #45, #55, #65, #76, #93, #111, #120, #129

"""
# one way is to store the memory address in hashtable and check coinciding memory addresses
# time : O(n) : space : O(n)

# another way is to check if when traversing if the nodes have same next address then, that node is intersection
# also basic check is to check the tail if the memory address is different then no interesection
# time : O(n) : space : O(1)

def intersection(head1, head2):
    m = head1.length()
    n = head2.length()

    if not (head1 or head2):
        return False

    difference = abs(m - n)
    head1, head2 = (head1, head2) if m > n else (head2, head1)
    if difference:
        while difference:
            head1 = head1.next 
            difference -= 1
    
    # same length
    while head1 and head2:
        if head1.next == head2.next:
            return True

        head1 = head1.next 
        head2 = head2.next 

    return False


    