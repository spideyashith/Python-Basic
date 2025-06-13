n = int(input("how many elements you want to enter in list: "))
e = []
sum = 0

for i in range(n):
    r= int( input(f"Enter the element {i+1}: "))
    e.append(r)
    
a = tuple(e)
print(type(a))

for s in a:
    sum+=s

avg = sum // len(e)
print(f"The sum is {sum} The average is {avg}" )
