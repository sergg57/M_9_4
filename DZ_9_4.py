#Lambda-функция
first = 'Мама мыла раму'
second = 'Рамена мало было'

print(list(map(lambda x, y: x == y, first, second)))

# Замыкание
def get_advanced_writer(file_name):

    def write_everything(*data_set):
        with open(file_name, 'a') as file:
            for data in data_set:
                file.write(f'{data}' +'\n')

    return write_everything

writer = get_advanced_writer('example.txt')
writer('Это строчка', ['А', 'это', 'уже', 'число', '5', 'в', 'списке'])

# Метод __call__
from random import choice

class MysticBall:

    def __init__(self, *words):
        self.words = words


    def __call__(self):
        return choice(self.words)

        #print(f'{choice(self.words)}')

first_ball =  MysticBall('Да', 'Нет', 'Наверное')
print(first_ball())
print(first_ball())
print(first_ball())
