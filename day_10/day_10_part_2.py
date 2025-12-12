import os
import re
from collections import deque
from typing import List

from z3 import Int, Optimize, sat


def parse_input(file_path):
    # Parse the input file
    with open(file_path, "r") as file:
        # Read the entire file
        data = file.read().strip()

        # 2. Read as a list of lines
        return data.split("\n")

        # 3. Read as a list of integers
        # return [int(line) for line in data.split('\n')]

        # 4. Read as a list of lists (e.g., for grid-like inputs)
        # return [list(line) for line in data.split('\n')]

        return data


def solve_with_z3(buttons, target):
    # Solve the minimal button presses problem using Z3.
    #
    # Args:
    #   buttons: List of button definitions, where each button is a list of counter indices it affects
    #             e.g., [[3], [1,3], [2], [2,3], [0,2], [0,1]]
    #    target: Target counter values, e.g., [3, 5, 4, 7]
    #
    # Returns:
    #    Minimum number of button presses, or None if no solution exists

    num_buttons = len(buttons)
    num_counters = len(target)

    # Create Z3 optimizer
    opt = Optimize()

    # Create integer variables for each button (number of times pressed)
    x = [Int(f"x_{i}") for i in range(num_buttons)]

    # Add non-negativity constraints
    for i in range(num_buttons):
        opt.add(x[i] >= 0)

    # Build constraints: for each counter, sum of button presses affecting it must equal target
    for counter_idx in range(num_counters):
        # Find which buttons affect this counter
        affecting_buttons = []
        for button_idx, button in enumerate(buttons):
            if counter_idx in button:
                affecting_buttons.append(x[button_idx])

        # Sum of all affecting button presses must equal the target for this counter
        if affecting_buttons:
            opt.add(sum(affecting_buttons) == target[counter_idx])
        else:
            # If no button affects this counter, target must be 0
            if target[counter_idx] != 0:
                return None  # No solution possible

    # Minimize the total number of button presses
    total_presses = sum(x)
    opt.minimize(total_presses)

    # Check if the problem is solvable
    if opt.check() == sat:
        model = opt.model()
        # Extract the minimum value
        min_presses = model.eval(total_presses).as_long()

        return min_presses
    else:
        return None  # No solution exists


def solve(input_data):
    result = 0
    machines = []

    for line in input_data:
        parts = re.split(r"[\]{]", line)

        buttons = []
        for b in parts[1].strip().split(" "):
            buttons.append([int(x) for x in b[1:-1].split(",")])

        target = [int(x) for x in parts[2][:-1].split(",")]

        machines.append((buttons, target))

    for idx, (buttons, target) in enumerate(machines):
        min_presses = solve_with_z3(buttons, target)
        if min_presses is not None:
            result += min_presses

    return result


def main():
    # Get the directory of the current script
    script_dir = os.path.dirname(os.path.abspath(__file__))

    # Construct the input file path relative to the script's location
    input_path = os.path.join(script_dir, "input.txt")
    # input_path = os.path.join(script_dir, "sample_input.txt")

    # Parse input
    parsed_input = parse_input(input_path)

    # Solve and print the solution
    result = solve(parsed_input)
    print(f"Solution for Day 10, Part Two: {result}")


if __name__ == "__main__":
    main()
