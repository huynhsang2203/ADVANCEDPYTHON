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
        return ''
    def total_population(self):
        total = 0
        for country in north_america.countries:
            total = total + country.population
        return (total)
    def review_1(self):
        res = north_america.name
        for country in north_america.countries:
            print(res + '\n'+ str(country))
        return res
    pass
mexico = Country('Mexico', 112336538, 1943950)
countries = [canada, usa, mexico]
north_america = Continent('North America', countries)
#a
print(mexico)
print(north_america.name)
#b
print('Tổng cư dân 3 nước Mĩ, Canada và Mexico là: ')
print(north_america.total_population())
#c
print(north_america.review())
print(north_america.review_1())
