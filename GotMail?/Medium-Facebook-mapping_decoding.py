"""
Medium
Good morning! Here's your coding interview problem for today.

This problem was asked by Facebook.

Given the mapping a = 1, b = 2, ... z = 26, and an encoded message, count the number of ways it can be decoded.

For example, the message '111' would give 3, since it could be decoded as 'aaa', 'ka', and 'ak'.

You can assume that the messages are decodable. For example, '001' is not allowed.
"""

# This is recursion problem where we have to use induction method using final outcome looks like
# code(1) = 1, code("") = 1
# code(11) = 2, code (111) = 3

# Therefore, tree breaks like this
# count is equal to number of codes the digits after index 0 can formed
# but what if first two digits also comes under the 26, therefore total count = count(1:) + count(2:) if count(:2) < 26
 

def is_char(code):
    return 0 if code > 26 or code < 1 else 1

def get_message_count(code):
    code = str(code)
    if len(code) <= 1:
        return 1
    if len(code) == 2:
        return 1 + is_char(int(code))
    else:
        count = get_message_count(int(code[1:]))
        if is_char(int(code[:2])):
            count += get_message_count(int(code[2:]))
    return count

assert get_message_count(81) == 1
assert get_message_count(11) == 2
assert get_message_count(111) == 3
assert get_message_count(1111) == 5
assert get_message_count(1311) == 4
