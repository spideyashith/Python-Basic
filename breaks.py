x = (5,9,4,3,85,41,6)

y = 3
i = 0

while i < len(x):
    if(x[i] == y):
        print("Found",i)
        break
    else:
        print("Not Found")
        i+=1
