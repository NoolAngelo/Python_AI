import heapq

class Node:
    def __init__(self, x, y, cost, parent=None):
        self.x = x
        self.y = y
        self.cost = cost
        self.parent = parent

    def __lt__(self, other):
        return self.cost < other.cost

def heuristic(node, goal):
    return abs(node.x - goal.x) + abs(node.y - goal.y)

def astar(start, goal, grid):
    open_list = []
    closed_set = set()

    heapq.heappush(open_list, start)

    while open_list:
        current_node = heapq.heappop(open_list)

        if current_node == goal:
            path = []
            while current_node:
                path.append((current_node.x, current_node.y))
                current_node = current_node.parent
            return path[::-1]

        closed_set.add(current_node)

        neighbors = [(current_node.x - 1, current_node.y),
                     (current_node.x + 1, current_node.y),
                     (current_node.x, current_node.y - 1),
                     (current_node.x, current_node.y + 1)]

        for neighbor in neighbors:
            x, y = neighbor

            if x < 0 or x >= len(grid) or y < 0 or y >= len(grid[0]):
                continue

            if grid[x][y] == 1:
                continue

            neighbor_node = Node(x, y, current_node.cost + 1, current_node)

            if neighbor_node in closed_set:
                continue

            neighbor_node.cost += heuristic(neighbor_node, goal)

            heapq.heappush(open_list, neighbor_node)

    return None

# Example usage
grid = [[0, 0, 0, 0, 0],
        [0, 1, 1, 0, 0],
        [0, 0, 0, 0, 0],
        [0, 0, 1, 1, 0],
        [0, 0, 0, 0, 0]]

start = Node(0, 0, 0)
goal = Node(4, 4, 0)

path = astar(start, goal, grid)
if path:
    print("Shortest path found:", path)
else:
    print("No path found.")