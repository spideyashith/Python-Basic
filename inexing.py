# str = "Alloysius"

# print(str[8])

# print(str[2:6])

# print(str[0:len(str)])

# print(str[5:])
# print(str[:5])



# print(str[-3:-1])



# a = "AIMIT"

# rev = "" 

# for i in a:
#     rev = i + rev

# print(rev)




# m = [5, 8, 9, 3, 6, 7]

# max_digit = 0
# min_value = 0  # Initialize min to 0

# # Finding the maximum digit
# for number in m:
#     while number > 0:
#         r = number % 10
#         if r > max_digit:
#             max_digit = r
#         number = number // 10

# # Finding the minimum value in the list
# for number in m:
#     if number < min_value or min_value == 0:  # Check if min_value is still 0
#         min_value = number

# print("Maximum digit:", max_digit)
# print("Minimum value:", min_value)



# def min_max(num):

#     max = num[0]
#     min = num[0]

#     for n in num:
#         if n > max:
#             max = n
#         if n < min:
#             min = n
    
#     return max,min

# m = [5,9,6,8,7,4,5,5]
# min ,max = min_max(m)


# print("max",max)
# print("min",min)














# l = [10,20,30,40,50,60,70]

# u = int(input("Enter the number: "))

# found = False
# for index in range(len(l)):
#     if l[index] == u:
#         found = True
#         break


# if found:
#     print(f"Number {u} is found at index {index}")
# else:
#     print("Not found")



def count_vowels_consonants_blanks(input_string):
    vowels = "aeiouAEIOU"
    num_vowels = 0
    num_consonants = 0
    num_blanks = 0

    for char in input_string:
        if char.isalpha():  # Check if the character is a letter
            if char in vowels:
                num_vowels += 1
            else:
                num_consonants += 1
        elif char == ' ':
            num_blanks += 1

    return num_vowels, num_consonants, num_blanks

# Example usage
input_string = input("Enter a string: ")
vowels, consonants, blanks = count_vowels_consonants_blanks(input_string)

print(f"Total Vowels: {vowels}")
print(f"Total Consonants: {consonants}")
print(f"Total Blanks: {blanks}")