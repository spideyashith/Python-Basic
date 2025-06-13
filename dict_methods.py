student = {
    "name": "Rahul",
    "subject" : {
        "c/c++": 52,
        "java": 60,
        "Web design": 42
    }
}

print(list(student.keys()))

print(list(student.values()))

print(list(student.items()))

keys = student.get("subject")

print(keys)

new_dict = {"course" : "Msc", "name": "Brain"}
student.update(new_dict)
print(new_dict)

print(student.pop("name"))