dict = {"Name": "Rahul",
		 "ID": 101,
          "Course": "MSC"}
          

print(dict)
#Accesing The Dictionery
acess = dict.get("Name")
print("Accessed Dictioner is he: ",acess)


#Modifying the Dictionery
dict["Course"]= "MCA"
print(dict)