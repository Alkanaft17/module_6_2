class Vehicle:

    __COLOR_VARIANTS = ['blue', 'red', 'green', 'black', 'white']

    def __init__(self, owner: str, __model: str, __color: str, __engine_power: int):
        self.owner = owner                   # владелец транспорта (владелец может меняться)
        self.__model = __model               # модель (марка) транспорта. (мы не можем менять название модели)
        self.__engine_power = __engine_power # мощность двигателя. (мы не можем менять мощность двигателя самостоятельно)
        self.__color = __color               #  название цвета. (мы не можем менять цвет автомобиля своими руками)

    def get_model(self):
        return f'Модель {self.__model}'

    def gef_horsepower(self):
        return f'Мощность двигателя: {self.__engine_power}'

    def get_color(self):
        return f'Цвет: {self.__color}'

    def print_info(self):
        print(self.get_model())
        print(self.gef_horsepower())
        print(self.get_color())
        print(f'Владелец: {self.owner}')

    def set_color(self, new_color: str):
        for i_color in self.__COLOR_VARIANTS:
            if i_color.lower() == new_color.lower():
                self.__color = new_color
                return
        print(f'Нельзя сменить цвет на {new_color}')




class Sedan(Vehicle):
    __PASSENGERS_LIMIT = 5 # в седан может поместиться только 5 пассажиров

# Текущие цвета __COLOR_VARIANTS = ['blue', 'red', 'green', 'black', 'white']
vehicle1 = Sedan('Fedos', 'Toyota Mark II', 'blue', 500)

# Изначальные свойства
vehicle1.print_info()

# Меняем свойства (в т.ч. вызывая методы)
vehicle1.set_color('Pink')
vehicle1.set_color('BLACK')
vehicle1.owner = 'Vasyok'

# Проверяем что поменялось
vehicle1.print_info()