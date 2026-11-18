def towerOfHanoi(n: int):
    """
    Prints the sequence of moves to solve the Tower of Hanoi problem
    for n disks. The tower of Hanoi problem is a mathematical puzzle
    where we have three rods and n disks. The objective of the puzzle
    is to move the entire stack to another rod, obeying the following
    simple rules:
    1) Only one disk can be moved at a time.
    2) Each move consists of taking the upper disk from one of the
       stacks and placing it on top of another stack or on an empty rod.
    3) No disk may be placed on top of a smaller disk.
    """
    src = 0
    aux = 1
    dest = 2

    stack = [[] for i in range(3)]
    rod = ['S', 'A', 'D']
    
    for i in range(n, 0, -1):
        stack[src].append(i)

    total_moves = 2**n - 1 # 1 << n - 1

    if n % 2 == 0:
        aux, dest = dest, aux
        
    def move(src, dest):
        """
        Move a disk from a source rod to a destination rod.
        :param src: Source rod
        :param dest: Destination rod
        """
        if len(stack[dest]) == 0 or (stack[src] and stack[src][-1] < stack[dest][-1]):
            print("Move disk", stack[src][-1], "from", rod[src], "to", rod[dest])
            stack[dest].append(stack[src][-1])
            stack[src].pop()
        else:
            move(dest, src)

    for i in range(1, total_moves + 1):
        if i % 3 == 1:
            # src to dest
            move(src, dest)
        elif i % 3 == 2:
            # src to aux
            move(src, aux)
        elif i % 3 == 0:
            # aux to dest
            move(aux, dest)

N = 3
# number of disks
towerOfHanoi(N)
