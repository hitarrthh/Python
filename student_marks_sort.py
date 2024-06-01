def total(student):
    return student['math'] + student['physics'] + student['chem']

students = [
    {'NAME:':'HITARTH', 'ID: ':60009220209, 'math: ':91, 'physics: ':90, 'chem: ':98},
    {'NAME:':'HITANSHU', 'ID: ':60009220208, 'math: ':19, 'physics: ':23, 'chem: ':98},
    {'NAME:':'JAY', 'ID: ':60009220207, 'math: ':95, 'physics: ':70, 'chem: ':68},
    {'NAME:':'AAYISHI', 'ID: ':60009220202, 'math: ':71, 'physics: ':92, 'chem: ':88},
    {'NAME:':'DELANIE', 'ID: ':60009220201, 'math: ':97, 'physics: ':60, 'chem: ':58},
]
students.sort(key=lambda student: total(student), reverse=True)

print("STUDENTS IN DECENDING ODER ON MARKS ARE LISTED BELOW:")
for student in students:
    print(f"NAME: {student['NAME']},TOTAL MARKS: {total(student)}")