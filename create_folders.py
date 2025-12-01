import os


def create_aoc_project_structure():
    # Create project structure for days 1 through 25.
    # Template for the Python script
    def get_script_template(day, part):
        return f"""
import os
import collections

def parse_input(file_path):
    # Parse the input file
    with open(file_path, 'r') as file:
        # Read the entire file
        data = file.read().strip()

        # 2. Read as a list of lines
        # return data.split('\\n')

        # 3. Read as a list of integers
        # return [int(line) for line in data.split('\\n')]

        # 4. Read as a list of lists (e.g., for grid-like inputs)
        # return [list(line) for line in data.split('\\n')]

        return data

def solve(input_data):
    # Implement solution here
    pass

def main():
    # Get the directory of the current script
    script_dir = os.path.dirname(os.path.abspath(__file__))

    # Construct the input file path relative to the script's location
    input_path = os.path.join(script_dir, 'input.txt')

    # Parse input
    parsed_input = parse_input(input_path)

    # Solve and print the solution
    result = solve(parsed_input)
    print(f"Solution for Day {day}, Part {part}: {{result}}")

if __name__ == '__main__':
    main()
"""

    # Create .gitignore at the project root
    with open(".gitignore", "w") as gitignore:
        gitignore.write("""# Ignore input text files for each day
**/input.txt
# Python bytecode
**pycache**/
*.py[cod]
# Virtual environment
venv/
.venv/
env/
# IDE specific files
.vscode/
.idea/
*.sublime-project
*.sublime-workspace
# Rope project settings
.ropeproject/
""")

    # Create structure for days 1-25
    for day in range(1, 13):
        # Use zero-padding for day numbers
        padded_day = f"{day:02d}"

        # Create day folder
        day_folder = f"day_{padded_day}"
        os.makedirs(day_folder, exist_ok=True)

        # Create Python files for part one
        part_one_file = os.path.join(day_folder, f"day_{padded_day}_part_1.py")
        with open(part_one_file, "w") as f:
            f.write(get_script_template(padded_day, "One"))

        # Create Python files for part two
        part_two_file = os.path.join(day_folder, f"day_{padded_day}_part_2.py")
        with open(part_two_file, "w") as f:
            f.write(get_script_template(padded_day, "Two"))

        # Create a placeholder input.txt in the day folder
        with open(os.path.join(day_folder, "input.txt"), "w") as f:
            f.write("# Paste your Advent of Code input here")

    print("Advent of Code project structure created successfully!")


# Run the function to create the structure
if __name__ == "__main__":
    create_aoc_project_structure()
