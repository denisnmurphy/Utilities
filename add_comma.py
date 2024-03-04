# Open the input file in read mode
input_file = 'input.txt'
output_file = 'output.txt'

with open(input_file, 'r') as f_in:
    # Read all lines from the input file
    lines = f_in.readlines()

# Open the output file in write mode
with open(output_file, 'w') as f_out:
    # Iterate over each line
    for line in lines:
        # Add a comma to the end of the line
        line_with_comma = line.rstrip('\n') + ',\n'
        # Write the modified line to the output file
        f_out.write(line_with_comma)

print("Commas added to the end of each line in the file.")