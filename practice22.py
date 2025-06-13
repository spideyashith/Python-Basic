num = [25,8,45,6,45,7]

r = int(input("Enter the value to be searched: "))

for el in num:
    if(el == r):
        print("FOUND")
        break
    else:
        print("NOT FOUND")

