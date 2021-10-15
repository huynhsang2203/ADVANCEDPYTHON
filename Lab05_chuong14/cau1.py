class Country:
    def __init__(self, name, population, area):
        self.name = name
        self.population = population
        self.area = area               #Khai báo từng dòng biến
    def is_larger(self, other):
        return self.area > other.area
    def population_density(self):
        return self.population / self.area #tính mật độ dân số
    def __str__(self):
        return '{} có dân số là {} triệu dân và có diện tích khoảng {} km vuông.'.format(self.name, self.population, self.area)
    def __repr__(self):
        return "Country('{0}',{1},{2})".format(self.name, self.population, self.area)
canada = Country('Canada', 34482779, 9984670)
usa = Country('United States of America', 313914040, 9826675)
#a
print('Thông tin:')
print(canada.name)
print(canada.population)
print(canada.area)
#b
print('Diện tích Canada lớn hơn Mĩ?')
print(canada.is_larger(usa))
print('Diện tích Mĩ lơn hơn Canada?')
print(usa.is_larger(canada))
#c
print('Mật độ dân số của Canada là:')
print(canada.population_density())
print('Mật độ dân số của Mĩ là:')
print(usa.population_density())
#d
print('Review')
print(usa)
print(canada)
#e
print(canada.__repr__())
print([canada])
print('************************************************************************************************************')
