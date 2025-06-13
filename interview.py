# a = "4"
# b = "77"

# c = int(a) + int(b)

# print(c)


# a  = 6
# b = 9

# if(a < b):
#     print(True)
# else:
#     print(False)



# s = frozenset(["cat" ,"dog", "elephant"])
# print("monkey" or s)


# a = 100
# b = -120

# c = 2.5

# d = 4 + 5j
# e = -5j

# print(a,b,c,d,e)


# a = r"c:/user/ashit"
# print(a)


# a = [1,2,3]
# b = [1,2,3]

# print(a is b)

# num1 = 5
# num2 = 5

# print(num1 is num2)

# print(id(num1))
# print(id(num2))



# a = 70
# m = True

# if a >= 50:
#     if m:
#         print("30%")
#     else:
#         print("50%")
# else:
#     print("not")


 
# li = ["geeks", "for", "geeks"] 
# for i in li: 
#     print(i) 

     
# d = dict({'x':123, 'y':354}) 
# for i in d: 
#     print("%s  %d" % (i, d[i])) 


     
# s = "Geeks" 
# for i in s: 
#     print(i) 

# for letter in 'geeksforgeeks': 
 
#     if letter == 'e' or letter == 's': 
#         break 
 
# print('Current Letter :', letter)


 
# for letter in 'geeksforgeeks': 
#     pass 
# # print('Last Letter :', letter)


# #del statement: Deletes an element at a specified index. 
# a = [10, 20, 30, 40, 50] 
 
# # Removes the first occurrence of 30 
# a.remove(30)   
# print("After remove(30):", a) 
 
# # Removes the element at index 1 (20) 
# popped_val = a.pop(1)   
# print("Popped element:", popped_val) 
# print("After pop(1):", a)  
 
# # Deletes the first element (10) 
# del a[0]   
# print("After del a[0]:", a) 



# a = [1, 2, 3, 4, 5, 6, 7, 8, 9] 
 
# # Get the entire list using negative step 
# b = a[::-1] 
# print(b) 


# s = "gfg"

# s1 = s + s[0]
# print(s1)


# s = "geeksforGeeks" 
 
# # Trying to change the first character raises an error 
# # s[0] = 'I'  # Uncommenting this line will cause a TypeError 
 
# # Instead, create a new string 
# s = "G" + s[1:]
# del s 
# print(s)



# #To update a part of a string we need to create a new string since strings are immutable. 
# s = "hello geeks" 
# # Updating by creating a new string 
# s1 = "H" + s[1:] 
# # replacnig "geeks" with "GeeksforGeeks" 
# s2 = s.replace("geeks", "GeeksforGeeks") 
# print(s1) 
# print(s2)


# tup = 5,8,9

# print(type(tup))




# items = [5,10,11,6,8]
# n = bytearray(items)
# print(n)
# n[0] = 6
# print(n[0])


# import keyword
# print(keyword.kwlist)



# Using floor division operator
# numerator = 15
# denominator = 4
# quotient = numerator // denominator
# print("Quotient:", quotient)


 
x = 30
y = 20 
list = [10, 20, 30, 40, 50] 
 
if (x not in list): 
    print("x is NOT present in given list") 
else: 
    print("x is present in given list") 
 
if (y in list): 
    print("y is present in given list") 
else: 
    print("y is NOT present in given list")