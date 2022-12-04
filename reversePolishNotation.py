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

    def is_empty(self):
        return self.num_elements == 0

    def size(self):
        return self.num_elements

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

def evaluate_post_fix(input_list):
    stack = Stack()
    for element in input_list:
        if element in ["+", "-", "*", "/"]:
            element2 = stack.pop()
            element1 = stack.pop()
            stack.push(str(int(eval(element1 + element + element2))))
        else:
            stack.push(element)

    return stack.pop()


def test_function(test_case):
    output = evaluate_post_fix(test_case[0])
    print(output)
    if output == test_case[1]:
        print("Pass")
    else:
        print("Fail")


test_case_1 = [["3", "1", "+", "4", "*"], 16]

test_function(test_case_1)

test_case_2 = [["4", "13", "5", "/", "+"], 6]
test_function(test_case_2)

test_case_3 = [["10", "6", "9", "3", "+", "-11",
                "*", "/", "*", "17", "+", "5", "+"], 22]
test_function(test_case_3)
