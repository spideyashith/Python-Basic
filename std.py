class student:
    def accept(self,name,regno):
        self.name = name
        self.regno = regno
    
    def display(self):
        print("Std name: ",self.name)
        print("regno: ",self.regno)
    
std = student()
n = input("Enter name: ")
r = int(input("Enter regno: "))
std.accept(n,r)

std.display()
       