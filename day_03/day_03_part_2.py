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
    result = 0

    for line in input_data:
        n = len(line)
        nums = []
        l_bound = -1

        # print(line)
        for i in range(n - 12, n):
            nums.append((int(line[i]), i))
        # print(nums)

        for i in range(12):
            for j in range(nums[i][1] - 1, l_bound, -1):
                # print(val, j, line[j])
                if int(line[j]) >= nums[i][0]:
                    nums[i] = (int(line[j]), j)
            l_bound = nums[i][1]
            # print(nums)

        result += int("".join([str(x[0]) for x in nums]))

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
    print(f"Solution for Day 03, Part One: {result}")


if __name__ == "__main__":
    main()
