class Student:
    def __init__(self,name,surname,fieldOfStudy):
        self.name = name
        self.surname = surname
        self.fielOfStudy = fieldOfStudy
        self.id = Student.id
        Student.id += 1

    id = 100000
    uni = "UEK Kraków"


    def __str__(self):
        return f"{self.name} {self.surname} ({self.id}), {self.fielOfStudy}, {self.uni}"

st1 = Student('Anna',"Maj","Applied Informatics")
print(st1)
st2 = Student('Izuku',"Midoriya","Hero Study")
print(st2)
st3 = Student('Max','Caulfield','Photography')
print(st3)