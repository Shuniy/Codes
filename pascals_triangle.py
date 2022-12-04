def pascal_triangle(n):
    for line in range(1, n + 1):
        c = 1
        for i in range(1, line + 1):
            print(c, end = " ")
            c = int(c * (line - i) / i)
        print("")

print(pascal_triangle(5))