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


def solve(grid):
    h, w = len(grid), len(grid[0])
    result = 0
    positions = set([(1, grid[0].index("S"))])

    while positions:
        next_positions = set()

        for pos in positions:
            r, c = pos
            if not 0 <= r < h - 1:
                continue
            if not 0 <= c < w:
                continue

            grid[r][c] = "|"

            if grid[r + 1][c] == ".":
                next_positions.add((r + 2, c))

            else:
                result += 1
                next_positions.add((r + 2, c - 1))
                next_positions.add((r + 2, c + 1))

        positions = next_positions

    # for row in grid:
    #     print(row)

    return result


def main():
    # Get the directory of the current script
    script_dir = os.path.dirname(os.path.abspath(__file__))

    # Construct the input file path relative to the script's location
    # input_path = os.path.join(script_dir, "input.txt")
    input_path = os.path.join(script_dir, "sample_input.txt")

    # Parse input
    parsed_input = parse_input(input_path)

    # Solve and print the solution
    result = solve(parsed_input)
    print(f"Solution for Day 07, Part One: {result}")


if __name__ == "__main__":
    main()
