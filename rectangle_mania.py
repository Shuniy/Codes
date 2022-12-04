# Three Approaches
# Worst Cases
# First : Time : O(n^2) / Space : O(n^2)
# Second : Time : O(n^2) / Space : O(n)
# Third : Time : O(n^2) / Space : Same as Second O(n) but will be cleaner

# First Approach
up = "up"
right = "right"
left = "left"
down = "down"

def rectangle_mania(coords):
    coords_table = get_coords_table(coords)
    return get_rectangle_count(coords, coords_table)

def get_rectangle_count(coords, coords_table):
    rectangle_count = 0
    for coord in coords:
        rectangle_count += clockwise_count_rectangles(coord, coords_table, up, coord)

    return rectangle_count

def clockwise_count_rectangles(coord, coords_table, direction, origin):
    coord_string = coord_to_string(coord)
    if direction == left:
        rectangle_found = origin in coords_table[coord_string][left]
        return 1 if rectangle_found else 0
    else:
        rectangle_count = 0
        next_direction = get_next_clockwise_direction(direction)
        for next_coord in coords_table[coord_string][direction]:
            rectangle_count += clockwise_count_rectangles(next_coord, coords_table, next_direction, origin)

        return rectangle_count


def get_next_clockwise_direction(direction):
    if direction == up:
        return right
    if direction == right:
        return down
    if direction == down:
        return left
    return ""

def get_coords_table(coords):
    coords_table = {}

    for coord1 in coords:
        coord1d_directions = {
            up : [],
            right : [],
            down : [],
            left : []
        }
        for coord2 in coords:
            coord2d_direction = get_coords_direction(coord1, coord2)
            if coord2d_direction in coord1d_directions:
                coord1d_directions[coord2d_direction].append(coord2)
            
        coord1_string = coord_to_string(coord1)
        coords_table[coord1_string] = coord1d_directions
    return coords_table    

def get_coords_direction(coord1, coord2):
    x1, y1 = coord1
    x2, y2 = coord2

    if y2 == y1:
        if x2 > x1:
            return right
        elif x2 < x1:
            return left
    elif x2 == x1:
        if y2 > y1:
            return up
        elif y2 < y1:
            return down
    else:
        return ""

def coord_to_string(coord):
    x, y = coord
    return str(x) + "-" + str(y)


# Second Approach
# Basically indexing values according to x and y coordinates 
# and not storing the coordinates possible

def rectangle_mania(coords):
    coords_table = get_coords_table(coords)
    return get_rectangle_count(coords, coords_table)

def get_rectangle_count(coords, coords_table):
    rectangle_count = 0

    for coord in coords:
        lower_left_y = coord[1]
        rectangle_count += clockwise_count_rectangles(coord, coords_table, up, lower_left_y)
    return rectangle_count

def clockwise_count_rectangles(coord1, coords_table, direction, lower_left_y):
    x1, y1 = coord1
    if direction == down:
        relevant_coords = coords_table['x'][x1]
        for coord2 in relevant_coords:
            lower_right_y = coord2[1]
            if lower_right_y == lower_left_y:
                return 1
        return 0
    else:
        rectangle_count = 0
        if direction == up:
            relevant_coords = coords_table['x'][x1]
            for coord2 in relevant_coords:
                y2 = coord2
                is_above = y2 > y1
                if is_above:
                    rectangle_count += clockwise_count_rectangles(coord2, coords_table, right, lower_left_y)
        elif direction == right:
            relevant_coords = coords_table['y'][y1]
            for coord2 in relevant_coords:
                x2 = coord2[1]
                is_right = x2 > x1

                if is_right:
                    rectangle_count += clockwise_count_rectangles(coord2, coords_table, down, lower_left_y)

        return rectangle_count


def get_coords_table(coords):
    coords_table = {
        "x" : {},
        "y" : {}
    }

    for coord in coords:
        x, y = coord
        
        if x not in coords_table["x"]:
            coords_table['x'][x] = []
        coords_table['x'][x].append(coord)
        
        if y not in coords_table["y"]:
            coords_table['y'][y] = []
        coords_table['y'][y].append(coord)

    return coords_table


# Third Approach
# Will store list of x coordinates and list of y coordinates

def rectangle_mania(coords):
    coords_table = get_coords_table(coords)
    return get_rectangle_count(coords, coords_table)

def get_coords_table(coords):
    coords_table = {}
    for coord in coords:
        coord_string = coord_to_string(coord)
        coords_table[coord_string] = True
    return coords_table

def get_rectangle_count(coords, coords_table):
    rectangle_count = 0
    for x1, y1 in coords:
        for x2, y2 in coords:
            if not is_upper_right():
                continue
            upper_coord_string = coord_to_string([x1, y2])
            right_coord_String = coord_to_string([x2, y1])
            if upper_coord_string in coords_table and right_coord_String in coords_table:
                rectangle_count += 1
    return rectangle_count

def is_upper_right(coord1, coord2):
    x1, y1 = coord1
    x2, y2 = coord2
    return x2 > x1 and y2 > y1
