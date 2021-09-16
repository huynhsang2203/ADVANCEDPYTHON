import doctest
def average(num1: float, num2: float) -> float:
    return num1 + num2 / 2
print(average(5,20))
print(doctest.testmod())