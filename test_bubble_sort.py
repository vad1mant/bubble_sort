#!/usr/bin/env python3
"""
Test script for bubble sort algorithm
This script tests the sorting functionality without graphics for quick verification
"""

def bubble_sort_test(data):
    """Simple bubble sort implementation for testing"""
    arr = data.copy()
    n = len(arr)
    comparisons = 0
    swaps = 0
    
    for i in range(n):
        swapped = False
        for j in range(0, n - i - 1):
            comparisons += 1
            if arr[j] > arr[j + 1]:
                arr[j], arr[j + 1] = arr[j + 1], arr[j]
                swaps += 1
                swapped = True
        
        if not swapped:
            break
    
    return arr, comparisons, swaps

def test_bubble_sort():
    """Run various test cases"""
    print("Testing Bubble Sort Algorithm")
    print("=" * 40)
    
    test_cases = [
        [64, 34, 25, 12, 22, 11, 90],
        [5, 2, 4, 6, 1, 3],
        [1, 2, 3, 4, 5],
        [5, 4, 3, 2, 1],
        [1],
        [],
        [3, 3, 3, 3],
        [9, 8, 7, 6, 5, 4, 3, 2, 1]
    ]
    
    for i, test_data in enumerate(test_cases, 1):
        print(f"\nTest Case {i}: {test_data}")
        
        if not test_data:
            print("Empty array - skipping")
            continue
            
        sorted_arr, comparisons, swaps = bubble_sort_test(test_data)
        expected = sorted(test_data)
        
        print(f"Original: {test_data}")
        print(f"Sorted:   {sorted_arr}")
        print(f"Expected: {expected}")
        print(f"Comparisons: {comparisons}, Swaps: {swaps}")
        
        if sorted_arr == expected:
            print("✅ PASS")
        else:
            print("❌ FAIL")
            return False
    
    print("\n" + "=" * 40)
    print("All tests completed!")
    return True

def performance_test():
    """Test performance with larger arrays"""
    print("\nPerformance Test")
    print("-" * 20)
    
    import random
    
    sizes = [10, 50, 100]
    
    for size in sizes:
        # Generate random array
        data = [random.randint(1, 1000) for _ in range(size)]
        
        print(f"\nArray size: {size}")
        print(f"Sample data: {data[:5]}...")  # Show first 5 elements
        
        sorted_arr, comparisons, swaps = bubble_sort_test(data)
        
        print(f"Comparisons: {comparisons}")
        print(f"Swaps: {swaps}")
        print(f"Expected comparisons (worst case): {size * (size - 1) // 2}")
        
        # Verify sorting is correct
        if sorted_arr == sorted(data):
            print("✅ Sorting correct")
        else:
            print("❌ Sorting incorrect")
            return False
    
    return True

if __name__ == "__main__":
    print("Bubble Sort Test Suite")
    print("=" * 50)
    
    # Run basic tests
    basic_tests_passed = test_bubble_sort()
    
    # Run performance tests
    performance_tests_passed = performance_test()
    
    print("\n" + "=" * 50)
    if basic_tests_passed and performance_tests_passed:
        print("🎉 All tests passed! The bubble sort implementation is working correctly.")
    else:
        print("❌ Some tests failed. Please check the implementation.")
    
    print("\nTo run the full visualizer, execute:")
    print("python bubble_sort.py") 