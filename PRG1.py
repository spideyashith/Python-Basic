T1 = (1, 2, "ABC", 3.14, True)

for i in T1:
    print(i)

search_element = "ABC"

if search_element in map(str, T1):
    print("FOUND")
else:
    print("NOT FOUND")
   
    