import collections
import os


def parse_input(file_path):
    # Parse the input file
    with open(file_path, "r") as file:
        # Read the entire file
        data = file.read().strip()

        # 2. Read as a list of lines
        return data.split(",")

        # 3. Read as a list of integers
        # return [int(line) for line in data.split('\n')]

        # 4. Read as a list of lists (e.g., for grid-like inputs)
        # return [list(line) for line in data.split('\n')]

        return data


def solve(input_data):
    # print(input_data)
    result = 0

    for rng in input_data:
        s, e = rng.split("-")
        start, end = int(s), int(e)
        # print(rng, start, end)
        for i in range(start, end + 1):
            # print(i)
            i_str = str(i)
            i_len = len(i_str)
            if len(i_str) % 2 == 1:
                continue
            if i_str[: i_len // 2] == i_str[i_len // 2 :]:
                print(i, i_str[: i_len // 2], i_str[i_len // 2 :])
                result += i

    return result


def main():
    # Get the directory of the current script
    script_dir = os.path.dirname(os.path.abspath(__file__))

    # Construct the input file path relative to the script's location
    input_path = os.path.join(script_dir, "input.txt")

    # Parse input
    parsed_input = parse_input(input_path)

    # Solve and print the solution
    result = solve(parsed_input)
    print(f"Solution for Day 02, Part One: {result}")


if __name__ == "__main__":
    main()
