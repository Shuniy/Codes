class Solution:
    def furthestBuilding(self, heights: list[int], bricks: int, ladders: int) -> int:
        return self.furthestBuildingHelper(heights, 0, bricks, ladders)

    def furthestBuildingHelper(self, heights, index, bricks, ladders) -> int:
        if index >= len(heights):
            return 0

        if bricks <= 0 and ladders <= 0 and heights[index + 1] > heights[index]:
            return 0

        if heights[index + 1] <= heights[index]:
            return 1 + self.furthestBuildingHelper(heights, index + 1, bricks, ladders)
        else:
            output1 = 0
            output2 = 0
            # Using Bricks
            if heights[index + 1] - heights[index] <= bricks:
                output1 = 1 + \
                    self.furthestBuilding(heights, index + 1, bricks, ladders)
            # Using ladders
            if ladders > 0:
                output2 = 1 + \
                    self.furthestBuilding(heights, index + 1, bricks, ladders)
            return max(output1, output2)


class Solution:
    def furthestBuilding(self, heights: list[int], bricks: int, ladders: int) -> int:
        return self.furthestBuildingHelper(heights, bricks, ladders, 0)

    def furthestBuildingHelper(self, heights, bricks, ladders, i) -> int:
        if(i >= len(heights) - 1):
            return i
        if(heights[i+1] > heights[i] and (ladders == 0 and bricks < (heights[i+1] - heights[i]))):
            return i

        if(heights[i+1] < heights[i]):
            return self.furthestBuildingHelper(heights, bricks, ladders, i + 1)

        if(ladders > 0):
            index1 = self.furthestBuildingHelper(
                heights, bricks, ladders - 1, i + 1)

        if(bricks > (heights[i+1] - heights[i])):
            index2 = self.furthestBuildingHelper(
                heights, bricks - (heights[i+1] - heights[i]), ladders, i + 1)

        return max(index1, index2)
