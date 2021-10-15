class Country:
    def __init__(self, name, population, area):
        self.name = name
        self.population = population
        self.area = area
    #Khai báo từng dòng biến
    def __str__(self):
        return '%s + %s + %s' % (self.name, self.population, self.area) #return chuỗi
    def is_larger(self, other):
        return self.area > other.area
    def population_density(self):
        return self.population / self.area #tính mật độ dân số
    def __str__(self):
        return '{} có dân số là {} triệu dân và có diện tích khoảng {} km vuông.'.format(self.name, self.population, self.area)
    def __repr__(self):
        return "Country('{0}',{1},{2})".format(self.name, self.population, self.area)
x = Country('Canada', 34482779, 9984670)
canada = Country('Canada', 34482779, 9984670)
usa = Country('United States of America', 313914040, 9826675)
#a
print('Thông tin:')
print('Cách 1')
print(x)
print('Cách 2')
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
print('                                                  Câu 2')
class Continent(Country):
    def __init__(self, name, countries):
        self.name = name
        self.countries = countries
    def review(self):
        num = 0
        for country in north_america.countries:
            num+=1
            print(country)
            #print(num)
        return country
    def total_population(self):
        total = 0
        for country in north_america.countries:
            total = total + country.population
        return (total)
    pass
mexico = Country('Mexico', 112336538, 1943950)
countries = [canada, usa, mexico]
north_america = Continent('North America', countries)
print(mexico)
print(north_america.name)
print(north_america.total_population())
print(north_america.review())