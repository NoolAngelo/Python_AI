import sys
import os
import heapq
from PIL import Image, ImageDraw
from typing import List, Tuple, Optional, Dict

class Node:
    """A node in the search tree."""
    def __init__(self, state: Tuple[int, int], parent: Optional['Node'], action: Optional[str], cost: int = 0, heuristic: int = 0):
        self.state = state
        self.parent = parent
        self.action = action
        self.cost = cost
        self.heuristic = heuristic
        self.total_cost = cost + heuristic

    def __lt__(self, other: 'Node'):
        return self.total_cost < other.total_cost

class PriorityQueueFrontier:
    """A priority queue frontier implementation using heapq."""
    def __init__(self):
        self._frontier: List[Node] = []
        self._states: Dict[Tuple[int, int], float] = {}

    def add(self, node: Node):
        state = node.state
        if state not in self._states or node.total_cost < self._states[state]:
            heapq.heappush(self._frontier, node)
            self._states[state] = node.total_cost

    def contains_state(self, state: Tuple[int, int]) -> bool:
        return state in self._states

    def empty(self) -> bool:
        return len(self._frontier) == 0

    def remove(self) -> Node:
        if self.empty():
            raise Exception("Empty frontier")
        node = heapq.heappop(self._frontier)
        self._states.pop(node.state)
        return node

class Maze:
    """Maze solver using A* search algorithm."""
    def __init__(self, filename: str):
        self._load_maze(filename)
        self.solution = None
        self.explored = set()
        self.colors = {
            'wall': (40, 40, 40),
            'start': (255, 0, 0),
            'goal': (0, 171, 28),
            'path': (220, 235, 113),
            'explored': (212, 97, 85),
            'empty': (237, 240, 252)
        }

    def _load_maze(self, filename: str):
        try:
            with open(filename) as f:
                contents = f.read()
        except FileNotFoundError:
            raise Exception(f"File {filename} not found")

        if contents.count("A") != 1:
            raise Exception("Maze must have exactly one start point")
        if contents.count("B") != 1:
            raise Exception("Maze must have exactly one goal")

        contents = contents.splitlines()
        self.height = len(contents)
        self.width = max(len(line) for line in contents)

        self.walls = []
        for i in range(self.height):
            row = []
            for j in range(self.width):
                try:
                    if contents[i][j] == "A":
                        self.start = (i, j)
                        row.append(False)
                    elif contents[i][j] == "B":
                        self.goal = (i, j)
                        row.append(False)
                    elif contents[i][j] == " ":
                        row.append(False)
                    else:
                        row.append(True)
                except IndexError:
                    row.append(False)
            self.walls.append(row)

    def print(self):
        solution = self.solution[1] if self.solution is not None else None
        print()
        for i, row in enumerate(self.walls):
            for j, col in enumerate(row):
                if col:
                    print("█", end="")
                elif (i, j) == self.start:
                    print("A", end="")
                elif (i, j) == self.goal:
                    print("B", end="")
                elif solution is not None and (i, j) in solution:
                    print("*", end="")
                else:
                    print(" ", end="")
            print()
        print()

    def neighbors(self, state: Tuple[int, int]) -> List[Tuple[str, Tuple[int, int]]]:
        row, col = state
        candidates = [
            ("up", (row - 1, col)),
            ("down", (row + 1, col)),
            ("left", (row, col - 1)),
            ("right", (row, col + 1))
        ]

        result = []
        for action, (r, c) in candidates:
            if 0 <= r < self.height and 0 <= c < self.width and not self.walls[r][c]:
                result.append((action, (r, c)))
        return result

    def manhattan_distance(self, state: Tuple[int, int]) -> int:
        (x1, y1) = state
        (x2, y2) = self.goal
        return abs(x1 - x2) + abs(y1 - y2)
    
    def solve(self):
        """Solve the maze using A* search with Manhattan distance heuristic."""
        self.num_explored = 0
        start = Node(
            state=self.start,
            parent=None,
            action=None,
            cost=0,
            heuristic=self.manhattan_distance(self.start)
        )
        frontier = PriorityQueueFrontier()
        frontier.add(start)

        while True:
            if frontier.empty():
                raise Exception("No solution exists")

            node = frontier.remove()
            self.num_explored += 1

            if node.state == self.goal:
                return self._reconstruct_path(node)

            self.explored.add(node.state)

            for action, state in self.neighbors(node.state):
                if not frontier.contains_state(state) and state not in self.explored:
                    child = Node(
                        state=state,
                        parent=node,
                        action=action,
                        cost=node.cost + 1,
                        heuristic=self.manhattan_distance(state)
                    )
                    frontier.add(child)

    def _reconstruct_path(self, node: Node):
        """Reconstruct the path from start to goal."""
        actions = []
        cells = []
        while node.parent is not None:
            actions.append(node.action)
            cells.append(node.state)
            node = node.parent
        actions.reverse()
        cells.reverse()
        self.solution = (actions, cells)

    def output_image(self, filename: str, show_solution: bool = True, show_explored: bool = False, 
                    cell_size: int = 50, cell_border: int = 2) -> str:
        """Generate an image of the maze with optional solution path."""
        img = Image.new(
            "RGBA",
            (self.width * cell_size, self.height * cell_size),
            "black"
        )
        draw = ImageDraw.Draw(img)

        solution = self.solution[1] if self.solution is not None else None
        for i, row in enumerate(self.walls):
            for j, col in enumerate(row):
                if col:
                    fill = self.colors['wall']
                elif (i, j) == self.start:
                    fill = self.colors['start']
                elif (i, j) == self.goal:
                    fill = self.colors['goal']
                elif solution is not None and show_solution and (i, j) in solution:
                    fill = self.colors['path']
                elif solution is not None and show_explored and (i, j) in self.explored:
                    fill = self.colors['explored']
                else:
                    fill = self.colors['empty']

                draw.rectangle(
                    ([(j * cell_size + cell_border, i * cell_size + cell_border),
                      ((j + 1) * cell_size - cell_border, (i + 1) * cell_size - cell_border)]),
                    fill=fill
                )

        return self._save_image(filename, img)

    def _save_image(self, filename: str, img: Image.Image) -> str:
        """Save the image with an incremental filename if file exists."""
        base, extension = os.path.splitext(filename)
        counter = 1
        new_filename = filename
        while os.path.exists(new_filename):
            new_filename = f"{base}{counter}{extension}"
            counter += 1
        img.save(new_filename)
        return new_filename

def main(filename: str):
    """Main function to solve and visualize the maze."""
    try:
        m = Maze(filename)
    except Exception as e:
        sys.exit(f"Error loading maze: {str(e)}")

    print("Maze:")
    m.print()
    print("Solving...")
    
    try:
        m.solve()
    except Exception as e:
        sys.exit(f"Error solving maze: {str(e)}")

    print("States Explored:", m.num_explored)
    print("Solution:")
    m.print()
    
    output_filename = m.output_image("maze_solution.png", show_solution=True, show_explored=True)
    print(f"Solution saved as '{output_filename}'")

    if m.solution:
        print(f"Steps to solution: {len(m.solution[0])}")
        print(f"Path: {' -> '.join(m.solution[0])}")

if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("No maze file provided as argument.")
        filename = input("Please enter the maze filename: ")
    else:
        filename = sys.argv[1]
    
    main(filename)