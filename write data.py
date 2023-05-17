import os

# Get the current working directory
cwd = os.getcwd()

# Construct the full file path to input.txt
input_file_path = os.path.join(cwd, "path/to/input.txt")
# open the input file in read mode
with open("input.txt", "r") as input_file:
    # read the data from the file
    data = input_file.read()

# manipulate the data (e.g. convert to uppercase)
data = data.upper()

# open the output file in write mode
with open("output.txt", "w") as output_file:
    # write the manipulated data to the file
    output_file.write(data)

print("Data has been read from input.txt, converted to uppercase, and written to output.txt.")

