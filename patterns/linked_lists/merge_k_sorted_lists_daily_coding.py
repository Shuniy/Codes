"""
You are given an array of k linked-lists lists, each linked-list is sorted in ascending order.

Merge all the linked-lists into one sorted linked-list and return it.

Example 1:

Input: lists = [[1,4,5],[1,3,4],[2,6]]
Output: [1,1,2,3,4,4,5,6]
Explanation: The linked-lists are:
[
  1->4->5,
  1->3->4,
  2->6
]
merging them into one sorted list:
1->1->2->3->4->4->5->6

Example 2:

Input: lists = []
Output: []

Example 3:

Input: lists = [[]]
Output: []


"""
# First Method is to Flatten the list and apply sort
# Time : O(KNlogKN) / Space : O(KNlogKN)

# Merge Sort applied
# Time : O(NlogK) / Space : O(N)

# Third Method is to use heap and take smallest element each time and store it into another array
# Time : O(KNlogk) / Space : O(N)

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

def merge(left, right):
    ptr = temp = ListNode(0)

    while left and right:
        if left.val < right.val:
            temp.next = left
            temp = temp.next
            left = left.next
        else:
            temp.next = right
            right = right.next 
            temp = temp.next
    if right:
        temp.next = right

    if left:
        temp.next = left

    return ptr.next

def mergeKSortedLists(lists):
    if not lists:
        return None

    if len(lists) == 1:
        return lists[0]
    
    mid = len(lists) // 2

    left = mergeKSortedLists(lists[:mid])
    right = mergeKSortedLists(lists[mid:])
    merged = merge(left, right)

    return merged

