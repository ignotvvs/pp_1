import json

student = {
    "name": "Nathan Prescott",
    "dob": "29.08.1995",
    "city": "Arcadia Bay",
    "GPA": 3.7,
    "phone": [
        {"type": "home", "number": 5557063},
        {"type": "cellPhone", "number": 5551010}
    ]
}

with open("student.json","w") as file:
    json.dump(student,file,indent=4)
