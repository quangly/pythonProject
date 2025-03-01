import os

# Function to split the file
def split_file(file_path, num_parts):
    # Get the file size in bytes
    file_size = os.path.getsize(file_path)
    part_size = file_size // num_parts

    with open(file_path, 'r') as file:
        # Read the header
        header = file.readline()

        part_number = 1
        part_file = open(f"part{part_number}-{file_path}", 'w')
        part_file.write(header)

        current_size = len(header)

        for line in file:
            line_size = len(line)
            # If the current part exceeds the size limit, start a new file
            if current_size + line_size > part_size and part_number < num_parts:
                part_file.close()
                part_number += 1
                part_file = open(f"part{part_number}-{file_path}", 'w')
                part_file.write(header)
                current_size = len(header)

            # Write the line to the current part
            part_file.write(line)
            current_size += line_size

        # Close the last part file
        part_file.close()

# File path and number of parts
file_path = "mock_users.csv"
num_parts = 5

# Split the file
split_file(file_path, num_parts)

print(f"File split into {num_parts} parts successfully.")
