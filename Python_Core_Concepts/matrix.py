# Learing 2D arrays(Matrix) in python
# Programmer : Medi Assumani
# Task get each student :
        # highest score, lowest score, average
        # Find highest score in Science, English, History, Arts, and Maths

seniors = [['Roy',80,75,85,90,95],
           ['John',75,80,75,85,100],
           ['Dave',80,80,80,90,95],
           ['Medi',90,45,78,85,66],
           ['Mace',67,89,77,90,45],
           ['Patrcik',97,45,89,65,40]]

def find_student_average(student_name):
    average = 0.0
    for row in seniors:
        if seniors[row] == student_name:
            row = row + 1
            average += seniors[row]
        else:
            continue
        for col in seniors



#def find_student_lowest_score():
#def find_student_highest_score():
#def find_best_overall_performer():
#def find_overall_average()
# def get_student_name():
