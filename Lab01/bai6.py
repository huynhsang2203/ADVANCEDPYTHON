def average_grade(grade1, grade2, grade3):
 """ (number, number, number) -> number
 Return the average of the grade1, grade2, and grade3, where
 each grade ranges from 0 to 100, inclusive.
 >>> average_grade(80, 95, 90)
 88.33333333333333
 """
 return (grade1 + grade2 + grade3) / 3
print(average_grade(80, 95, 90))
