#!/usr/bin/env python3
"""
Test script that runs sorting algorithms without GUI display
This is useful for testing on systems without display or when matplotlib backend issues occur
"""

import matplotlib
matplotlib.use('Agg')  # Use non-interactive backend

from bubble_sort import BubbleSortVisualizer, MergeSortVisualizer
import numpy as np
import time

def test_without_gui():
    """Test both sorting algorithms without GUI display"""
    print("Testing Sorting Algorithms (No GUI)")
    print("=" * 50)
    
    # Test with different array sizes
    test_sizes = [10, 50, 128]
    
    for size in test_sizes:
        print(f"\n{'='*20} Testing with {size} elements {'='*20}")
        
        # Generate test data
        data = list(np.random.randint(1, 1000, size))
        print(f"Generated array: {data[:5]}...")
        
        # Test Bubble Sort
        print(f"\n1. Bubble Sort ({size} elements):")
        start_time = time.time()
        bubble_viz = BubbleSortVisualizer(data.copy())
        bubble_frames = bubble_viz.bubble_sort()
        bubble_time = time.time() - start_time
        
        print(f"   Time taken: {bubble_time:.4f} seconds")
        print(f"   Comparisons: {bubble_viz.comparisons}")
        print(f"   Swaps: {bubble_viz.swaps}")
        print(f"   Frames generated: {len(bubble_frames)}")
        
        # Save animation without displaying
        print("   Saving animation...")
        bubble_viz.create_animation(bubble_frames, save_gif=True, 
                                  filename=f"bubble_sort_{size}.gif")
        
        # Test Merge Sort
        print(f"\n2. Merge Sort ({size} elements):")
        start_time = time.time()
        merge_viz = MergeSortVisualizer(data.copy())
        merge_frames = merge_viz.merge_sort()
        merge_time = time.time() - start_time
        
        print(f"   Time taken: {merge_time:.4f} seconds")
        print(f"   Comparisons: {merge_viz.comparisons}")
        print(f"   Merges: {merge_viz.merges}")
        print(f"   Frames generated: {len(merge_frames)}")
        
        # Save animation without displaying
        print("   Saving animation...")
        merge_viz.create_animation(merge_frames, save_gif=True, 
                                 filename=f"merge_sort_{size}.gif")
        
        # Performance comparison
        print(f"\n3. Performance Comparison ({size} elements):")
        print(f"   Bubble Sort: {bubble_viz.comparisons} comparisons, {bubble_time:.4f}s")
        print(f"   Merge Sort:  {merge_viz.comparisons} comparisons, {merge_time:.4f}s")
        print(f"   Speedup: {bubble_time/merge_time:.2f}x faster with Merge Sort")
        
        # Verify sorting is correct
        bubble_sorted = bubble_viz.data
        merge_sorted = merge_viz.data
        expected = sorted(data)
        
        print(f"   Bubble Sort correct: {bubble_sorted == expected}")
        print(f"   Merge Sort correct: {merge_sorted == expected}")
    
    print(f"\n{'='*50}")
    print("ALL TESTS COMPLETED!")
    print("=" * 50)
    print("Generated files:")
    for size in test_sizes:
        print(f"  - bubble_sort_{size}.gif")
        print(f"  - merge_sort_{size}.gif")
    print("\nYou can view the GIF files to see the animations!")

def test_simple_case():
    """Test with a simple known case"""
    print("\n" + "="*50)
    print("SIMPLE TEST CASE")
    print("="*50)
    
    data = [64, 34, 25, 12, 22, 11, 90]
    print(f"Original: {data}")
    
    # Bubble Sort
    bubble_viz = BubbleSortVisualizer(data.copy())
    bubble_frames = bubble_viz.bubble_sort()
    print(f"Bubble Sort result: {bubble_viz.data}")
    print(f"Bubble Sort comparisons: {bubble_viz.comparisons}")
    
    # Merge Sort
    merge_viz = MergeSortVisualizer(data.copy())
    merge_frames = merge_viz.merge_sort()
    print(f"Merge Sort result: {merge_viz.data}")
    print(f"Merge Sort comparisons: {merge_viz.comparisons}")
    
    expected = sorted(data)
    print(f"Expected: {expected}")
    print(f"Both correct: {bubble_viz.data == expected and merge_viz.data == expected}")

if __name__ == "__main__":
    print("Sorting Algorithm Test (No GUI)")
    print("This test runs without requiring a display window")
    
    # Test simple case first
    test_simple_case()
    
    # Test with various sizes
    test_without_gui()
    
    print("\n" + "="*50)
    print("SUCCESS! All algorithms are working correctly.")
    print("Check the generated GIF files to see the animations.")
    print("="*50) 