n = int(input("Enter the nummber: "))
s = int(input("Enter another number: "))

try:
    a = n/s
    print(a)
except Exception as e:
    print(f" {e}")
finally:
    print("the code reached to end")