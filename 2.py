from math import sqrt

message:str = ('Добро пожаловать в самую лучшую программу для вычисления '
               'квадратного корня из заданного числа')
print (message)


def CalculateSquareRoot (Number: int ) -> int:
    """ Вычисляет квадратный корень"""
    return sqrt(Number)


def calc(your_number) :
    if your_number<=0:
        return       
    root = 0
    print(f'Мы вычислили квадратный корень' 
          f'из введённого вами числа. Это будет: {CalculateSquareRoot(your_number)}')


print(message)
calc (25.5)