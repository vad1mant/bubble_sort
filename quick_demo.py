#!/usr/bin/env python3
"""
Quick demo of the sorting algorithm visualizer
This script runs both bubble sort and merge sort with a 128-element array
"""

from bubble_sort import BubbleSortVisualizer, MergeSortVisualizer
import numpy as np

def quick_demo():
    """Run a quick demonstration of both sorting algorithms"""
    print("Sorting Algorithm Quick Demo")
    print("=" * 40)
    
    # Generate a 128-element array for demonstration
    data = list(np.random.randint(1, 1000, 128))
    print(f"Generated array of size: {len(data)}")
    print(f"Sample data: {data[:10]}...")
    
    # Test both algorithms
    algorithms = [
        ("Bubble Sort", BubbleSortVisualizer, "bubble_sort_demo.gif"),
        ("Merge Sort", MergeSortVisualizer, "merge_sort_demo.gif")
    ]
    
    for name, visualizer_class, filename in algorithms:
        print(f"\n{'='*20} {name} {'='*20}")
        
        # Create visualizer
        visualizer = visualizer_class(data.copy())
        
        # Run sorting algorithm
        print(f"Running {name}...")
        if name == "Bubble Sort":
            frames = visualizer.bubble_sort()
        else:
            frames = visualizer.merge_sort()
        
        # Display animation
        print(f"Displaying {name} animation...")
        print("Close the plot window to continue...")
        visualizer.create_animation(frames, save_gif=True, filename=filename)
        
        # Print results
        visualizer.print_sorting_info()
    
    print("\n" + "=" * 60)
    print("DEMO COMPLETED!")
    print("=" * 60)
    print("Files generated:")
    print("- bubble_sort_demo.gif")
    print("- merge_sort_demo.gif")
    print("\nKey differences observed:")
    print("- Bubble Sort: O(n²) - Many comparisons and swaps")
    print("- Merge Sort:  O(n log n) - Fewer comparisons, uses divide-and-conquer")
    print("- Merge Sort is much more efficient for large arrays!")

if __name__ == "__main__":
    quick_demo() 