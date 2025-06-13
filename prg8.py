class student:
    def __init__(self, regno, name, m1, m2, m3):
        self.regno = regno
        self.name = name
        self.m1 = m1
        self.m2 = m2
        self.m3 = m3
        
    def display(self):
        print("STUDENT DETAILS")
        print("Name: ", self.name)
        print("Reg No: ", self.regno)
        print("Marks in 3 subjects: ", self.m1, self.m2, self.m3)

std = student(101, "Rahul", 45, 46, 52)
std.display()
