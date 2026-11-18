def find_happy_number(num: int):
    slow, fast = num, num
    while True:
        slow = find_square_num(slow)
        fast = find_square_num(find_square_num(fast))
        if fast == slow: # when found cycle break
            break
    return slow == 1 # check if cycle breaked at 1, so that it is happy number

def find_happy_number_set(num: int):
    s = set()
    n = num
    while True:
        n = find_square_num(n)
        if n in s:
            break
        s.add(n)
    return n == 1

def find_square_num(num):
    s = 0
    while num > 0:
        q, r = divmod(num, 10)
        num = q
        s += r ** 2
    return s

def main():
    print(find_happy_number(23))
    print(find_happy_number(12))

    print(find_happy_number_set(23))
    print(find_happy_number_set(12))

main()