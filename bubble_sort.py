import matplotlib.pyplot as plt
import matplotlib.animation as animation
import matplotlib.patches as patches
import numpy as np
import time
from typing import List, Tuple

class BubbleSortVisualizer:
    def __init__(self, data: List[int]):
        self.data = data.copy()
        self.original_data = data.copy()
        self.frames = []
        self.comparisons = 0
        self.swaps = 0
        
    def bubble_sort(self) -> List[Tuple[List[int], int, int]]:
        """
        Perform bubble sort and record each step for visualization
        Returns: List of tuples (array_state, comparison_index, swap_index)
        """
        n = len(self.data)
        frames = []
        
        for i in range(n):
            swapped = False
            for j in range(0, n - i - 1):
                self.comparisons += 1
                frames.append((self.data.copy(), j, -1))  # Comparison frame
                
                if self.data[j] > self.data[j + 1]:
                    # Swap elements
                    self.data[j], self.data[j + 1] = self.data[j + 1], self.data[j]
                    self.swaps += 1
                    frames.append((self.data.copy(), j, j + 1))  # Swap frame
                    swapped = True
                else:
                    frames.append((self.data.copy(), j, -1))  # No swap frame
            
            if not swapped:
                break
                
        return frames
    
    def create_animation(self, frames: List[Tuple[List[int], int, int]], 
                        save_gif: bool = False, filename: str = "bubble_sort.gif"):
        """
        Create and display animation of the bubble sort process
        """
        fig, ax = plt.subplots(figsize=(16, 10))
        
        def animate(frame_data):
            ax.clear()
            data, comp_idx, swap_idx = frame_data
            
            # Create bar chart with updated color scheme
            bars = ax.bar(range(len(data)), data, 
                         color=['blue' if i == comp_idx else 
                               'green' if i == swap_idx else 
                               'gray' for i in range(len(data))])
            
            # Add value labels on bars (only for smaller arrays)
            if len(data) <= 50:
                for i, (bar, val) in enumerate(zip(bars, data)):
                    height = bar.get_height()
                    ax.text(bar.get_x() + bar.get_width()/2., height + 0.1,
                           f'{val}', ha='center', va='bottom', fontweight='bold', fontsize=8)
            
            ax.set_title(f'Bubble Sort Visualization\nComparisons: {self.comparisons} | Swaps: {self.swaps}', 
                        fontsize=14, fontweight='bold')
            ax.set_xlabel('Array Index', fontsize=12)
            ax.set_ylabel('Value', fontsize=12)
            ax.set_ylim(0, max(self.original_data) + 2)
            ax.grid(True, alpha=0.3)
            
            # Add legend with updated colors
            legend_elements = [
                patches.Rectangle((0,0),1,1, facecolor='gray', label='Untouched'),
                patches.Rectangle((0,0),1,1, facecolor='blue', label='Comparing'),
                patches.Rectangle((0,0),1,1, facecolor='green', label='Swapping')
            ]
            ax.legend(handles=legend_elements, loc='upper right')
            
        # Create animation
        anim = animation.FuncAnimation(fig, animate, frames=frames, 
                                     interval=100, repeat=False, blit=False)
        
        if save_gif:
            print(f"Saving animation to {filename}...")
            anim.save(filename, writer='pillow', fps=5)
            print(f"Animation saved as {filename}")
        
        plt.tight_layout()
        plt.show()
        
        return anim
    
    def print_sorting_info(self):
        """Print information about the sorting process"""
        print("=" * 50)
        print("BUBBLE SORT VISUALIZATION")
        print("=" * 50)
        print(f"Original array: {self.original_data[:10]}{'...' if len(self.original_data) > 10 else ''}")
        print(f"Sorted array:   {self.data[:10]}{'...' if len(self.data) > 10 else ''}")
        print(f"Array length:   {len(self.data)}")
        print(f"Comparisons:    {self.comparisons}")
        print(f"Swaps:          {self.swaps}")
        print(f"Time complexity: O(n²)")
        print(f"Space complexity: O(1)")
        print("=" * 50)

class MergeSortVisualizer:
    def __init__(self, data: List[int]):
        self.data = data.copy()
        self.original_data = data.copy()
        self.frames = []
        self.comparisons = 0
        self.merges = 0
        
    def merge_sort(self) -> List[Tuple[List[int], int, int, int]]:
        """
        Perform merge sort and record each step for visualization
        Returns: List of tuples (array_state, left_idx, right_idx, merge_idx)
        """
        self.frames = []
        self._merge_sort_recursive(0, len(self.data) - 1)
        return self.frames
    
    def _merge_sort_recursive(self, left: int, right: int):
        """Recursive merge sort implementation"""
        if left < right:
            mid = (left + right) // 2
            
            # Recursively sort left and right halves
            self._merge_sort_recursive(left, mid)
            self._merge_sort_recursive(mid + 1, right)
            
            # Merge the sorted halves
            self._merge(left, mid, right)
    
    def _merge(self, left: int, mid: int, right: int):
        """Merge two sorted subarrays"""
        left_half = self.data[left:mid + 1]
        right_half = self.data[mid + 1:right + 1]
        
        i = j = 0
        k = left
        
        while i < len(left_half) and j < len(right_half):
            self.comparisons += 1
            self.frames.append((self.data.copy(), left + i, mid + 1 + j, k))
            
            if left_half[i] <= right_half[j]:
                self.data[k] = left_half[i]
                i += 1
            else:
                self.data[k] = right_half[j]
                j += 1
            k += 1
            self.merges += 1
        
        # Copy remaining elements
        while i < len(left_half):
            self.data[k] = left_half[i]
            i += 1
            k += 1
            self.merges += 1
        
        while j < len(right_half):
            self.data[k] = right_half[j]
            j += 1
            k += 1
            self.merges += 1
        
        self.frames.append((self.data.copy(), -1, -1, -1))
    
    def create_animation(self, frames: List[Tuple[List[int], int, int, int]], 
                        save_gif: bool = False, filename: str = "merge_sort.gif"):
        """
        Create and display animation of the merge sort process
        """
        fig, ax = plt.subplots(figsize=(16, 10))
        
        def animate(frame_data):
            ax.clear()
            data, left_idx, right_idx, merge_idx = frame_data
            
            # Create bar chart with merge sort color scheme
            colors = ['gray'] * len(data)
            if left_idx >= 0:
                colors[left_idx] = 'blue'  # Left element being compared
            if right_idx >= 0:
                colors[right_idx] = 'red'  # Right element being compared
            if merge_idx >= 0:
                colors[merge_idx] = 'green'  # Element being merged
            
            bars = ax.bar(range(len(data)), data, color=colors)
            
            # Add value labels on bars (only for smaller arrays)
            if len(data) <= 50:
                for i, (bar, val) in enumerate(zip(bars, data)):
                    height = bar.get_height()
                    ax.text(bar.get_x() + bar.get_width()/2., height + 0.1,
                           f'{val}', ha='center', va='bottom', fontweight='bold', fontsize=8)
            
            ax.set_title(f'Merge Sort Visualization\nComparisons: {self.comparisons} | Merges: {self.merges}', 
                        fontsize=14, fontweight='bold')
            ax.set_xlabel('Array Index', fontsize=12)
            ax.set_ylabel('Value', fontsize=12)
            ax.set_ylim(0, max(self.original_data) + 2)
            ax.grid(True, alpha=0.3)
            
            # Add legend for merge sort
            legend_elements = [
                patches.Rectangle((0,0),1,1, facecolor='gray', label='Untouched'),
                patches.Rectangle((0,0),1,1, facecolor='blue', label='Left Element'),
                patches.Rectangle((0,0),1,1, facecolor='red', label='Right Element'),
                patches.Rectangle((0,0),1,1, facecolor='green', label='Merging')
            ]
            ax.legend(handles=legend_elements, loc='upper right')
            
        # Create animation
        anim = animation.FuncAnimation(fig, animate, frames=frames, 
                                     interval=100, repeat=False, blit=False)
        
        if save_gif:
            print(f"Saving animation to {filename}...")
            anim.save(filename, writer='pillow', fps=5)
            print(f"Animation saved as {filename}")
        
        plt.tight_layout()
        plt.show()
        
        return anim
    
    def print_sorting_info(self):
        """Print information about the sorting process"""
        print("=" * 50)
        print("MERGE SORT VISUALIZATION")
        print("=" * 50)
        print(f"Original array: {self.original_data[:10]}{'...' if len(self.original_data) > 10 else ''}")
        print(f"Sorted array:   {self.data[:10]}{'...' if len(self.data) > 10 else ''}")
        print(f"Array length:   {len(self.data)}")
        print(f"Comparisons:    {self.comparisons}")
        print(f"Merges:         {self.merges}")
        print(f"Time complexity: O(n log n)")
        print(f"Space complexity: O(n)")
        print("=" * 50)

def interactive_sorting():
    """Interactive function to run sorting algorithms with user input"""
    print("Sorting Algorithm Visualizer")
    print("-" * 30)
    
    # Get user input
    choice = input("Choose input method:\n1. Random array\n2. Custom array\nEnter choice (1 or 2): ")
    
    if choice == "1":
        size = int(input("Enter array size (5-128 recommended): "))
        data = list(np.random.randint(1, 1000, size))
        print(f"Generated array: {data[:10]}{'...' if len(data) > 10 else ''}")
    elif choice == "2":
        data_str = input("Enter numbers separated by spaces: ")
        data = [int(x) for x in data_str.split()]
    else:
        print("Invalid choice. Using default array.")
        data = list(np.random.randint(1, 1000, 20))
    
    # Choose algorithm
    algo_choice = input("Choose algorithm:\n1. Bubble Sort\n2. Merge Sort\nEnter choice (1 or 2): ")
    
    # Ask user about saving animation
    save_choice = input("Save animation as GIF? (y/n): ").lower()
    save_gif = save_choice == 'y'
    
    if algo_choice == "1":
        visualizer = BubbleSortVisualizer(data)
        frames = visualizer.bubble_sort()
        visualizer.create_animation(frames, save_gif=save_gif, filename="bubble_sort.gif")
        visualizer.print_sorting_info()
    elif algo_choice == "2":
        visualizer = MergeSortVisualizer(data)
        frames = visualizer.merge_sort()
        visualizer.create_animation(frames, save_gif=save_gif, filename="merge_sort.gif")
        visualizer.print_sorting_info()
    else:
        print("Invalid choice. Running both algorithms...")
        run_comparison_demo(data, save_gif)

def run_comparison_demo(data, save_gif=False):
    """Run both algorithms on the same data for comparison"""
    print(f"\nComparing algorithms on array of size {len(data)}")
    print("=" * 60)
    
    # Bubble Sort
    print("\n1. Running Bubble Sort...")
    bubble_viz = BubbleSortVisualizer(data)
    bubble_frames = bubble_viz.bubble_sort()
    bubble_viz.create_animation(bubble_frames, save_gif=save_gif, filename="bubble_sort_comparison.gif")
    bubble_viz.print_sorting_info()
    
    # Merge Sort
    print("\n2. Running Merge Sort...")
    merge_viz = MergeSortVisualizer(data)
    merge_frames = merge_viz.merge_sort()
    merge_viz.create_animation(merge_frames, save_gif=save_gif, filename="merge_sort_comparison.gif")
    merge_viz.print_sorting_info()
    
    # Performance comparison
    print("\n" + "=" * 60)
    print("PERFORMANCE COMPARISON")
    print("=" * 60)
    print(f"Array size: {len(data)}")
    print(f"Bubble Sort - Comparisons: {bubble_viz.comparisons}, Swaps: {bubble_viz.swaps}")
    print(f"Merge Sort  - Comparisons: {merge_viz.comparisons}, Merges: {merge_viz.merges}")
    print(f"Bubble Sort complexity: O(n²) = O({len(data)}²) = O({len(data)**2})")
    print(f"Merge Sort  complexity: O(n log n) = O({len(data)} log {len(data)}) ≈ O({len(data) * np.log2(len(data)):.0f})")

def demo_sorting_algorithms():
    """Run demonstrations with predefined arrays including 128 elements"""
    print("Sorting Algorithm Demo")
    print("-" * 20)
    
    # Demo arrays including 128 elements
    demo_arrays = [
        [64, 34, 25, 12, 22, 11, 90],
        list(np.random.randint(1, 1000, 50)),
        list(np.random.randint(1, 1000, 128))  # 128 bars as requested
    ]
    
    for i, data in enumerate(demo_arrays, 1):
        print(f"\nDemo {i}: Array size {len(data)}")
        print(f"Sample data: {data[:5]}{'...' if len(data) > 5 else ''}")
        
        # Run both algorithms
        run_comparison_demo(data, save_gif=True)
        time.sleep(2)

if __name__ == "__main__":
    print("Welcome to Sorting Algorithm Visualizer!")
    print("=" * 50)
    print("Algorithms available:")
    print("1. Bubble Sort - O(n²) - Simple, in-place")
    print("2. Merge Sort  - O(n log n) - Efficient, divide-and-conquer")
    print("=" * 50)
    
    mode = input("Choose mode:\n1. Interactive (custom input)\n2. Demo (predefined arrays)\nEnter choice (1 or 2): ")
    
    if mode == "1":
        interactive_sorting()
    elif mode == "2":
        demo_sorting_algorithms()
    else:
        print("Invalid choice. Running demo mode...")
        demo_sorting_algorithms()
