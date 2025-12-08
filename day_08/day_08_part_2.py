import collections
import math
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


class Box:
    def __init__(self, id: int, x: int, y: int, z: int):
        self.id = id
        self.x = x
        self.y = y
        self.z = z

    def get_dist(self, neighbor: "Box"):
        return math.sqrt(
            (self.x - neighbor.x) ** 2
            + (self.y - neighbor.y) ** 2
            + (self.z - neighbor.z) ** 2
        )

    def __repr__(self):
        return f"Box= id: {self.id}, x: {self.x}, y: {self.y}, z: {self.z}"


class UnionFind:
    def __init__(self, n):
        self.par = {}  # stores the parent of the tree
        self.rank = {}  # this is essentially the height of the tree

        # init each node as its own parent with a rank of 0
        for i in range(n):
            self.par[i] = i
            self.rank[i] = 0

    # Find parent of n, with path compression.
    def find(self, n):
        p = self.par[n]
        while p != self.par[p]:
            self.par[p] = self.par[self.par[p]]
            p = self.par[p]
        return p

    # Union by height / rank.
    # Return false if already connected, true otherwise.
    def union(self, n1, n2):
        p1, p2 = self.find(n1), self.find(n2)
        if p1 == p2:
            return False

        if self.rank[p1] > self.rank[p2]:
            self.par[p2] = p1
        elif self.rank[p1] < self.rank[p2]:
            self.par[p1] = p2
        else:
            self.par[p1] = p2
            self.rank[p2] += 1
        return True

    def count_components(self):
        roots = []
        for i in self.par.keys():
            root = self.find(i)
            roots.append(root)

        size_counter = collections.Counter(roots)
        sizes = list(size_counter.values())

        return len(sizes)

    def __repr__(self):
        return f"UnionFind({self.par})"


def solve(input_data):
    boxes = []

    for i, line in enumerate(input_data):
        pos = line.split(",")
        box = Box(i, int(pos[0]), int(pos[1]), int(pos[2]))
        boxes.append(box)

    n = len(boxes)
    comparisons = []

    for i in range(n):
        for j in range(i + 1, n):
            box_a, box_b = boxes[i], boxes[j]
            dist = box_a.get_dist(box_b)
            comparisons.append((dist, box_a, box_b))

    comparisons.sort()

    uf = UnionFind(n)
    for _, box_a, box_b in comparisons:
        uf.union(box_a.id, box_b.id)
        if uf.count_components() == 1:
            return box_a.x * box_b.x


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
    print(f"Solution for Day 08, Part One: {result}")


if __name__ == "__main__":
    main()
