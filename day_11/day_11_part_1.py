import os

# import collections
from collections import deque


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


def solve(input_data):
    adj = {}

    for line in input_data:
        key = line.split(":")[0]
        values = line.split(":")[1].strip().split(" ")
        if key in adj:
            print("There are duplicate keys")
        adj[key] = values

    result = 0

    q = deque(["you"])

    while q:
        node = q.popleft()

        if node == "out":
            result += 1
            continue

        for nbr in adj[node]:
            q.append(nbr)

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
    print(f"Solution for Day 11, Part One: {result}")


if __name__ == "__main__":
    main()
