import collections
import os


def parse_input(file_path):
    # Parse the input file
    with open(file_path, "r") as file:
        # Read the entire file
        data = file.read().strip()

        # 2. Read as a list of lines
        # return data.split('\n')

        # 3. Read as a list of integers
        # return [int(line) for line in data.split('\n')]

        # 4. Read as a list of lists (e.g., for grid-like inputs)
        return [list(line) for line in data.split("\n")]

        return data


def check_cell(grid, pos, h, w):
    r, c = pos
    adj_cells = [
        (r - 1, c - 1),
        (r - 1, c),
        (r - 1, c + 1),
        (r, c - 1),
        (r, c + 1),
        (r + 1, c - 1),
        (r + 1, c),
        (r + 1, c + 1),
    ]
    roll_count = 0

    for nr, nc in adj_cells:
        if not (0 <= nr < h):
            continue

        if not (0 <= nc < w):
            continue

        if grid[nr][nc] == "@":
            roll_count += 1

    # print(r, c, roll_count)

    return roll_count < 4


def solve(grid):
    # print(grid)
    h, w = len(grid), len(grid[0])
    result = 0

    for r in range(h):
        for c in range(w):
            if grid[r][c] != "@":
                continue

            if check_cell(grid, (r, c), h, w):
                result += 1

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
    print(f"Solution for Day 04, Part One: {result}")


if __name__ == "__main__":
    main()
