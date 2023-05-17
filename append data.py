filename = "example.txt"  # replace with the name of your file

# Open the file in append mode
with open(filename, "a") as f:
    # Ask the user to enter data to append to the file
    data = input("Enter data to append: ")
    # Write the data to the file
    f.write(data + "\n")
    # Close the file
    f.close()
