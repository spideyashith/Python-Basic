f = open("myfile.txt","w")

n = int(input("Enter the number of lines: "))
for i in range(n):
    l = input("Enter the lines: ")
    f.write(l + "\n")
f.close()

f = open("myfile.txt","r")
txt = f.read()
print("content inside the file")
print(txt)
f.close()


Lines = txt.splitlines()
words = txt.split()

chr = 0
for j in txt:
    if j.isalpha():
        chr+=1


print("--------------------------------------------")
print("Lines: ",len(Lines))
print("words: ",len(words)) 
print("Character: ",chr)