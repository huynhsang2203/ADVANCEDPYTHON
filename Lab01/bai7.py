def top_three_avg(grade1, grade2, grade3, grade4):
 """ (number, number, number, number) -> number
 Return the average of the top three of grades grade1, grade2,
 grade3, and grade4.
 >>> top_three_avg(50, 60, 70, 80)
 70
 """
 # Here is one solution that does not use average_grade from Q6.
 total = grade1 + grade2 + grade3 + grade4
 top_three = total - min(grade1, grade2, grade3, grade4)
 return top_three / 3
 # Here is a different solution that does use the function from Q6.
 return max(average_grade(grade1, grade2, grade3),
 average_grade(grade1, grade2, grade4),
 average_grade(grade1, grade3, grade4),
 average_grade(grade2, grade3, grade4))
 return (grade1 + grade2 + grade3) / 3
print(top_three_avg(50, 60, 70, 80))