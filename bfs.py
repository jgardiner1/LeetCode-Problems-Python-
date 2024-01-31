graph = {"5": ["3", "7"], "3": ["2", "4"], "7": ["8"], "2": [], "4": ["8"], "8": []}
graph2 = {
    "1": ["2"],
    "2": ["4", "5"],
    "3": ["8"],
    "4": ["8", "11"],
    "5": ["1"],
    "6": [],
    "7": [],
    "8": [],
    "11": [],
}

visited = []  # List for visited nodes.
queue = []  # Initialize a queue


def bfs(visited, graph, node):
    visited.append(node)
    queue.append(node)

    # while queue is not empty
    while queue:
        # get the next node
        curNode = queue.pop(0)
        print(curNode, end=" ")

        for neighbour in graph[curNode]:
            if neighbour not in visited:
                visited.append(neighbour)
                queue.append(neighbour)


bfs(visited, graph2, "5")
