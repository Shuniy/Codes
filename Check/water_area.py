# Time : O(n)
# Space : O(n)

def water_area(heights):
    maxes = [0 for x in heights]

    leftmax = 0
    for i in range(len(heights)):
        height = heights[i]
        maxes[i] = leftmax
        leftmax = max(leftmax, height)

    rightmax = 0
    for i in reversed(range(len(heights))):
        height = heights[i]
        minimum_height = min(rightmax, maxes[i])

        if height < minimum_height:
            maxes[i] = minimum_height - height

        else:
            maxes[i] = 0

        rightmax = max(rightmax, height)

    return sum(maxes)
