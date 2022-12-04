# Maximize the heights of disk and dimensions should be smaller than the disk stacked on
# No rotation of dimensions

# [[2,2,1], [2,1,2], [3,2,3], [2,3,4], [4,4,5], [2,2,8]]
# Answer = [[2,1,2], [3,2,3], [4,4,5]]

# Time : O(n^2)
# Space : O(n)

def disk_stacking(disks):
    disks.sort(key = lambda x : x[2])
    heights = [disk[2] for disk in disks]
    sequences = [None for _ in disks]
    max_height_index = 0
    
    for i in range(1, len(disks)):
        current_disk = disks[i]

        for j in range(i):
            other_disk = disks[j]
            if are_valid_dimensions(current_disk, other_disk):
                if heights[i] < current_disk[2] + heights[j]:
                    heights[i] = current_disk[2] + heights[j]
                    sequences[i] = j
        if heights[i] >= heights[max_height_index]:
            max_height_index = i

    return build_sequence(sequences, disks, max_height_index)

def build_sequence(sequences, disks, max_height_index):
    sequence = []
    while max_height_index is not None:
        sequence.append(disks[max_height_index])
        max_height_index = sequences[max_height_index]

    return list(reversed(sequence))

def are_valid_dimensions(current_disk, other_disk):
    return other_disk[0] < current_disk[0] and other_disk[1] < current_disk[1] and other_disk[2] < current_disk[2]
