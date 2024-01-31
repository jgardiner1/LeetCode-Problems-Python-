"""
### NOT COMPLETED ###
1559. Detect Cycles in 2D Grid
Medium
Topics
Companies
Hint
Given a 2D array of characters grid of size m x n, you need to find if there exists any cycle consisting of the same value in grid.

A cycle is a path of length 4 or more in the grid that starts and ends at the same cell. From a given cell, you can move to one of the cells adjacent to it - in one of the four directions (up, down, left, or right), if it has the same value of the current cell.

Also, you cannot move to the cell that you visited in your last move. For example, the cycle (1, 1) -> (1, 2) -> (1, 1) is invalid because from (1, 2) we visited (1, 1) which was the last visited cell.

Return true if any cycle of the same value exists in grid, otherwise, return false.

 

Example 1:



Input: grid = [["a","a","a","a"],["a","b","b","a"],["a","b","b","a"],["a","a","a","a"]]
Output: true
Explanation: There are two valid cycles shown in different colors in the image below:

Example 2:



Input: grid = [["c","c","c","a"],["c","d","c","c"],["c","c","e","c"],["f","c","c","c"]]
Output: true
Explanation: There is only one valid cycle highlighted in the image below:

Example 3:



Input: grid = [["a","b","b"],["b","z","b"],["b","b","a"]]
Output: false
 

Constraints:

m == grid.length
n == grid[i].length
1 <= m, n <= 500
grid consists only of lowercase English letters.
"""


class Solution:
    def pickNewStartPos(self, grid, visited):
        for x in range(len(grid[0])):
            for y in range(len(grid)):
                if [x, y] not in visited:
                    return [x, y]

    def checkAdjacent(self, pos, targetV, grid, l, h):
        adjacent = []

        x = pos[0]
        y = pos[1]

        # right
        try:
            if y + 1 < l and grid[x][y + 1] == targetV:
                adjacent.append([x, y + 1])
            # left
            if y - 1 >= 0 and grid[x][y - 1] == targetV:
                adjacent.append([x, y - 1])
            # up
            if x - 1 >= 0 and grid[x - 1][y] == targetV:
                adjacent.append([x - 1, y])
            # down
            if x + 1 < h and grid[x + 1][y] == targetV:
                adjacent.append([x + 1, y])
        except IndexError:
            print("out of bounds")

        return adjacent

    def containsCycle(self, grid: list[list[str]]) -> bool:
        l = len(grid[0])
        h = len(grid)
        print(l, h)

        visited = []
        startPos = [0, 0]
        queue = []
        queue.append(startPos)
        targetV = grid[startPos[0]][startPos[1]]
        cycle = []

        # while we havent visited every node
        while len(visited) != l * h:
            if len(queue) == 0:
                queue.append(self.pickNewStartPos(grid, visited))
                startPos = queue[0]
                print(startPos[0], startPos[1])
                targetV = grid[startPos[0]][startPos[1]]

            while queue:
                curPos = queue.pop()
                visited.append(curPos)
                adjacent = self.checkAdjacent(curPos, targetV, grid, l, h)
                print("adjacent check: ", adjacent)

                for p in adjacent:
                    if p not in visited and p not in queue:
                        queue.append(p)
                        print("appended: ", p)

                cycle.append(curPos)

            if startPos in self.checkAdjacent(cycle[-1], targetV, grid, l, h):
                if len(cycle) < 4:
                    return False
                else:
                    return True

            cycle.clear()
            queue.clear()

        return False


grid = [["b", "a"], ["a", "a"], ["b", "b"], ["b", "a"]]
sol = Solution()
print(sol.containsCycle(grid=grid))
