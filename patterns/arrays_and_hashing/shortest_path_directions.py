def shortestPath(directions):
    directions = directions.lower()
    path = ""
    x = 0
    y = 0

    for item in directions:
        if item == "s":
            y -= 1
        elif item == "w":
            x -= 1
        elif item == "n":
            y += 1
        elif item == "e":
            x += 1

    if x >= 0:
        while x:
            path += 'e'
            x -= 1

    if y >= 0:
        while y:
            path += 'n'
            y -= 1

    if x < 0:
        while x < 0:
            path += 'w'
            x += 1

    if y < 0:
        while y < 0:
            path += 's'
            y += 1

    return path


directions = "snnnewe"
print("Shortest Path : ", shortestPath(directions))
