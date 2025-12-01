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
    # Implement solution here
    # pass
    pos = 50
    result = 0

    for line in input_data:
        direction, distance = line[:1], line[1:]
        dist = int(distance)

        if direction == "L":
            for _ in range(dist):
                pos -= 1
                if pos == 0:
                    result += 1
                if pos == -1:
                    pos = 99

        elif direction == "R":
            for _ in range(dist):
                pos += 1
                if pos == 100:
                    pos = 0
                if pos == 0:
                    result += 1

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
    print(f"Solution for Day 01, Part One: {result}")


if __name__ == "__main__":
    main()
