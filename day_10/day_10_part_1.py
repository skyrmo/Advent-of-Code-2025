import os
import re
from collections import deque
from typing import Dict, List


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


def dfs(state: int, buttons: List[int]):
    if state == 0:
        return 0

    # state, prev_button, steps
    q = deque([(state, -1, 0)])
    visited = {state: 0}

    while q:
        state, prev_button, steps = q.popleft()

        for button in buttons:
            if button == prev_button:
                continue

            new_state = state ^ button
            new_steps = steps + 1

            if new_state == 0:
                return new_steps

            if new_state not in visited or new_steps < visited[new_state]:
                visited[new_state] = new_steps
                q.append((new_state, button, new_steps))

    return -1  # should never happen


def solve(input_data):
    result = float("inf")
    machines = []

    for line in input_data:
        parts = re.split(r"[\]{]", line)

        state = [x == "#" for x in parts[0][1:]]
        n = len(state)

        state_value = 0
        for bool in state:
            state_value = (state_value << 1) | int(bool)

        buttons = []
        for b in parts[1].strip().split(" "):
            button_list = [int(x) for x in b[1:-1].split(",")]
            button_value = 0
            for i in range(n):
                button_value = (button_value << 1) | int(i in button_list)

            buttons.append(button_value)

        machines.append((state_value, buttons))

    result = 0
    for state, buttons in machines:
        result += dfs(state, buttons)

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
    print(f"Solution for Day 10, Part One: {result}")


if __name__ == "__main__":
    main()
