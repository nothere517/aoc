#!/usr/bin/env python3
"""
Advent of Code 2024 - Day 1 Solution
"""

def parse_input(input_file: str) -> tuple[list[int], list[int]]:
    """Read and parse input file into two lists of numbers."""
    left_list = []
    right_list = []
    
    with open(input_file, 'r') as f:
        for line in f:
            # Split each line into two numbers
            left, right = line.strip().split()
            left_list.append(int(left))
            right_list.append(int(right))
    
    return left_list, right_list

def solver(data: tuple[list[int], list[int]]) -> int:
    """
    Solve part 1: Calculate total distance between paired numbers from sorted lists.
    Returns the sum of absolute differences between paired numbers.
    """
    # Parse input into two lists
    left_list, right_list = data
    
    # Sort both lists
    left_sorted = sorted(left_list)
    right_sorted = sorted(right_list)
    
    # Calculate total distance
    total_distance = 0
    for left, right in zip(left_sorted, right_sorted):
        distance = abs(left - right)
        print(f"Distance between {left} and {right}: {distance}")
        total_distance += distance
    
    return total_distance

if __name__ == "__main__":
    # Read input and convert to proper format
    raw_data = parse_input("input.txt")
    
    print(f"Total distance between list numbers: {solver(raw_data)}")
    