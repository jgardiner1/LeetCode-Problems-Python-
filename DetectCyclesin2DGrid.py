def checkAdjacent(pos, targetV, grid):
    adjacent = []

    x = pos[0]
    y = pos[1]

    #right
    if y + 1 < l and grid[x][y + 1] == targetV:
        adjacent.append([x, y+1])
    #left
    if y - 1 >= 0 and grid[x][y-1] == targetV:
        adjacent.append([x, y-1])
    #up
    if x - 1 >= 0 and grid[x-1][y] == targetV:
        adjacent.append([x-1, y])
    #down
    if x + 1 < h and grid[x+1][y] == targetV:
        adjacent.append([x+1, y])
    
    return adjacent


def pickNewStartPos():
    for x in range(len(grid[0])):
        for y in range(len(grid)):
            if [x, y] not in visited:
                return [x, y]

    

grid = [["a","b","b"],["b","z","b"],["b","b","a"]]

l = len(grid[0])
h = len(grid)


# select starting point and add to queue
# while queue is not empty continue traversing
# see if any adjacent carry on cycle
# if it does add it to queue and update the current cycle and repeat
# when we run out of nodes or come across one we have already visited check if the pattern is a cylce

# if it doesnt then check we have visited every node at least once,
# if we have then there are no cycles if we havent then select new starting point
visited = []
startPos = [0, 0]
queue = []
queue.append(startPos)
targetV = grid[startPos[0]][startPos[1]]
cycle = []

# while we havent visited every node
while len(visited) != l * h:

    if len(queue) == 0:
        print("picking new start")
        queue.append(pickNewStartPos())
        startPos = queue[0]
        targetV = grid[startPos[0]][startPos[1]]
        print("new pick: ", queue)

    while queue:
        curPos = queue.pop()
        visited.append(curPos)
        print("Currently at: ", curPos)
        adjacent = checkAdjacent(curPos, targetV, grid)
        print("Adjacent to curPos: ", adjacent)

        for p in adjacent:
            if p not in visited and p not in queue:
                queue.append(p)
        
        cycle.append(curPos)
        print("Current queue is: ", queue)
        print("Current cycle is: ", cycle, "\n\n")
    
    if startPos in checkAdjacent(cycle[-1], targetV, grid):
        print("Contains cycle!")
        print(cycle)
        break

    cycle.clear()
    queue.clear()

print("no cycles found")
