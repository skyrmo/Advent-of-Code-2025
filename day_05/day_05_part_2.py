import os


def parse_input(file_path):
    # Parse the input file
    with open(file_path, "r") as file:
        # Read the entire file
        data = file.read().strip()

        # 2. Read as a list of lines
        return data.split("\n\n")

        # 3. Read as a list of integers
        # return [int(line) for line in data.split('\n')]

        # 4. Read as a list of lists (e.g., for grid-like inputs)
        # return [list(line) for line in data.split('\n')]

        return data


def solve(input_data):
    range_data = input_data[0].split("\n")
    ranges = []
    result = 0

    for r in range_data:
        s, e = r.split("-")
        ranges.append((int(s), int(e)))

    ranges.sort(key=lambda x: (x[0], x[1]))

    filtered_ranges = [[ranges[0][0], ranges[0][1]]]

    for start, end in ranges[1:]:
        prev_end = filtered_ranges[-1][1]

        if start > prev_end:
            filtered_ranges.append([start, end])
        else:
            filtered_ranges[-1][1] = max(prev_end, end)

    for start, end in filtered_ranges:
        result += end - start + 1

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
    print(f"Solution for Day 05, Part One: {result}")


if __name__ == "__main__":
    main()
