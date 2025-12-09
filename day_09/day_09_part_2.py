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


#     return True
class Point:
    def __init__(self, r, c, i):
        self.r = r
        self.c = c
        self.idx = i
        self.nr = -1
        self.nc = -1

    def __repr__(self):
        return f"P: ({self.r}, {self.c}) > ({self.nr}, {self.nc})"


def compress(points):
    points.sort(key=lambda p: (p.c, p.r))
    compressed = -1
    prev = -1

    for i, point in enumerate(points):
        if point.c > prev:
            compressed += 2
            prev = point.c
        point.nc = compressed

    points.sort(key=lambda p: (p.r, p.c))
    compressed = -1
    prev = -1

    for i, point in enumerate(points):
        if point.r > prev:
            compressed += 2
            prev = point.r
        point.nr = compressed


def write_grid_to_file(grid, file_path):
    with open(file_path, "w") as f:
        for row in grid:
            f.write("".join(row) + "\n")
    print(f"Grid written to: {file_path}")


def create_edges(points):
    points.sort(key=lambda p: p.idx)
    edges = [(points[-1], points[0])]
    for i in range(1, len(points)):
        edges.append((points[i - 1], points[i]))

    return edges


def create_grid(points, edges):
    h = max([p.nr for p in points]) + 2
    w = max([p.nc for p in points]) + 2

    # Create Grid
    grid = [["."] * (w) for r in range(h)]

    points.sort(key=lambda p: p.idx)

    for p1, p2 in edges:
        grid[p1.nr][p1.nc] = "#"

        # drow along cols axis
        if p1.nr == p2.nr:
            min_c, max_c = min(p1.nc, p2.nc), max(p1.nc, p2.nc)

            for new_c in range(min_c + 1, max_c):
                grid[p1.nr][new_c] = "X"

        # draw aloing row axis
        elif p1.nc == p2.nc:
            min_r, max_r = min(p1.nr, p2.nr), max(p1.nr, p2.nr)

            for new_r in range(min_r + 1, max_r):
                grid[new_r][p1.nc] = "X"
        else:
            print(p1, p2)
            print("This hsould never happen")

    return grid


def flood_fill(grid):
    h, w = len(grid), len(grid[0])
    outside_cells = set()
    q = collections.deque([(0, 0)])

    while q:
        r, c = q.popleft()
        grid[r][c] = "*"
        for nr, nc in [(r - 1, c), (r, c + 1), (r + 1, c), (r, c - 1)]:
            if not ((0 <= nr < h) and (0 <= nc < w)):
                continue

            if grid[nr][nc] != ".":
                continue

            if (nr, nc) in outside_cells:
                continue

            outside_cells.add((nr, nc))
            q.append((nr, nc))

    return outside_cells


def solve(input_data):
    points = []
    for i, line in enumerate(input_data):
        c, r = line.split(",")
        p = Point(int(r), int(c), i)
        points.append(p)

    n = len(points)

    compress(points)

    edges = create_edges(points)

    grid = create_grid(points, edges)

    outside_cells = flood_fill(grid)

    result = 0

    squares = []

    for i in range(n):
        p1 = points[i]
        for j in range(i + 1, n):
            p2 = points[j]

            min_r = min(p1.r, p2.r)
            max_r = max(p1.r, p2.r)
            min_c = min(p1.c, p2.c)
            max_c = max(p1.c, p2.c)

            squares.append((p1, p2, (max_r - min_r + 1) * (max_c - min_c + 1)))

    for square in squares:
        p1, p2, original_area = square

        if original_area < result:
            continue

        min_r = min(p1.nr, p2.nr)
        max_r = max(p1.nr, p2.nr)
        min_c = min(p1.nc, p2.nc)
        max_c = max(p1.nc, p2.nc)

        is_valid = True

        for r in range(min_r, max_r + 1):
            for c in range(min_c, max_c + 1):
                if (r, c) in outside_cells:
                    is_valid = False
                    break
            if not is_valid:
                break

        if is_valid:
            result = max(result, original_area)

    return result

    # # write grid to file for inspection
    # script_dir = os.path.dirname(os.path.abspath(__file__))
    # output_path = os.path.join(script_dir, "grid_output.txt")
    # write_grid_to_file(grid, output_path)


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
