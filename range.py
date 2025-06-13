# # # # for i in range(8): #(stop)
# # # #     print(i)



# # # # for i in range(2,8): #(start,stop)
# # # #     print(i)



# # # for i in range(2,8,2): #(start,stop,step)
# # #     print(i)


# # def sum_and_average_tuple(numbers):
# #     total = sum(numbers)
# #     average = total / len(numbers) 
# #     return total, average

# # def sum_and_average_list(numbers):
# #     total = sum(numbers)
# #     average = total / len(numbers) 
# #     return total, average

# # # Input for tuple
# # tuple_input = input("Enter numbers for tuple (comma-separated): ")
# # tuple_numbers = tuple(map(int, tuple_input.split(',')))
# # tuple_sum, tuple_average = sum_and_average_tuple(tuple_numbers)
# # print("Tuple - Sum:", tuple_sum, "Average:", tuple_average)

# # # Input for list
# # list_input = input("Enter numbers for list (comma-separated): ")
# # list_numbers = list(map(int, list_input.split(',')))
# # list_sum, list_average = sum_and_average_list(list_numbers)
# # print("List - Sum:", list_sum, "Average:", list_average)



# def main():
#     filename = 'text_file.txt'
    
#     # Get the number of lines to insert
#     n = int(input("Enter the number of lines you want to insert: "))
    
#     # Create and write to the text file
#     with open(filename, 'w') as file:
#         for i in range(n):
#             line = input(f"Enter line {i + 1}: ")
#             file.write(line + '\n')
    
#     # Read and display the contents of the file
#     with open(filename, 'r') as file:
#         contents = file.read()
#         print("\nContents of the file:")
#         print(contents)
    
#     # Count lines, words, and characters
#     num_lines = contents.count('\n')   # Count lines
#     num_words = len(contents.split())      # Count words
#     num_characters = len(contents)         # Count characters

#     # Display the counts
#     print("\nStatistics:")
#     print(f"Number of lines: {num_lines}")
#     print(f"Number of words: {num_words}")
#     print(f"Number of characters: {num_characters}")

# if __name__ == "__main__":
#     main()


limit = int(input("ENter the number: "))  # You can change this limit to find more perfect numbers

for num in range(2, limit + 1):
    divisors_sum = 0
    for i in range(1, num // 2 + 1):
        if num % i == 0:
            divisors_sum += i
            
    if divisors_sum == num:
        print(num)