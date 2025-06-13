# def fact(n):
#     if n == 0 or n == 1:
#         return 1
#     return fact(n-1) * n

# print(fact(5))


# #practice program 1
# def natural(n):
#     for i in range(0,n-1):
#         sum =  i + 



# def pattern(n):
#     for i in range(1, n + 1):
#         print("  " * (n - i), end="")
#         for j in range(1, i + 1):
#             print(j, end=" ")
#         for j in range(i - 1, 0, -1):
#             print(j, end=" ")
#         print()

# n = int(input("Enter levels: "))
# pattern(n)


# def fact(n):
#     result = 1
#     for i in range(2,n+1):
#         result = result * i
#     return result


# print(fact(5))



# n = 4
# f= 1
# for i in range(2,n+1):
#     f = f*i
# print(f)


# p = input("Enter the string or num: ")

# for i in range[:p:-1]:
#     i == p
#     print("plain")
# else:
#     print("not")






# def convert_string(input_string):
#     # Get input from the user
#    # input_string = input("Enter a string: ")

#     while True:
#         # Display the menu
#         print("\nMenu:")
#         print("1. Convert to Upper Case")
#         print("2. Convert to Lower Case")
#         print("3. Convert to Proper Case")
#         print("4. Swap Case")
#         print("5. Exit")

#         # Get the user's choice
#         choice = input("Enter your choice (1-5): ")

#         if choice == '1':
#             # Convert to Upper Case
#             print("Upper Case:", input_string.upper())
#         elif choice == '2':
#             # Convert to Lower Case
#             print("Lower Case:", input_string.lower())
#         elif choice == '3':
#             # Convert to Proper Case
#             print("Proper Case:", input_string.title())
#         elif choice == '4':
#             # Swap Case
#             print("Swap Case:", input_string.swapcase())
#         elif choice == '5':
#             # Exit the program
#             print("Exiting the program.")
#             break
#         else:
#             print("Invalid choice. Please select a valid option.")

# # Call the function to run the program
# convert_string(input("Enyer the string"))




def to_upper_case(s):
    result = ""
    for char in s:
        if 'a' <= char <= 'z':  # Check if the character is lowercase
            result += chr(ord(char) - 32)  # Convert to uppercase
        else:
            result += char  # Keep the character as is
    return result

def to_lower_case(s):
    result = ""
    for char in s:
        if 'A' <= char <= 'Z':  # Check if the character is uppercase
            result += chr(ord(char) + 32)  # Convert to lowercase
        else:
            result += char  # Keep the character as is
    return result

def to_proper_case(s):
    result = ""
    capitalize_next = True  # Flag to capitalize the first character of each word
    for char in s:
        if char == ' ':
            result += char  # Keep spaces as is
            capitalize_next = True  # Next character should be capitalized
        elif capitalize_next:
            result += to_upper_case(char)  # Capitalize the character
            capitalize_next = False  # Reset the flag
        else:
            result += to_lower_case(char)  # Lowercase the character
    return result

def swap_case(s):
    result = ""
    for char in s:
        if 'a' <= char <= 'z':
            result += to_upper_case(char)  # Convert to uppercase
        elif 'A' <= char <= 'Z':
            result += to_lower_case(char)  # Convert to lowercase
        else:
            result += char  # Keep the character as is
    return result

def convert_string():
    # Get input from the user
    input_string = input("Enter a string: ")

    while True:
        # Display the menu
        print("\nMenu:")
        print("1. Convert to Upper Case")
        print("2. Convert to Lower Case")
        print("3. Convert to Proper Case")
        print("4. Swap Case")
        print("5. Exit")

        # Get the user's choice
        choice = input("Enter your choice (1-5): ")

        if choice == '1':
            # Convert to Upper Case
            print("Upper Case:", to_upper_case(input_string))
        elif choice == '2':
            # Convert to Lower Case
            print("Lower Case:", to_lower_case(input_string))
        elif choice == '3':
            # Convert to Proper Case
            print("Proper Case:", to_proper_case(input_string))
        elif choice == '4':
            # Swap Case
            print("Swap Case:", swap_case(input_string))
        elif choice == '5':
            # Exit the program
            print("Exiting the program.")
            break
        else:
            print("Invalid choice. Please select a valid option.")

# Call the function to run the program
convert_string()