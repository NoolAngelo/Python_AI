"""
Maze solver module that implements search algorithms to find paths in mazes.

This module contains the implementation of a maze solver using different search
strategies including depth-first search (DFS) via StackFrontier and
breadth-first search (BFS) via QueueFrontier.
"""

import sys
from typing import List, Tuple, Optional, Set, Dict, Any
from PIL import Image, ImageDraw


class Node:
    """
    A node in the search tree.

    Attributes:
        state: The current position in the maze
        parent: The parent node that led to this node
        action: The action taken to get from the parent to this node
        cost: The cost of the path to this node
    """

    def __init__(
        self,
        state: Tuple[int, int],
        parent: Optional["Node"],
        action: Optional[str],
        cost: int = 0,
    ) -> None:
        self.state = state
        self.parent = parent
        self.action = action
        self.cost = cost


class StackFrontier:
    """
    A frontier implemented as a stack for depth-first search.
    """

    def __init__(self) -> None:
        self.frontier: List[Node] = []

    def add(self, node: Node) -> None:
        """Add a node to the frontier."""
        self.frontier.append(node)

    def contains_state(self, state: Tuple[int, int]) -> bool:
        """Check if the frontier contains a specific state."""
        return any(node.state == state for node in self.frontier)

    def empty(self) -> bool:
        """Check if the frontier is empty."""
        return len(self.frontier) == 0

    def remove(self) -> Node:
        """Remove and return a node from the frontier (last in, first out)."""
        if self.empty():
            raise Exception("Empty frontier")
        else:
            node = self.frontier.pop()
            return node


class QueueFrontier(StackFrontier):
    """
    A frontier implemented as a queue for breadth-first search.
    """

    def remove(self) -> Node:
        """Remove and return a node from the frontier (first in, first out)."""
        if self.empty():
            raise Exception("Empty frontier")
        else:
            node = self.frontier.pop(0)
            return node


class Maze:
    """
    A class representing a maze and implementing search algorithms.

    Attributes:
        height: The height of the maze
        width: The width of the maze
        walls: A set of wall positions
        start: The starting position
        goal: The goal position
        solution: The solution path
        explored: The explored positions during search
    """

    def __init__(self, filename: str) -> None:
        """
        Initialize the maze from a file.

        Args:
            filename: Path to the file containing maze definition

        Raises:
            Exception: If the file is not found or the maze is invalid
        """
        # Read the maze from a file
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
        self.walls: Set[Tuple[int, int]] = set()
        for i in range(self.height):
            row = contents[i]
            for j in range(len(row)):
                if row[j] == "A":
                    self.start = (i, j)
                elif row[j] == "B":
                    self.goal = (i, j)
                elif row[j] == " " or row[j] == ".":
                    pass
                else:
                    self.walls.add((i, j))

        self.solution: Optional[List[Tuple[int, int]]] = None
        self.explored: Set[Tuple[int, int]] = set()

    def print(self) -> None:
        """Print a textual representation of the maze."""
        solution = self.solution[1:-1] if self.solution else None
        for i in range(self.height):
            for j in range(self.width):
                if (i, j) == self.start:
                    print("A", end="")
                elif (i, j) == self.goal:
                    print("B", end="")
                elif solution and (i, j) in solution:
                    print("*", end="")
                elif (i, j) in self.walls:
                    print("█", end="")
                elif (i, j) in self.explored:
                    print("◌", end="")
                else:
                    print(" ", end="")
            print()
        print()

    def neighbors(self, state: Tuple[int, int]) -> Dict[str, Tuple[int, int]]:
        """
        Return the neighbors of a given state.

        Args:
            state: Current position

        Returns:
            Dictionary mapping actions to resulting states
        """
        row, col = state
        candidates = {
            "up": (row - 1, col),
            "down": (row + 1, col),
            "left": (row, col - 1),
            "right": (row, col + 1),
        }

        result = {}
        for action, (r, c) in candidates.items():
            if (
                0 <= r < self.height
                and 0 <= c < self.width
                and (r, c) not in self.walls
            ):
                result[action] = (r, c)

        return result

    def solve(self, algorithm: str = "dfs") -> bool:
        """
        Solve the maze using the specified algorithm.

        Args:
            algorithm: Either "dfs" for depth-first search or "bfs" for breadth-first search

        Returns:
            True if a solution is found, False otherwise
        """
        self.explored = set()

        # Initialize frontier based on algorithm
        if algorithm.lower() == "dfs":
            frontier = StackFrontier()
        elif algorithm.lower() == "bfs":
            frontier = QueueFrontier()
        else:
            raise ValueError("Invalid algorithm: choose 'dfs' or 'bfs'")

        # Initialize the starting state
        start = Node(state=self.start, parent=None, action=None)
        frontier.add(start)

        # Keep track of states explored
        self.explored = set()

        # Search for the solution
        while True:
            # If frontier is empty, no path exists
            if frontier.empty():
                self.solution = None
                return False

            # Choose a node from the frontier
            node = frontier.remove()

            # If node is the goal, we have a solution
            if node.state == self.goal:
                # Reconstruct solution
                actions = []
                cells = []

                while node.parent is not None:
                    actions.append(node.action)
                    cells.append(node.state)
                    node = node.parent

                actions.reverse()
                cells.reverse()

                self.solution = [self.start] + cells
                return True

            # Mark node as explored
            self.explored.add(node.state)

            # Add neighbors to frontier
            for action, state in self.neighbors(node.state).items():
                if not frontier.contains_state(state) and state not in self.explored:
                    child = Node(state=state, parent=node, action=action)
                    frontier.add(child)

    def output_image(
        self, filename: str, show_explored: bool = False, show_solution: bool = True
    ) -> None:
        """
        Output a visual representation of the maze.

        Args:
            filename: Path to save the image
            show_explored: Whether to show the explored states
            show_solution: Whether to show the solution path
        """
        cell_size = 50
        cell_border = 2

        # Create a new image
        img = Image.new(
            "RGBA", (self.width * cell_size, self.height * cell_size), "black"
        )
        draw = ImageDraw.Draw(img)

        # Fill the cells
        for i in range(self.height):
            for j in range(self.width):
                cell = (j * cell_size, i * cell_size)

                # Walls are black
                if (i, j) in self.walls:
                    fill = (40, 40, 40)

                # Start is green
                elif (i, j) == self.start:
                    fill = (50, 200, 50)

                # Goal is red
                elif (i, j) == self.goal:
                    fill = (200, 50, 50)

                # Solution is blue
                elif show_solution and self.solution and (i, j) in self.solution:
                    fill = (50, 50, 200)

                # Explored is light blue
                elif show_explored and (i, j) in self.explored:
                    fill = (200, 200, 255)

                # Empty cell is white
                else:
                    fill = (255, 255, 255)

                # Draw the cell
                draw.rectangle(
                    [cell, (cell[0] + cell_size, cell[1] + cell_size)], fill=fill
                )

        # Draw grid lines
        for i in range(self.height + 1):
            draw.line(
                [(0, i * cell_size), (self.width * cell_size, i * cell_size)],
                fill="black",
                width=cell_border,
            )
        for j in range(self.width + 1):
            draw.line(
                [(j * cell_size, 0), (j * cell_size, self.height * cell_size)],
                fill="black",
                width=cell_border,
            )

        # Save the image
        img.save(filename)
