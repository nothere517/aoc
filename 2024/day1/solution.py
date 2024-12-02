#!/usr/bin/env python3
"""
Advent of Code 2024 - Day 1 Solution
"""

def parse_input(input_file: str) -> list[str]:
    """Read and parse input file."""
    with open(input_file, 'r') as f:
        return f.read().splitlines()

def solve_part1(data: list[str]) -> int:
    """Solve part 1 of the puzzle."""
    pass

def solve_part2(data: list[str]) -> int:
    """Solve part 2 of the puzzle."""
    pass

if __name__ == "__main__":
    input_data = parse_input("input.txt")
    
    # Part 1
    print(f"Part 1: {solve_part1(input_data)}")
    
    # Part 2
    print(f"Part 2: {solve_part2(input_data)}")
