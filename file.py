# # f = open('myfile1.txt','a')
# # f.write("Hello world")
# # f.write("Add this line")
# # # text  = f.read()
# # # print(text)
# # f.close()



# file = open("Employees.txt", "w") 

# for i in range(3): 
#     name = input("Enter the name of the employee: ") 
#     file.write(name) 
#     file.write("\n") 
	
# file.close() 

# print("Data is written into the file.") 




# file1 = open("Employees.txt", "w") 
# lst = [] 
# for i in range(3): 
# 	name = input("Enter the name of the employee: ") 
# 	lst.append(name + '\n') 
	
# file1.writelines(lst) 
# file1.close() 
# print("Data is written into the file.") 




f = open("sample.txt","r")
print(f.tell())
f.read(6)
print(f.tell())
f.close()