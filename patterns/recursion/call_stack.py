"""
What is a call stack?
When we use functions in our code, the computer makes use of a data structure called a call stack. As the name suggests, a call stack is a type of stack—meaning that it is a Last-In, First-Out (LIFO) data structure.

So it's a type of stack—but a stack of what, exactly?

Essentially, a call stack is a stack of frames that are used for the functions that we are calling. When we call a function, say print_integers(5), a frame is created in memory. All the variables local to the function are created in this memory frame. And as soon as this frame is created, it's pushed onto the call stack.

The frame that lies at the top of the call stack is executed first. And as soon as the function finishes executing, this frame is discarded from the call stack.
"""

"""
Problem Statement
Consider the following problem:

Given a positive integer n, write a function, print_integers, that uses recursion to print all numbers from n to 1.

For example, if n is 4, the function shuld print 4 3 2 1.

If we use iteration, the solution to the problem is simple. We can simply start at 4 and use a loop to print all numbers till 1. However, instead of using an interative approach, our goal is to solve this problem using recursion.
"""

def print_integers(n):
    if n == 1:
        print(n)
        return
    print(n)
    return print_integers(n - 1)

print_integers(5)