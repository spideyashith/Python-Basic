# def line_check():
#     word = "learning"
#     data = True
#     line_no = 1
#     with open("practice.txt","r") as f:
#         while data:
#             data = f.readline()
#             if word in data:
#                 print(line_no)
#                 return
#             line_no+=1
#     return -1

# line_check()
            
            
            
with open("practice.txt","r") as f:
    data =  f.read()
    if (data % 2 ==0):
        print("Even")
    else:
        print("odd")


