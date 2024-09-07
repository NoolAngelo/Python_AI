import sys
import os
from PIL import Image, ImageDraw

class Node:
    def __init__(self, state, parent, action, heuristic=0):
        self.state = state
        self.parent = parent
        self.action = action
        self.heuristic = heuristic

    def __lt__(self, other):
        return self.heuristic < other.heuristic

# class PriorityQueueFrontier:
    def __init__(self):
        self.frontier = []

    def add(self, node):
        self.frontier.append(node)
        self.frontier.sort()

    def contains_state(self, state):
        return any(node.state == state for node in self.frontier)

    def empty(self):
        return len(self.frontier) == 0

    def remove(self):
        if self.empty():
            raise Exception("Empty frontier")
        else:
            node = self.frontier.pop(0)
            return node

class Maze:
    def __init__(self, filename):
        # Read the maze from file
        try:
            with open(filename) as f:
                contents = f.read()
        except FileNotFoundError:
            raise Exception(f"File {filename} not found")

        # Validate start and goal
        if contents.count("A") != 1:
            raise Exception("Maze must have exactly one start point")
        if contents.count("B") != 1:
            raise Exception("Maze must have exactly one goal")
        
        # Determine height and width of maze
        contents = contents.splitlines()
        self.height = len(contents)
        self.width = max(len(line) for line in contents)

        # Keep track of walls
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

        self.solution = None
        self.explored = set()

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

    def neighbors(self, state):
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

    def manhattan_distance(self, state):
        """Calculate the Manhattan distance from the current state to the goal."""
        (x1, y1) = state
        (x2, y2) = self.goal
        return abs(x1 - x2) + abs(y1 - y2)
    
    def solve(self):
        """Finds a solution to maze, if one exists."""

        self.num_explored = 0

        # Initialize frontier to just the starting position
        start = Node(state=self.start, parent=None, action=None, heuristic=self.manhattan_distance(self.start))
        frontier = PriorityQueueFrontier()
        frontier.add(start)

        # Keep looping until solution found
        while True:
            # If nothing left in frontier, then no path
            if frontier.empty():
                raise Exception("No solution")

            # Choose a node from the frontier
            node = frontier.remove()
            self.num_explored += 1

            # If node is the goal, then we have a solution
            if node.state == self.goal:
                actions = []
                cells = []

                # Follow parent nodes to find solution
                while node.parent is not None:
                    actions.append(node.action)
                    cells.append(node.state)
                    node = node.parent
                actions.reverse()
                cells.reverse()
                self.solution = (actions, cells)
                return

            # Mark node as explored
            self.explored.add(node.state)

            # Add neighbors to frontier
            for action, state in self.neighbors(node.state):
                if not frontier.contains_state(state) and state not in self.explored:
                    child = Node(state=state, parent=node, action=action, heuristic=self.manhattan_distance(state))
                    frontier.add(child)

    def output_image(self, filename, show_solution=True, show_explored=False):
        cell_size = 50
        cell_border = 2

        # Create a blank canvas
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

        # Save the image, incrementing the filename if necessary
        base, extension = os.path.splitext(filename)
        counter = 1
        new_filename = filename
        while os.path.exists(new_filename):
            new_filename = f"{base}{counter}{extension}"
            counter += 1
        img.save(new_filename)
        return new_filename

def main(filename):
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
        print(f"Using maze file: {filename}")
    
    main(filename)