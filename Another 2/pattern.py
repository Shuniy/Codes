"""
Print Swastik pattern
"""
# According to pattern there are 3 special cases and two common cases.
# Special cases differs according to number.

def swastik_pattern(n):
    # Block 1 print * then (n - 3)/2 spaces then (n + 1)/2 *
    print('*', end = ' ')
    for _ in range((n - 3)//2):
        print(" ", end=' ')

    for _ in range((n + 1)//2):
        print("*", end=' ')

    print('', end = "\n")

    # Block 2
    for _ in range((n-3)//2):
        print("*", end=' ')
        for _ in range((n-3)//2):
            print(" ", end = ' ')
        print("*", end=' ')
        for _ in range((n + 1)//2):
            print(" ", end=' ')
        print("", end='\n')

    # Block 3
    for _ in range(n):
        print("*", end=' ')

    print()

    # Block 4
    for _ in range((n-3)//2):
        for _ in range((n-3)//2 + 1):
            print(" ", end = ' ')
        print("*", end=' ')
        for _ in range((n-3)//2):
            print(" ", end=' ')
        print("* ", end=' ')
        print("", end = '\n')

    # Block 5
    print('*', end=' ')
    for _ in range((n - 3)//2 + 1):
        print("*", end=' ')

    for _ in range((n - 3)//2):
        print(" ", end=' ')
    print("*")


# Test
swastik_pattern(7)
