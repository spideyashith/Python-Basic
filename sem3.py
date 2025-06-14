# l = []

# n = int(input("Enter the number: "))
# for i in range(n):
#     e = int(input(f"Enetr the nummberss{i+1}: "))
#     l.append(e)

# #linear search

# s = int(input("Enter the number to be searched: "))

# found = False
# for f in l:
#      if f == s:
#          print("F")
#          found = True
#          break
# if not found:
#     print("NF")


def process_tuple(tup):
    # Step 1: Convert tuple to list so we can modify it
    num_list = list(tup)
    print("Initial list:", num_list)

    # Step 2: Add an element (we'll add 99 at the end)
    num_list.append(99)
    print("After appending 99:", num_list)

    # Step 3: Remove an element (we'll remove the first element)
    if num_list:  # Check if list is not empty
        removed = num_list.pop(0)
        print(f"Removed first element ({removed}):", num_list)

    # Step 4: Insert an element (we'll insert 55 at index 1)
    num_list.insert(1, 55)
    print("After inserting 55 at index 1:", num_list)

    # Step 5: Find the second-largest element
    unique_numbers = list(set(num_list))  # Remove duplicates
    unique_numbers.sort(reverse=True)     # Sort in descending order
    print("Sorted unique elements:", unique_numbers)

    if len(unique_numbers) >= 2:
        second_largest = unique_numbers[1]
        print("Second-largest element:", second_largest)
        return second_largest
    else:
        print("Not enough unique elements for second-largest.")
        return None

# Test the function
sample_tuple = (10, 20, 30, 40, 20)
result = process_tuple(sample_tuple)
print("Result:", result)
