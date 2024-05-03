from random import choice, randint, uniform
from fractions import Fraction
import math


def quadratic_equation_16639():
    """Генератор аналогичных задач 16638-16640 https://kuzovkin.info/one_exercise_1/16339:
       Решите уравнение: (5⋅x+1)⋅(2⋅x−3)=(10⋅x−3)⋅(x+1)"""
    data = list(range(-10, 0)) + list(range(1, 11))
    k, m, n = (choice(data) for _ in range(3))
    p = Fraction(k * m, n)
    k1, m1, n1, p1 = (choice(data) for _ in range(4))
    b = k * m1 + m * k1 - p * n1 - n * p1
    c = k1 * m1 - n1 * p1
    answer = str(-c / b)

    equal = f'Решите уравнение: \\(({k}\\cdot x {"+" if k1 >= 0 else "-"} {abs(k1)})\\cdot ' \
            f'({m}\\cdot x{"+" if m1 >= 0 else "-"} {abs(m1)})=' \
            f'({n}\\cdot x{"+" if n1 >= 0 else "-"} {abs(n1)})\\cdot ' \
            f'({p}\\cdot x{"+" if p1 >= 0 else "-"} {abs(p1)})\\)'

    return {
        "condition": equal,
        "answer": answer
    }


def equation_17524():
    """Генератор аналогичной задачи 17524 https://kuzovkin.info/one_exercise_1/17524"""
    k, z, y = (randint(2, 5) for _ in range(3))
    b = randint(1, 10)
    while not (b ** 2 - 4 * y * k) in tuple(i ** 2 for i in range(13)):
        b = randint(1, 10)
    descr = b ** 2 - 4 * y * k
    answer = f'x = {-b / 2}' if descr == 0 else (f'x1 = {(-b + math.sqrt(descr)) / 2}', f'x2 = {(-b - math.sqrt(descr)) / 2}')
    return {
        "condition": f'Решить уравнение: \( \lg \left ( {z ** y}*\sqrt[{k}]' + "{" + str(z) + '^{x^{2}'
                     + f'{"+" if b >= 0 else "-"}{abs(b)}' + "x}} \right )=0 \)",
        "answer": answer
    }


def equation_16616():
  """Генератор аналогичной задачи  16616 https://kuzovkin.info/one_exercise_1/16616:
  Решите уравнение: (x−2)⋅(x−3)−(x+2)⋅(x−5)=0"""
  data = list(range(-10, 0)) + list(range(1, 11))
  a, b, c, d = (choice(data) for _ in range(4))
  while (a + b - c - d) == 0:
      a, b, c, d = (choice(data) for _ in range(4))
  answer = str(Fraction((c * d - a * b), (a + b - c - d)))
  return {
      "condition": f'\((x{"+" if a >= 0 else "-"}{abs(a)})\cdot (x{"+" if b >= 0 else "-"}{abs(b)})-' 
                   f'(x{"+" if c >= 0 else "-"}{abs(c)})\cdot (x{"+" if d >= 0 else "-"}{abs(d)})=0\)',
      "answer": answer
  }


def equation_10244():
    """ Аналогичная задача https://kuzovkin.info/one_exercise_1/10244:
    Найдите значение выражени: (2,6−1,04):0,24⋅0,8"""
    a, b, c, d = (round(uniform(0.1, 5), 2) for _ in range(4))
    answer = round(((a - b) / c * d), 2)
    return {
        "condition": f'Найдите значение выражения, округленное до 2 цифры после запятой: \(\left ( {a}-{b}' + r"\right"
                     + f'):{c}\cdot {d}\)',
        "answer": answer
    }
