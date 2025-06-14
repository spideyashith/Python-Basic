l = []

n = int(input("Enter the number: "))
for i in range(n):
    e = int(input(f"Enetr the nummberss{i+1}: "))
    l.append(e)

#linear search

s = int(input("Enter the number to be searched: "))

found = False
for f in l:
     if f == s:
         print("F")
         found = True
         break
if not found:
    print("NF")
         
