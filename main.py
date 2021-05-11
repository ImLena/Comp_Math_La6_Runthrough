import logic


def input_params():
    print('Выберите уравнение:\n'
          '1. y\'\' +  x^(-2) y\' + x^3 y = e^x\n'
          '2. y\'\' + x^2 y\' + 2y  = 2x - 1\n')
    t = float(input())
    print('Введите концы промежутка через пробел (хa xb)')
    xa, xb = input().split()
    print('Введите начальные условия через пробел (ya уb)')
    ya, yb = input().split()
    print('Введите точность')
    h = float(input())
    return float(xa), float(xb), float(ya), float(yb), h, t


xa, xb, ya, yb, h, t = input_params()
logic.runthrough(xa, xb, ya, yb, h, t)
