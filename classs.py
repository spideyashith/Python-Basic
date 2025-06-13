# class student:
#     n = "Ash"
    
# s = student()
# print(s.n)


class car:
    company_name = "Global Car pvt ltd"
    def __init__(self,carname, regdate):
        self.n = carname
        self.r = regdate
        print("Car details")


c1 = car("BMW",24-12-2003)
print(c1.n, c1.r)
print(c1.company_name)

c2 = car("Audi",24-5-2022)
print(c2.n,c2.r)

print(car.company_name)

#object attribute as more precedings that class attribute
#obj.attr > class.attr

        
        