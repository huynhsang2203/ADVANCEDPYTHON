def average(num1: float, num2: float):
    return (num1 + num2) / 2
n1 = float(input(":"))
n2 = float(input(":"))
while average(n1,n2)<5:
    print("Fail")
    print("re-input")
    n1= float(input("Repeat 1:"))
    n2 = float(input("Repeat 2:"))
print("Pass")