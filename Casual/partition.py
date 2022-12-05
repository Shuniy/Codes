"""
Partition: Write code to partition a linked list around a value x, such that all nodes less than x come 
before all nodes greater than or equal to x. If x i s contained within the list the values of x only need 
to be after the elements less than x (see below). The partition element x can appear anywhere in the 
"right partition"; it does not need to appear between the left and right partitions. 
EXAMPLE 
Input:  3  ->  5  ->  8  ->  5  ->  10  ->  2  ->  1 [partition= 5] 
Output:  3  ->  1  ->  2  ->  10  ->  5  ->  5  ->  8
"""

# Way is to create two lists and then add element to the list which are greater or smaller respectively

def partition(head, partitionValue):
    head = LinkedList()
    tail = LinkedList()
    maxNode = None
    prevMaxNode = None
    temp = head
    while temp:
        if temp.value < partitionValue:
            head.insert(temp.value)
        else:
            prevMaxNode = maxNode
            maxNode = temp if temp.value >= partitionValue else maxNode

            if prevMaxNode:
                tail.insert(prevMaxNode)

        temp = temp.next

    tail.insert(maxNode)
    head.next = tail
    tail = None
    return  head
