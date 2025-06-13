l  = [5,9,8,7,4,3]

n = int(input("Enter the number to search: "))
found = False

for i in l:
    if(i == n):
        print("Found")
        found = True
        break


if not found:
    print("Not found")
