# def max_min(num):
#     max = num[0]
#     min = num[0]
    
#     for i in num:
#         if i > max:
#             max = i
#         if i < min:
#             min = i
#     return max , min

# num = [5,9,7,4,2,8]
# max_v, min_v = max_min(num)
# print("l",num)
# print("MAX",max_v)
# print("MIN",min_v)
    
 
 
print("-----------------------Menu-----------------------")
print("1.Uppercase")
print("2.lowercase")
print("3.Propercase")
print("4.Swapcase")
print("5.Exit...")

s = input("Enter tthe string: ")

while True:
    ch = int(input("Enter the number: "))
    
    if ch == 1:
        print("Upper: ",s.upper())
    elif ch == 2:
        print("Lower: ",s.lower())
    elif ch == 3:
        print("Proper: ",s.title())
    elif ch == 4:
        print("Swap: ",s.swapcase())
    elif ch == 5:
        print("Exit....")
        break
    else: 
        print("Invalid")

    
    
    
