# Tup = (1,2.5,"Hello")

# print(Tup)

# s = 2.5

# if s in Tup:
#     print("f")
# else:
#     print("NF")
# n = int(input("Enter number of elements: "))

# nu = []

# # Collect input numbers
# for i in range(n):
#     it = int(input(f"Enter number {i+1}: "))
#     nu.append(it)

# print("Input numbers:", nu)

# # Initialize lists for odd, even, and zero
# odd = []
# even = []
# zero = []

# # Classify numbers into odd, even, and zero
# for i in nu:
#     if i == 0:
#         zero.append(i)
#     elif i % 2 == 0:
#         even.append(i)
#     else:
#         odd.append(i)

# # Output results
# print("Odd numbers:", odd)
# print("Even numbers:", even)
# print("Zeros:", zero)

# print("Count of odd numbers:", len(odd))
# print("Count of even numbers:", len(even))
# print("Count of zeros:", len(zero))







l = [1,2,3,4,9,7]

s = int(input())
f = False

for i in l:
    if i == s:
        print("F",i)
        f = True
    
if not f:
    print("NF")    
