import collections
import os


def parse_input(file_path):
    # Parse the input file
    with open(file_path, "r") as file:
        # Read the entire file
        data = file.read().strip()

        # 2. Read as a list of lines
        sections = data.split("\n\n")

        shapes = []
        shape_section_end = 0
        for i, section in enumerate(sections):
            if ":" in section and "x" in section.split(":")[0]:
                # This is a region line, not a shape
                shape_section_end = i
                break

            # Parse shape
            lines = section.strip().split("\n")
            shape_grid = [list(line) for line in lines[1:]]
            shapes.append(shape_grid)

        # Parse regions
        regions = []
        for section in sections[shape_section_end:]:
            for line in section.split("\n"):
                if ":" in line:
                    parts = line.split(":")
                    dims = parts[0].strip().split("x")
                    width, height = int(dims[0]), int(dims[1])
                    counts = [int(x) for x in parts[1].strip().split()]
                    regions.append((width, height, counts))

        return shapes, regions


def get_shape_cells(shape):
    """Get list of (row, col) positions where shape has '#'."""
    cells = []
    for r, row in enumerate(shape):
        for c, char in enumerate(row):
            if char == "#":
                cells.append((r, c))
    return cells


def normalize_cells(cells):
    """Normalize cells so minimum row and col are 0."""
    if not cells:
        return []
    min_r = min(r for r, c in cells)
    min_c = min(c for r, c in cells)
    return tuple(sorted((r - min_r, c - min_c) for r, c in cells))


def get_all_orientations(shape):
    """Generate all unique orientations (rotations and flips) of a shape."""
    cells = get_shape_cells(shape)
    orientations = set()

    # Original
    orientations.add(normalize_cells(cells))

    # Rotations (90, 180, 270 degrees)
    for _ in range(3):
        cells = [(c, -r) for r, c in cells]
        orientations.add(normalize_cells(cells))

    # Flip horizontally
    cells = get_shape_cells(shape)
    cells = [(r, -c) for r, c in cells]
    orientations.add(normalize_cells(cells))

    # Rotations of flipped
    for _ in range(3):
        cells = [(c, -r) for r, c in cells]
        orientations.add(normalize_cells(cells))

    # Flip vertically
    cells = get_shape_cells(shape)
    cells = [(-r, c) for r, c in cells]
    orientations.add(normalize_cells(cells))

    # Rotations of vertically flipped
    for _ in range(3):
        cells = [(c, -r) for r, c in cells]
        orientations.add(normalize_cells(cells))

    return list(orientations)


def solve(shapes, regions):
    n = len(regions)
    result = 0

    for i in range(n):
        region = regions[i]
        area = region[0] * region[1]
        # print(region[0], region[1], area)

        area_2 = sum(region[2]) * 7
        if area > area_2:
            result += 1
        print(area, area_2, area > area_2)

    return result


def main():
    # Get the directory of the current script
    script_dir = os.path.dirname(os.path.abspath(__file__))

    # Construct the input file path relative to the script's location
    input_path = os.path.join(script_dir, "input.txt")
    # input_path = os.path.join(script_dir, "sample_input.txt")

    # Parse input
    shapes, regions = parse_input(input_path)

    # Solve and print the solution
    result = solve(shapes, regions)
    print(f"Solution for Day 12, Part One: {result}")


if __name__ == "__main__":
    main()
