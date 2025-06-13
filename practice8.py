n1 = int(input("Enter the 1st number: "))
n2 = int(input("Enter the 2nd number: "))
n3 = int(input("Enter the 3rd number: "))
n4 = int(input("Enter the 4th number: "))

if (n1 >= n2 and n1 >= n3 and n1 >= n4):
    print("N1 is the greatest")
elif (n2 >= n3 and n2 >= n4):
    print("N2 is the greatest")
elif (n3 >= n4):
    print("N3 is the greatest")
else:
    print("N4 is the greatest")