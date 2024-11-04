import sys
import os
from PIL import Image, ImageDraw
from typing import List, Tuple, Optional

class Node:
    def __init__(self, state: Tuple[int, int], parent: Optional['Node'], action: Optional[str], heuristic: int = 0):
        self.state = state
        self.parent = parent
        self.action = action
        self.heuristic = heuristic

    def __lt__(self, other: 'Node'):
        return self.heuristic < other.heuristic

class PriorityQueueFrontier:
    def __init__(self):
        self.frontier: List[Node] = []

    def add(self, node: Node):
        self.frontier.append(node)
        self.frontier.sort()

    def contains_state(self, state: Tuple[int, int]) -> bool:
        return any(node.state == state for node in self.frontier)

    def empty(self) -> bool:
        return len(self.frontier) == 0

    def remove(self) -> Node:
        if self.empty():
            raise Exception("Empty frontier")
        else:
            return self.frontier.pop(0)

class Maze:
    def __init__(self, filename: str):
        self._load_maze(filename)
        self.solution = None
        self.explored = set()

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
        self.num_explored = 0
        start = Node(state=self.start, parent=None, action=None, heuristic=self.manhattan_distance(self.start))
        frontier = PriorityQueueFrontier()
        frontier.add(start)

        while True:
            if frontier.empty():
                raise Exception("No solution")

            node = frontier.remove()
            self.num_explored += 1

            if node.state == self.goal:
                actions = []
                cells = []

                while node.parent is not None:
                    actions.append(node.action)
                    cells.append(node.state)
                    node = node.parent
                actions.reverse()
                cells.reverse()
                self.solution = (actions, cells)
                return

            self.explored.add(node.state)

            for action, state in self.neighbors(node.state):
                if not frontier.contains_state(state) and state not in self.explored:
                    child = Node(state=state, parent=node, action=action, heuristic=self.manhattan_distance(state))
                    frontier.add(child)

    def output_image(self, filename: str, show_solution: bool = True, show_explored: bool = False) -> str:
        cell_size = 50
        cell_border = 2

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
                    fill = (40, 40, 40)
                elif (i, j) == self.start:
                    fill = (255, 0, 0)
                elif (i, j) == self.goal:
                    fill = (0, 171, 28)
                elif solution is not None and show_solution and (i, j) in solution:
                    fill = (220, 235, 113)
                elif solution is not None and show_explored and (i, j) in self.explored:
                    fill = (212, 97, 85)
                else:
                    fill = (237, 240, 252)

                draw.rectangle(
                    ([(j * cell_size + cell_border, i * cell_size + cell_border),
                      ((j + 1) * cell_size - cell_border, (i + 1) * cell_size - cell_border)]),
                    fill=fill
                )

        base, extension = os.path.splitext(filename)
        counter = 1
        new_filename = filename
        while os.path.exists(new_filename):
            new_filename = f"{base}{counter}{extension}"
            counter += 1
        img.save(new_filename)
        return new_filename

def main(filename: str):
    try:
        m = Maze(filename)
    except Exception as e:
        sys.exit(str(e))

    print("Maze:")
    m.print()
    print("Solving...")
    try:
        m.solve()
    except Exception as e:
        sys.exit(str(e))

    print("States Explored:", m.num_explored)
    print("Solution:")
    m.print()
    output_filename = m.output_image("maze_solution.png", show_solution=True)
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

if __name__ == "__main__":
    print("GGs")