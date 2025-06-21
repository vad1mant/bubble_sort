# Sorting Algorithm Visualizer

A Python program that demonstrates sorting algorithms with animated graphics using matplotlib. Features both Bubble Sort and Merge Sort with performance comparison.

## Features

- **Two Sorting Algorithms**: 
  - **Bubble Sort** - O(n²) - Simple, in-place sorting
  - **Merge Sort** - O(n log n) - Efficient, divide-and-conquer approach
- **Animated Visualization**: Watch sorting algorithms in action with color-coded bars
- **Large Array Support**: Handles arrays up to 128 elements efficiently
- **Interactive Mode**: Input your own arrays or generate random ones
- **Demo Mode**: Run predefined examples including 128-element arrays
- **Performance Comparison**: Compare algorithms side-by-side
- **Statistics**: Track comparisons, swaps/merges, and complexity information
- **GIF Export**: Save animations as GIF files for sharing or documentation
- **Educational**: Perfect for learning and teaching sorting algorithms

## Color Coding

### Bubble Sort
- **Gray**: Untouched elements
- **Blue**: Elements being compared
- **Green**: Elements being swapped

### Merge Sort
- **Gray**: Untouched elements
- **Blue**: Left element being compared
- **Red**: Right element being compared
- **Green**: Element being merged

## Installation

1. Make sure you have Python 3.7+ installed
2. Install the required dependencies:

```bash
pip install -r requirements.txt
```

## Usage

Run the program:

```bash
python bubble_sort.py
```

### Interactive Mode
Choose option 1 to:
- Generate a random array of specified size (up to 128)
- Input your own custom array
- Choose between Bubble Sort and Merge Sort
- Watch the sorting animation
- Optionally save the animation as a GIF

### Demo Mode
Choose option 2 to:
- Run through predefined example arrays (including 128 elements)
- Automatically compare both algorithms
- Save animations as GIF files
- See performance differences

## Example Output

```
Welcome to Sorting Algorithm Visualizer!
==================================================
Algorithms available:
1. Bubble Sort - O(n²) - Simple, in-place
2. Merge Sort  - O(n log n) - Efficient, divide-and-conquer
==================================================

Sorting Algorithm Demo
--------------------

Demo 1: Array size 7
Sample data: [64, 34, 25, 12, 22, 11, 90]...

============================================================
Comparing algorithms on array of size 7
============================================================

1. Running Bubble Sort...
Saving animation to bubble_sort_comparison.gif...

==================================================
BUBBLE SORT VISUALIZATION
==================================================
Original array: [64, 34, 25, 12, 22, 11, 90]
Sorted array:   [11, 12, 22, 25, 34, 64, 90]
Array length:   7
Comparisons:    21
Swaps:          14
Time complexity: O(n²)
Space complexity: O(1)
==================================================

2. Running Merge Sort...
Saving animation to merge_sort_comparison.gif...

==================================================
MERGE SORT VISUALIZATION
==================================================
Original array: [64, 34, 25, 12, 22, 11, 90]
Sorted array:   [11, 12, 22, 25, 34, 64, 90]
Array length:   7
Comparisons:    12
Merges:         6
Time complexity: O(n log n)
Space complexity: O(n)
==================================================

============================================================
PERFORMANCE COMPARISON
============================================================
Array size: 7
Bubble Sort - Comparisons: 21, Swaps: 14
Merge Sort  - Comparisons: 12, Merges: 6
Bubble Sort complexity: O(n²) = O(7²) = O(49)
Merge Sort  complexity: O(n log n) = O(7 log 7) ≈ O(20)
```

## Algorithm Details

### Bubble Sort Algorithm
1. Compare adjacent elements
2. If they are in wrong order, swap them
3. Repeat until no swaps are needed

**Time Complexity:**
- **Best Case**: O(n) - when array is already sorted
- **Average Case**: O(n²)
- **Worst Case**: O(n²)

**Space Complexity:** O(1) - in-place sorting algorithm

### Merge Sort Algorithm
1. Divide the array into two halves
2. Recursively sort the two halves
3. Merge the sorted halves

**Time Complexity:**
- **Best Case**: O(n log n)
- **Average Case**: O(n log n)
- **Worst Case**: O(n log n)

**Space Complexity:** O(n) - requires additional space

## Why Merge Sort?

I chose **Merge Sort** as the second algorithm because:

1. **Efficiency**: O(n log n) vs O(n²) for bubble sort - much faster for large arrays
2. **Divide-and-Conquer**: Demonstrates a different algorithmic paradigm
3. **Stable Sort**: Maintains relative order of equal elements
4. **Predictable Performance**: Consistent O(n log n) regardless of input
5. **Educational Value**: Shows how recursion and merging work
6. **Visual Contrast**: Creates very different visual patterns compared to bubble sort

## Files Generated

- `bubble_sort_demo.gif` - Bubble sort animation
- `merge_sort_demo.gif` - Merge sort animation
- `bubble_sort_comparison.gif` - Comparison mode bubble sort
- `merge_sort_comparison.gif` - Comparison mode merge sort

## Requirements

- Python 3.7+
- matplotlib
- numpy
- pillow

## Educational Value

This program is excellent for:
- Understanding how different sorting algorithms work
- Visualizing algorithm complexity differences
- Learning about divide-and-conquer vs iterative approaches
- Teaching computer science concepts
- Comparing algorithm performance empirically
- Understanding recursion vs iteration

## Performance Insights

With 128 elements:
- **Bubble Sort**: ~8,128 comparisons, O(16,384)
- **Merge Sort**: ~896 comparisons, O(896)

The difference becomes dramatic with larger arrays!

## Customization

You can modify the program to:
- Change animation speed (modify `interval` parameter)
- Adjust colors and styling
- Add more sorting algorithms (Quick Sort, Heap Sort, etc.)
- Include additional statistics
- Modify the visualization style
- Change the maximum array size 