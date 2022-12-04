"""
Problem Statement
Given an input string consisting of only { and }, figure out the minimum number of reversals required to make the brackets balanced.

For example:

For input_string = "}}}}, the number of reversals required is 2.
For input_string = "}{}}, the number of reversals required is 1.
If the brackets cannot be balanced, return -1 to indicate that it is not possible to balance them.
"""

class LinkedListNode:

    def __init__(self, value):
        self.value = value
        self.next = None


class Stack:

    def __init__(self):
        self.num_elements = 0
        self.head = None

    def push(self, value):
        new_node = LinkedListNode(value)
        if self.head is None:
            self.head = new_node
        else:
            new_node.next = self.head
            self.head = new_node
        self.num_elements += 1

    def pop(self):
        if self.is_empty():
            return None
        temp = self.head.value
        self.head = self.head.next
        self.num_elements -= 1
        return temp

    def top(self):
        if self.head is None:
            return None
        return self.head.value

    def size(self):
        return self.num_elements

    def is_empty(self):
        return self.num_elements == 0

def minimum_bracket_reversals(input_string):
    movements = 0
    if input_string[0] == "}":
        input_string = "{" + input_string[1:]
        movements += 1
    if input_string[len(input_string) - 1] == "{":
        input_string = input_string[:len(input_string) - 1] + "}"
        movements += 1
    prevChar = "-"

    if len(input_string) % 2 != 0:
        return -1
    else:
        stack = Stack()
        for char in input_string:
            if prevChar + char == "{}":
                _ = stack.pop()
                prevChar = stack.top()
                if stack.size() == 0:
                    prevChar = "-"
            else:
                stack.push(char)
                prevChar = char

    return int(stack.size() / 2) + movements


def test_function(test_case):
    input_string = test_case[0]
    expected_output = test_case[1]
    output = minimum_bracket_reversals(input_string)

    if output == expected_output:
        print("Pass")
    else:
        print("Fail")


test_case_1 = ["}}}}", 2]
test_function(test_case_1)

test_case_2 = ["}}{{", 2]
test_function(test_case_2)

test_case_3 = ["{{{{{{{{{{{{{{{{{{{{{{{{{{{{{{{}}}}}", 13]

test_function(test_case_1)

test_case_4 = ["}{}{}{}{}{}{}{}{}{}{}{}{}{}{}{", 2]
test_function(test_case_2)

test_case_5 = ["}}{}{}{}{}{}{}{}{}{}{}{}{}{}{}", 1]

test_function(test_case_3)
