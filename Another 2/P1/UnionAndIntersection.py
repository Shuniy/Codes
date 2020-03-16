"""
Union and Intersection of Two Linked Lists
Your task for this problem is to fill out the union and intersection functions. The union of two sets A and B is the set of elements which are in A, in B, or in both A and B. The intersection of two sets A and B, denoted by A ∩ B, is the set of all objects that are members of both the sets A and B.

You will take in two linked lists and return a linked list that is composed of either the union or intersection, respectively. Once you have completed the problem you will create your own test cases and perform your own run time analysis on the code.

For the union and intersection problem, the approach has been to transform the linked lists, a format which is harder to work with, on something much simpler as is a list. Once the transformation has been done, the combination with the handy object sets, has done all the work.

Time and Space complexity
In the study of the time complexity, we find that the transformation from linked list to list, takes O(n) time complexity, the the set function is in the same or less order of magnitude, as for the variations:

Union: we find the creation of the final array, again O(n), making n*O(n) be resulting to O(n)
Intersection: we find the creation of the final array, which is a double for-loop (operation x in s, acts with O(n)), resulting finally in O(n^n)
In respect to the space time complexity, we generate for both functions, 3 auxiliary lists, being O(3n); and resulting in O(n).
"""

