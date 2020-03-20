"""
A heap is a data structure with the following two main properties:

Complete Binary Tree
Heap Order Property

Complete Binary Tree - Like the name suggests we use a binary tree to create heaps. A complete binary tree is a special type of binary tree in which all levels must be filled except for the last level. Moreover, in the last level, the elements must be filled from left to right.

Heap Order Property - Heaps come in two flavors
Min Heap
Max Heap
Min Heap - In the case of min heaps, for each node, the parent node must be smaller than both the child nodes. It's okay even if one or both of the child nodes do not exists. However if they do exist, the value of the parent node must be smaller. Also note that it does not matter if the left node is greater than the right node or vice versa. The only important condition is that the root node must be smaller than both it's child nodes
Max Heap - For max heaps, this condition is exactly reversed. For each node, the value of the parent node must be larger than both the child nodes.
Thus, for a data structure to be called a Heap, it must satisfy both of the above properties.

It must be a complete binary tree
It must satisfy the heap order property. If it's a min heap, it must satisfy the heap order property for min heaps. If it's a max heap, it should satisfy the heap order property for max heaps.

Now that we know about a complete binary, let's think about it in terms of Priority Queues. We talked about binary search trees where the complexity for insert and remove operation would be O(log(n)) if the BST is balanced.

In case of a complete binary tree we do not have to worry about whether the tree is balanced or not.

Max number of nodes in 1st level = 1
Max number of nodes in 2nd level = 2
Max number of nodes in 3rd level = 4
Max number of nodes in 4th level = 8
We see that there is a clear patter here.

Max number of nodes in hth level = $2^{(h-1)}$
Also, we can calculate the max number of nodes from 1st level to hth level = $2^h - 1$

Similarly, we can calculate the min number of nodes from 1st level to hth level =$2^{(h-1)}$

Note: the minimum number of nodes from 1st level to hth level = max number of nodes from 1st level to (h-1)th level + 1

Thus, in a complete binary tree of height h, we can be assured that the number of elements n would be between these two numbers i.e.

$$ 2^{(h-1)}  &lt;= n &lt;= 2^h - 1$$
If we write the first inequality in base-2 logarithmic format we would have
$$ \log_{2}\ (2^{(h-1)}) &lt;= \log_{2} n $$$$or$$$$ h &lt;= \log_{2} n + 1$$
Similarly, if we write the second equality in base-2 logarithmic format
$$ \log_{2} (n + 1) &lt;= \log_{2}\ 2^{h}$$$$ or $$$$ \log_{2} (n + 1) &lt;= h $$
Thus the value of our height h is always

$$ \log_{2} (n + 1) &lt;= h &lt;= \log_{2} n + 1$$
We can see that the height of our complete binary tree will always be in the order of O(h) or O(log(n))

So, if instead of using a binary search tree, we use a complete binary tree, both insert and remove operation will have the time complexity $\ \log_{2} n$

Heaps for Priority Queues
Let's take a step back and reflect on what we have done.

We have examined popular data structures and observed their time complexities.
We have looked at a new data structure called Heap
We know that Heaps have two properties -
 i. CBT 
 ii. Heap Order Property
We have looked at what CBT is and what Heap Order Property is
By now, it must have been clear to you that we are going to use Heaps to create our Priority Queues. But are you convinced that heaps are a good structure to create Priority Queues?

Ans.

Other than Binary Search trees, all other popular data structures seemed to have a time complexity of O(n) for both insertion and removal.

Binary Search Trees seemed like an effective data structure with average case time complexity of O(log(n) (or O(h)) for both the operations. However, in the worst case, a Binary Search Tree may not be balanced and instead behave like a linked list. In such a case, the time complexity in terms of height would still be O(h) but because the height of the binary search tree will be equal to the number of elements in the tree, the actual time complexity in terms of number of elements n would be O(n).

The CBT property of Heaps ensures that the tree is always balanced. Therefore, the height h of the tree will always be equal to log(n).

The Heap Order Property ensures that there is some definite structure to our Complete Binary Tree with respect to the value of the elements. In case of a min-heap, the minimum element will always lie at the root node. Similarly, in case of a maxp-heap, the maximum element will always lie at the root node. In both the cases, every time we insert or remove an element, the time complexity remains O(log(n)).

Therefore, because of the time complexity being O(log(n)), we prefer heaps over other popular data structures to create our Priority Queues.

Complete Binary Trees using Arrays
Although we call them complete binary trees, and we will always visualize them as binary trees, we never use binary trees to create them. Instead, we actually use arrays to create our complete binary trees.

An array is a contiguous blocks of memory with individual "blocks" are laid out one after the other in memory. We are used to visualizing arrays as sequential blocks of memory.

However, if we visualize them in the following way, can we find some similarities between arrays and complete binary trees?

Let's think about it.

In a complete binary tree, it is mandatory for all levels before the last level to be completely filled.
If we visualize our array in this manner, do we satisfy this property of a CBT? All we have to ensure is that we put elements in array indices sequenially i.e. the smaller index first and the larger index next. If we do that, we can be assured that all levels before the last level will be completely filled.

In a CBT, if the last level is not completely filled, the nodes must be filled from left to right.
Again, if we put elements in the array indices sequentially, from smaller index to larger index, we can be assured that if the last level is not filled, it will certainly be filled from left to right.

Thus we can use an array to create our Completer Binary Tree. Although it's an array, we will always visualize it as complete binary tree when talking about heaps.

Now let's talk about insert and remove operation in a heap. We will create our heap class which with these two operations. We also add a few utility methods for our convenience. Finally, because we know we are going to use arrays to create our heaps, we will also initialize an array.

Note that we are creating min heaps for now. The max heap will follow the exact some process. The only difference arises in the Heap Order Property.

As always we will use Python lists like C-style arrays to make the implementation as language agnostic as possible.

"""

class Heap:
    def __init__(self, initial_size):
        self.cbt = [None for _ in range(initial_size)]
        self.next_index = 0

    def _parent_index(self, children_index):
        return (children_index - 1) // 2

    def _parent_value(self, children_index):
        return self.cbt[self._parent_index(children_index)]

    def _children_index(self, parent_index):
        return (2 * parent_index) + 1, (2 * parent_index) + 2

    def _children_value(self, parent_index):
        index_children_1, index_children_2 = self._children_index(parent_index)
        return self.cbt[index_children_1], self.cbt[index_children_2]

    def up_heapify(self, index):
        if index == 0:
            return

        index_parent = self._parent_index(children_index=index)
        value_parent = self._parent_value(children_index=index)
        value_children = self.cbt[index]

        if value_parent > value_children:
            self.cbt[index] = value_parent
            self.cbt[index_parent] = value_children

            self.up_heapify(index_parent)
        else:
            pass

    def size(self):
        return self.next_index

    def insert(self, data):
        if self.next_index < len(self.cbt) - 1:
            self.cbt[self.next_index] = data
            self.up_heapify(self.next_index)
            self.next_index += 1
        else:
            pass

    def is_empty(self):
        return self.size() == 0

    def _down_heapify(self):
        parent_index = 0

        while parent_index < self.next_index:
            left_child_index = 2 * parent_index + 1
            right_child_index = 2 * parent_index + 2
            parent = self.cbt[parent_index]
            left_child = None
            right_child = None
            min_element = parent

            if left_child_index < self.next_index:
                left_child = self.cbt[left_child_index]

            if right_child_index < self.next_index:
                right_child = self.cbt[right_child_index]

            if left_child is not None:
                min_element = min(parent, left_child)

            if right_child is not None:
                min_element = min(parent, right_child)

            if min_element == parent:
                return
            if min_element == left_child:
                self.cbt[left_child_index] = parent
                self.cbt[parent_index] = min_element
                parent = left_child_index
            elif min_element == right_child:
                self.cbt[right_child_index] = parent
                self.cbt[parent_index] = min_element
                parent = right_child_index

    def get_minimum(self):
        # Returns the minimum element present in the heap
        if self.size() == 0:
            return None
        return self.cbt[0]

    def remove(self):
        if self.size() == 0:
            return None
        self.next_index -= 1

        to_remove = self.cbt[0]
        last_element = self.cbt[self.next_index]
        self.cbt[0] = last_element
        self.cbt[self.next_index] = to_remove
        self._down_heapify()
        return to_remove

"""
For min-heaps, we remove the smallest element from our heaps. For max-heaps, we remove the largest element from the heap.

Time Complexity
Can you determine the time complexity for remove using the same process that we followed for insert?

Ans: the time complexity for remove is also O(log(n))
"""
heap_size = 5
heap = Heap(heap_size)

elements = [1, 2, 3, 4, 1, 2]
for element in elements:
    heap.insert(element)
print('Inserted elements: {}'.format(elements))

print('size of heap: {}'.format(heap.size()))

for _ in range(4):
    print('Call remove: {}'.format(heap.remove()))

print('Call get_minimum: {}'.format(heap.get_minimum()))

for _ in range(2):
    print('Call remove: {}'.format(heap.remove()))

print('size of heap: {}'.format(heap.size()))
print('Call remove: {}'.format(heap.remove()))
print('Call is_empty: {}'.format(heap.is_empty()))
