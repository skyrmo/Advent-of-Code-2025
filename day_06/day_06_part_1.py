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
    lines = [x.split() for x in input_data]

    n = len(lines[0])
    result = 0

    for i in range(n):
        operator = lines[4][i]
        cur_sum = int(lines[0][i])

        if operator == "+":
            for j in range(1, 4):
                cur_sum += int(lines[j][i])
        else:
            for j in range(1, 4):
                cur_sum *= int(lines[j][i])

        result += cur_sum

    return result

    # for line in lines:
    #     print(len(line))


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
    print(f"Solution for Day 06, Part One: {result}")


if __name__ == "__main__":
    main()
