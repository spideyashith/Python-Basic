# f = open("practice.txt","r")

# data = f.read()

# new_data = data.replace("java", "Python")
# print(new_data)




# # f.write("Hi everyone \n we are learning file i\o \n  using java. \n I like programing in java ")
# f.close()




# f = open("practice.txt","w")
# f.write(new_data)

# f.close()


word = "learning"
with open("practice.txt","r") as f:
    data = f.read()
    #if data.find(word) != -1:
    if word in data:
        print("found")
    else:
        print("Not found")