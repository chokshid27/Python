def sort_numbers(numbers):
    # Use bubble sort to sort the numbers
    n = len(numbers)
    for i in range(n):
        for j in range(0, n-i-1):
            if numbers[j] > numbers[j+1]:
                # Swap the numbers using pointers
                numbers[j], numbers[j+1] = numbers[j+1], numbers[j]

if __name__ == "__main__":
    # Test the sort_numbers function
    num_list = [64, 34, 25, 12, 22, 11, 90]
    print("Original List: ", num_list)
   
    # Pass the list to the function and sort it
    sort_numbers(num_list)
   
    # Print the sorted list
    print("Sorted List: ", num_list)
