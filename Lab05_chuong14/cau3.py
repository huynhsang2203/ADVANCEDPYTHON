class Student:
    def __init__(self, fname, lname, mail, number):
        self.fname = fname
        self.lname = lname
        self.mail = mail
        self.number = number
    def __str__(self) -> str:
        return '{} {}\n{}\n{}'.format(self.fname, self.lname, self.mail, self.number)
    def __init__(self1, k1, k2, k3, k4, k5):
        self1.k1 = k1
        self1.k2 = k2
        self1.k3 = k3 
        self1.k4 = k4
        self1.k5 = k5
    def __repr__(self1) -> str:
        return "KH('{0}','{1}','{2}','{3}','{4}')".format(self1.k1, self1.k2, self1.k3, self1.k4, self1.k5)
    pass
student = Student('Paul','Ajax', 'pgries@cs.toronto.edu', '1234')
khoahoc = Student('Anh', 'Toan', 'Li', 'Hoa', 'Van', 'Lag')
print(student.__str__())
print(khoahoc.__repr__())
