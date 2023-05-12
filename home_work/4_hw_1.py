class Car:
    def __init__(self, color, type, year):
        self.color = color
        self.type = type
        self.year = year

    def start_engine(self):
        print('Автомобиль заведен')


    def stop_engine(self):
        print('Автомобиль заглушен')

    def year_of_car(self, a):
        self.year = a

    def type_of_car(self, a):
        self.type = a

    def color_of_car(self, a):
        self.color = a

    def __str__(self):
        return f'{self.color, self.type, self.year}'


audi = Car('black', 'suv', 2013)
print(audi)
audi.start_engine()
audi.stop_engine()
audi.year_of_car(2020)
audi.color_of_car('yellow')
audi.type_of_car('sedan')
print(audi)
