while True:
     e  = input("Enter the charcter: ")

    print("menue")
    print("1.Upper")
    print("2.lower")
    print("3.Proper")
    print("4.Swap")
    print("5.exit...")

ch = int(input("Enter the choice: "))

if ch ==1:
    print(e.upper())
elif ch == 2:
    print(e.lower())
elif ch == 3:
    print(e.title())
elif ch == 4:
    print("e.swapcase()")
elif ch == 5:
    print("Exit...")
else:
    print("Invalid ")

