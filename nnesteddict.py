#nested dictioner

student = {
    "name": "Rahul",
    "subject" : {
        "c/c++": 52,
        "java": 60,
        "Web design": 42
    }
}


print(student)

print(student["subject"])

print(student["subject"]["java"])