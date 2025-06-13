# # # Parent class
# # class Animal:
# #     def __init__(self, name, hungry):
# #         self.name = name  # Initialize the name attribute
# #         self.hungry = hungry  # Initialize the hungry attribute
        
# #     def is_hungry(self):
# #         return self.hungry  # Method to check if the animal is hungry

# #     def speak(self):
# #         pass  # Placeholder method to be overridden by child classes

# # # Child class inheriting from Animal
# # class Dog(Animal):
# #     def speak(self):
# #         return f"{self.name} barks!"  # Override the speak method
    
# #     def hungry_status(self):
# #         if self.is_hungry():
# #             return f"{self.name} is hungry."
# #         else:
# #             return f"{self.name} is not hungry."

# # # Creating instances of Dog
# # dog = Dog("Buddy", True)  # True indicates that Buddy is hungry
# # d = Dog("Tommy", False)  # False indicates that Tommy is not hungry

# # print(dog.speak())
# # print(dog.hungry_status())
# # print(d.speak())
# # print(d.hungry_status())




# # Function to calculate the area of a rectangle
# def calculate_rectangle_area(length, width):
# 	# Assertion to check that the length and width are positive
# 	assert length > 0 and width > 0, "Length and width"+ \
#                     	"must be positive"
# 	# Calculation of the area
# 	area = length * width
# 	# Return statement
# 	return area


# # Calling the function with positive inputs
# area1 = calculate_rectangle_area(5, 6)
# print("Area of rectangle with length 5 and width 6 is", area1)

# # Calling the function with negative inputs
# area2 = calculate_rectangle_area(-5, 6)
# print("Area of rectangle with length -5 and width 6 is", area2)









# f = open("sample.txt","w")

# for i in range(5):
#     n = input("Enter tthe name: ")
#     f.write(n)
#     f.write("\n")

#
# f.close()


# import numpy as np
# n = np.array([1,2,3,4])
# print(n.shape)


i = 15
j =10
