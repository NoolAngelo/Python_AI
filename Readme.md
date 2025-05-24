# Python AI & Algorithms Collection

A comprehensive collection of Python implementations for classic algorithms, AI techniques, and programming utilities.

## 🚀 Features

This repository contains:

- **Maze Solving Algorithms**: Several versions of maze solvers using search algorithms like BFS and DFS
- **Sorting Algorithms**: Implementations of common sorting techniques
  - Bubble Sort
  - Insertion Sort
  - Merge Sort
  - Quick Sort
  - Selection Sort
- **Dynamic Programming**: Knapsack problem solver
- **File Processing**: Utilities for reading and processing data files

## 📋 Table of Contents

- [Installation](#installation)
- [Usage](#usage)
  - [Maze Solver](#maze-solver)
  - [Sorting Algorithms](#sorting-algorithms)
  - [Knapsack Problem](#knapsack-problem)
  - [File Processing](#file-processing)
- [Project Structure](#project-structure)
- [Contributing](#contributing)
- [License](#license)
- [Changelog](#changelog)

## 🔧 Installation

Clone this repository:

```bash
git clone https://github.com/yourusername/Python_AI.git
cd Python_AI
```

Install dependencies:

```bash
pip install pillow  # For maze visualization
```

## 💻 Usage

### Maze Solver

The maze solver accepts text files where:

- `#` represents walls
- `A` represents the starting point
- `B` represents the goal

```bash
python maze.py maze.txt
```

This will generate a solution visualization as an image.

### Sorting Algorithms

Run any of the sorting algorithms interactively:

```bash
python sorting/bubble_sort.py
# Enter numbers separated by spaces when prompted
```

Or import and use the algorithms in your own code:

```python
from sorting.bubble_sort import bubble
from sorting.quick_sort import quicksort

sorted_list = bubble([5, 3, 8, 2, 1])
print(sorted_list)  # [1, 2, 3, 5, 8]
```

### Knapsack Problem

Solve the classic 0/1 Knapsack problem:

```python
from sorting.Knapsack import knapsack_01

weights = [10, 20, 30]
values = [60, 100, 120]
capacity = 50

total_weight, total_value, num_items, selected = knapsack_01(weights, values, capacity)
print(f"Maximum value: {total_value}")
print(f"Selected items: {selected}")
```

### File Processing

Process CSV files:

```bash
python "Python read from file/readfile.py" "Python read from file/cereal.csv"
```

## 📁 Project Structure

```
.
├── maze_ver*.py          # Different versions of maze solver
├── maze.py               # Main maze solver implementation
├── maze.txt              # Sample maze input
├── maze*.png             # Generated maze solutions
├── README.md             # This file
├── Python read from file/
│   ├── cereal.csv        # Sample CSV data
│   └── readfile.py       # CSV file processor
└── sorting/
    ├── bubble_sort.py    # Bubble sort implementation
    ├── insertion_sort.py # Insertion sort implementation
    ├── Knapsack.py       # Knapsack problem solver
    ├── merge_sort.py     # Merge sort implementation
    ├── quick_sort.py     # Quick sort implementation
    └── Selection_sort.py # Selection sort implementation
    └── sortinghat.py     # Sorting algorithms comparison
```

## 👥 Contributing

Contributions are welcome! Please feel free to submit a Pull Request.

1. Fork the repository
2. Create your feature branch (`git checkout -b feature/amazing-feature`)
3. Commit your changes (`git commit -m 'Add some amazing feature'`)
4. Push to the branch (`git push origin feature/amazing-feature`)
5. Open a Pull Request

## 📄 License

This project is licensed under the MIT License - see the LICENSE file for details.

## 📝 Changelog

### [1.0.2] - 2024-11-4

- Added a changelog

## [1.0.3] - Current

### Added

- Implemented A\* pathfinding algorithm for maze solving
- Added PriorityQueueFrontier class for efficient node exploration
- Added maze visualization with PIL
- Implemented Manhattan distance heuristic
- Added support for visual maze solution output as PNG
- Added command-line interface for maze file input

### Technical

- Type hints added for better code documentation
- Error handling for maze file loading and solving
- Solution path visualization with colored tiles
- Automatic file naming for multiple solution outputs

## [1.0.4] - Current

### Added

- Added proper cost tracking for A\* algorithm
- Added comprehensive docstrings
- Added color configuration dictionary

### Changed

- Optimized PriorityQueueFrontier using heapq
- Improved maze visualization configuration
- Enhanced error handling and messages

### Fixed

- Removed duplicate main block
- Improved state tracking in frontier
