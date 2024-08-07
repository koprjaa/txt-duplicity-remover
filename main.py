# Set the input and output file paths
original_file_path = 'set_your_input_path_here.txt'
new_file_path = 'set_your_output_path_here.txt'

# Dictionary to count occurrences of each line
line_counts = {}

# Read the original file and count line occurrences
try:
    with open(original_file_path, 'r', encoding='utf-8', errors='replace') as file:
        for line in file:
            stripped_line = line.strip()
            line_counts[stripped_line] = line_counts.get(stripped_line, 0) + 1
except UnicodeDecodeError as e:
    print(f"Error reading file: {e}")

# Identify unique lines
unique_lines = set(line_counts.keys())

# Log and remove duplicates
print("Duplicate removal log:")
for line, count in line_counts.items():
    if count > 1:
        print(f'"{line}" was removed {count-1} times.')

# Write the unique lines to a new file
try:
    with open(new_file_path, 'w', encoding='utf-8') as file:
        for line in sorted(unique_lines):
            file.write(f"{line}\n")
except UnicodeEncodeError as e:
    print(f"Error writing file: {e}")

print(f"Unique lines have been written to {new_file_path}.")
