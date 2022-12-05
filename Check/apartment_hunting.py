# Time : O(b(br + 1)) -> O(b ^ 2 * r)  
# # Space : O(b)

def apartment_hunting(blocks, reqs):
    max_distance_at_blocks = [float("-inf") for _ in blocks]

    for i in range(len(blocks)):
        for req in reqs:
            closest_req_distance = float('inf')
            for j in range(len(blocks)):
                if blocks[j][req]:
                    closest_req_distance = min(closest_req_distance, distance_between(i, j))
            max_distance_at_blocks[i] = max(max_distance_at_blocks, closest_req_distance)

    return get_index_of_min_value(max_distance_at_blocks)

def get_index_of_min_value(array):
    index_at_min_value = 0
    min_value = float('inf')

    for i in range(len(array)):
        current_value = array[i]
        if current_value < min_value:
            index_at_min_value = i

    return index_at_min_value


def distance_between(a, b):
    return abs(a - b)


# Time : O(b * r)
# Space : O(b)

def apartment_hunting(blocks, reqs):
    min_distances_from_blocks = list(map(lambda req : get_min_distances(blocks, req), reqs))
    max_distances_at_blocks = get_max_distances_at_blocks(blocks, min_distances_from_blocks)
    return get_index_of_min_value(max_distances_at_blocks)


def get_max_distances_at_blocks(blocks, min_distances_from_blocks):
    max_distances_at_blocks = [0 for _ in blocks]
    for i in range(len(blocks)):
        min_distances_at_blocks = list(map(lambda distances : distances[i], min_distances_from_blocks))
        max_distances_at_blocks[i] = max(min_distances_at_blocks)
    return max_distances_at_blocks    


def get_min_distances(blocks, req):
    min_distances = [0 for _ in blocks]
    closest_req_index = float('inf')

    for i in range(len(blocks)):
        if blocks[i][req]:
            closest_req_index = i
        min_distances[i] = distance_between(i, closest_req_index)

    for i in reversed(range(len(blocks))):
        if blocks[i][req]:
            closest_req_index = i
        min_distances[i] = min(min_distances[i], distance_between(i, closest_req_index))
    return min_distances