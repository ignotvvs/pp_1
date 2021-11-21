import csv

with open('students.txt') as file:
    students = csv.reader(file)
    count = 0
    for i in students:
        if count == 0:
            count+=1
            continue
        if int(i[2]) < 30:
            print(f"{i[0]}  {i[1]}  {i[len(i)-1]}")
        count+=1