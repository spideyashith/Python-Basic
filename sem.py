s = int(input())
e = int(input())

for i in range(s,e+1):
    if i > 1:
        for j in range(2,i):
            if i % j == 0:
                break
        else:
            print(i,end=" \n")
print("-----------------------------------------------")
a,b =0,1
while a<=e:
    if a >= s:
        print(a,end=" ")
    a,b = b , a+b
