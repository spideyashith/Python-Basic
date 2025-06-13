# s = {1,8,3,9,4}
# s1 = {5,1,2,7,4}

# print(s)
# print(s1)



# class Student:
#     def __init__(self,name,reg_no):
#         self.name = name;
#         self.reg_no = reg_no;
        
#     def display(self):
#         print("Student Details")
#         print("The Name of student: ",self.name)
#         print("The Name of student: ",self.reg_no)
        
# std = Student("Ash",123)
# std1 = Student("Rahul",147)
# std.display()
# std1.display()
        

# text = "Hello, welcome to the world  welcome of Python."
# # index = text.rfind("welcome")
# # print(index)  # Output: 7

# # s = text.replace("welcome", "bye",2)

# s = text.split(' ,',8)
# print(s)

class Employee:
   'Common base class for all employees'
   def __init__(self, name, age):
      self.name = name
      self.age = age

e1 = Employee("Bhavana", 24)
e2 = Employee("Bharat", 25)

print ("Name: ", e1.name)
print ("age: ",e1.age)
print ("Name: {}".format(e2.name))
print ("age: {}".format(e2.age))