from typing import ClassVar


class Student:
    def __init__(self, fname, lname, mail, phone):
        self.fname = fname
        self.lname = lname
        self.mail = mail
        self.phone = phone 
    def __repr__(self) -> str:
        return 'Full Name: {} {} \nMail: {} \nPhone: {}'.format(self.fname, self.lname, self.mail, self.phone)
    pass
student = Student('Huynh','Sang','187it21136@vanlanguni.vn','0906256058')
print(student.__repr__())
print('********************************BBBBBBBBBBBBB****************************')
class Faculty:
  def __init__(self, industry: str, ID_industry: str, mail: str ):
    self.industry = industry
    self.ID_industry = ID_industry
    self.mail = mail
  def __repr__(self):
    return('Chuyên nghành: {} \nKhoa: {} \nMail: {}'.format(self.industry, self.ID_industry, self.mail))
classFaculty = Faculty('Công nghệ phần mềm', 'Công nghệ thông tin', '187IT21136@vanlanguni.vn')
print(classFaculty.__repr__())
print('*******************************CCCCCC********************************')
class Member:
    def __init__(self, name, listMember) -> None:
        self.name = name 
        self.listMember = listMember
    def __repr__(self) -> str:
        return 'Name: {} \nDS Member: {}'.format(self.name, self.listMember)
    pass
listMember = ['Ronaldo', 'Kaka', 'Rooney']

member = Member('Python Nang Cao', listMember)
print(member.listMember)
print(member.__repr__())