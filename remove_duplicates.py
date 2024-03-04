input_file = 'duplicate_input.txt'
output_file = 'unique_output.txt'

# Read numbers from the input file
with open(input_file, 'r') as f:
    numbers = [int(line.strip()) for line in f]

# Remove duplicates using set() and sort the list
unique_numbers = sorted(set(numbers))

# Write unique numbers to the output file
with open(output_file, 'w') as f:
    for num in unique_numbers:
        f.write(str(num) + '\n')

print("Unique numbers have been written to", output_file)