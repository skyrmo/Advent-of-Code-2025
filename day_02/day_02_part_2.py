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


def get_factors(n):
    factors = []
    for i in range(1, int(n**0.5) + 1):
        if n % i == 0:
            factors.append(i)
            if i != n // i:
                factors.append(n // i)
    return sorted(factors)[:-1]


def check(num: str):
    n = len(num)
    factors = get_factors(n)

    # print(num, n, factors)

    is_repeated = False

    for factor in factors[::-1]:
        is_repeated = True
        for i in range(factor):
            for j in range(1, n // factor):
                tgt_idx = i + j * factor
                if num[i] != num[tgt_idx]:
                    is_repeated = False
                    break

            if not is_repeated:
                break

        if is_repeated:
            return True

    return is_repeated


def solve(input_data):
    result = 0

    for rng in input_data:
        s, e = rng.split("-")
        start, end = int(s), int(e)

        for i in range(start, end + 1):
            i_str = str(i)
            if check(i_str):
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
