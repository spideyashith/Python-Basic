# class shape:
#     def area(self):
#         return None

# class Rectangle(shape):
#     def __init__(self, w, l):
#         self.w = w
#         self.l = l

#     def area(self):
#         return self.l * self.w

# class circle(shape):
#     def __init__(self, r):
#         self.r = r

#     def area(self):
#         return 3.14 * (self.r ** 2)

# rect = Rectangle(5, 10)
# print("The area of rectangle is", rect.area())

# c = circle(9)
# print("The area of circle is: ", c.area())






# try:
#     n= int(input("Enter the number: "))
#     print(n)
# except ValueError:
#     print("Invalid input")




# def get_integer(
    
# ):
#     while True:
#         try:
#             user_input = int(input("Please enter an integer: "))
#             return user_input
#         except ValueError:
#             print("That's not a valid integer. Please try again.")









try:
    n = int(input("Enter the number "))
    assert n % 2 == 0
    print("Even")
except AssertionError:
    print("Odd value")      










