import os

# import collections
from collections import defaultdict, deque


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


def topological_sort(adj):
    # Find all nodes
    all_nodes = set(adj.keys())
    for neighbors in adj.values():
        all_nodes.update(neighbors)

    # Calculate in-degrees
    in_degree = {node: 0 for node in all_nodes}
    for node in adj:
        for neighbor in adj.get(node, []):
            in_degree[neighbor] += 1

    # Start with nodes that have no incoming edges
    queue = deque([node for node in all_nodes if in_degree[node] == 0])
    topo_order = []

    while queue:
        node = queue.popleft()
        topo_order.append(node)

        for neighbor in adj.get(node, []):
            in_degree[neighbor] -= 1
            if in_degree[neighbor] == 0:
                queue.append(neighbor)

    return topo_order


def solve(input_data):
    adj = {}

    for line in input_data:
        key = line.split(":")[0]
        values = line.split(":")[1].strip().split(" ")
        if key in adj:
            print("There are duplicate keys")
        adj[key] = values

    # Get topological order
    topo_order = topological_sort(adj)

    dp: dict[tuple[str, bool, bool], int] = defaultdict(int)
    dp[("svr", False, False)] = 1

    # Process nodes in topological order
    for node in topo_order:
        for seen_fft in [False, True]:
            for seen_dac in [False, True]:
                state = (node, seen_fft, seen_dac)

                if dp[state] == 0:
                    continue  # No paths reach this state

                path_count = dp[state]

                # Update flags for outgoing edges
                new_seen_fft = seen_fft or (node == "fft")
                new_seen_dac = seen_dac or (node == "dac")

                # Propagate to neighbors
                for nbr in adj.get(node, []):
                    new_state = (nbr, new_seen_fft, new_seen_dac)
                    dp[new_state] += path_count

    return dp[("out", True, True)]


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
    print(f"Solution for Day 11, Part One: {result}")


if __name__ == "__main__":
    main()
