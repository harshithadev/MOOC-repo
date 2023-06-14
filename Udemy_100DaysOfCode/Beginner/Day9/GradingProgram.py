def returngrade(mark):
    if(mark>90):
        grade = "Outstanding"
    elif(mark>80):
        grade = "Exceeds Expectations"
    elif(mark>70):
        grade = "Acceptable"
    else : 
        grade = "Fail"
    return grade
student_score = {
    "Harry" : 81,
    "Ron" : 78,
    "Hermione" : 99,
    "Droco" : 74,
    "Neville" : 62
}

for student in student_score:
    student_score[student] = returngrade(student_score[student])

print(student_score)