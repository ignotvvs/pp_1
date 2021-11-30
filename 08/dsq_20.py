import json
a = []
with open('students.json') as file,open('limited.json','w') as file2:
    st = json.load(file)
    for i in st:
        dict = i.copy()
        for k in i.keys():
            if k != "first_name" and k != "last_name" and k != "studentID":
                dict.pop(k)
        a.append(dict)
    json.dump(a,file2,indent=4)


