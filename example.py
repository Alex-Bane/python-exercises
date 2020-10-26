def grade_calc(score):
    grade_perc = float((score/175) * 100)
    
    if grade_perc >= 70:
        return "Your grade_perc score is:", grade_perc,
        "Your grade is an A"
    elif grade_perc >= 60:
        return ('Your grade_perc score is:', grade_perc,'Your grade is a B')
        
    elif grade_perc >= 50:
        return "Your grade_perc score is:", grade_perc,"Your grade is an C"
        
    elif grade_perc >= 40:
        return "Your grade_perc score is:", grade_perc
        "Your grade is an D"
    else:
     return "Your grade_perc score is:", grade_perc,
     "You have failed"

hwk = int(input("Input your homework score:"))
asessment = int(input("Input your assesment score:"))
exam = int(input("Input your exam score:"))

final_grade = grade_calc(hwk + asessment + exam)
print(final_grade)