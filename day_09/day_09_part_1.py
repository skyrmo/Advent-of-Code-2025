import collections
import os


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
    points = []
    for line in input_data:
        c, r = line.split(",")
        points.append((int(r), int(c)))

    n = len(points)

    result = 0

    for i in range(n):
        for j in range(i + 1, n):
            r1, c1 = points[i]
            r2, c2 = points[j]

            result = max(
                result,
                (max(r1, r2) - min(r1, r2) + 1) * (max(c1, c2) - min(c1, c2) + 1),
            )

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
    print(f"Solution for Day 09, Part One: {result}")


if __name__ == "__main__":
    main()
