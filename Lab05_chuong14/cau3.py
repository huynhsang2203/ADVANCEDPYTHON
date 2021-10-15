class Student:
    def __init__(self, fname, lname, mail, number):
        self.fname = fname
        self.lname = lname
        self.mail = mail
        self.number = number
    def __str__(self) -> str:
        return '{} {}\n{}\n{}'.format(self.fname, self.lname, self.mail, self.number)
student = Student('Paul','Ajax', 'pgries@cs.toronto.edu', '1234')
print(student.__str__())
