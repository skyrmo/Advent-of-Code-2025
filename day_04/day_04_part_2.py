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

    return roll_count < 4


# prev time = 0.337 total
def solve(grid):
    h, w = len(grid), len(grid[0])
    result = 0

    removed_cells = [(-1, -1)]
    while removed_cells:
        removed_cells = []

        for r in range(h):
            for c in range(w):
                if grid[r][c] != "@":
                    continue

                if check_cell(grid, (r, c), h, w):
                    removed_cells.append((r, c))

        result += len(removed_cells)
        for r, c in removed_cells:
            grid[r][c] = "."

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
