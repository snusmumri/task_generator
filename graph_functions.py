import matplotlib.pyplot as plt
from random import randint, choice
import numpy as np
import math as m
import decimal as d
from sympy import Point, Line, solve
from sympy.abc import x, y

def plot():# Функция создает координатную ось
  fig = plt.figure()
  ax = plt.axes()
  fig.add_axes(ax)
  ax.spines[["left", "bottom"]].set_position('zero')
  ax.spines[["top", "right"]].set_visible(False)
  ax.plot(1, 0, ">k", transform=ax.get_yaxis_transform(), clip_on=False)
  ax.plot(0, 1, "^k", transform=ax.get_xaxis_transform(), clip_on=False)
  plt.xticks(np.arange(-30, 30, 1), fontsize=8)
  plt.yticks(np.arange(-30, 30, 1), fontsize=8)
  ax.grid(True)
  arrow_length = 10
  ax.annotate('x', xy=(1, 0), xycoords=('axes fraction', 'data'),
              xytext=(0, arrow_length), textcoords='offset points',
              ha='center', va='bottom')
  ax.annotate('y', xy=(0, 1), xycoords=('data', 'axes fraction'),
              xytext=(arrow_length, 0), textcoords='offset points',
              ha='center', va='bottom')
  return fig, ax


def scatter(x_point, y_point): # Функция ставит точки на графике
  if float(y_point).is_integer():
      plt.scatter(x_point, y_point, c='black')

# Задача 1 №509213 c сайта https://math-ege.sdamgia.ru/problem?id=509213
# пересечение двух прямых
def input_parameters():
  while True:
    x1, y1, x2, y2, x3, y3, x4, y4 = np.random.randint(-8, 9, size=8)
    p1, p2, p3, p4 = Point(x1, y1), Point(x2, y2), Point(x3, y3), Point(x4, y4)
    if p1 != p2 and p2 != p3 and p3 != p4 and p1 != p4:
      l1, l2 = Line(p1, p2), Line(p3, p4)
      int_point = l1.intersection(l2)
      try:
        if int_point != []:
          x_int = int_point[0][0]
          y_int = int_point[0][1]
          if (x_int % 0.025 == 0 or x_int % 0.03125 == 0) and (y_int % 0.03125 == 0 or y_int % 0.025 == 0) and (x_int > 9 or x_int < -9) and (y_int > 9 or y_int < -9):
            x = np.linspace(-9, 9, 50)
            y_first = (((x-x1)*(y2-y1))/(x2-x1)) + y1
            y_second = (((x-x3)*(y4-y3))/(x4-x3)) + y3
            x_int, y_int  = [(int(param) if (float(param).is_integer()) else float(param)) for param in (x_int, y_int)]
            break
      except TypeError:
        pass
  return x, y_first, y_second, x_int, y_int, x1, y1, x2, y2, x3, y3, x4, y4


def function_graph(x, y_first, y_second, x1, y1, x2, y2, x3, y3, x4, y4):
    """Функция стоит две прямые по переданным параметрам"""
    fig, ax = plot()
    ax.plot(x, y_first)
    ax.plot(x, y_second)
    plt.ylim(-9, 9)
    plt.xlim(-9, 9)
    plt.scatter(x1, y1, c='blue')
    plt.scatter(x2, y2, c='blue')
    plt.scatter(x3, y3, c='red')
    plt.scatter(x4, y4, c='red')
    plt.show()


def function_result ():
    """Функция генерирует задание, выводит правильный ответ и график"""
    x, y_first, y_second, x_int, y_int, x1, y1, x2, y2, x3, y3, x4, y4 = input_parameters()
    task_random = randint(0,1)
    if task_random == 1:
        task = f'На рисунке изображены графики двух линейных функций. Найдите ординату точки пересечения графиков.' #ордината - y
        answer = y_int
    else:
        task = f'На рисунке изображены графики двух линейных функций. Найдите абциссу точки пересечения графиков.'  # абцисса - x
        answer = x_int
    solution = None
    def paint():
        function_graph(x, y_first, y_second, x1, y1, x2, y2, x3, y3, x4, y4)
    return answer, task, paint, solution


# Задача 2 https://math-ege.sdamgia.ru/problem?id=509259
# Пересечение двух парабол
def input_parameters():
  """Функция формирует точки, через которые строятся 2 параболы"""
  while True:
    a1, b1, c1 = symbols('a1 b1 c1')
    a2, b2, c2 = symbols('a2 b2 c2')
    a1, b1, c1, a2, b2, c2  = np.random.randint(-6, 7, size=6)
    if a1 != 0 and b1 != 0 and c1 !=0 and a2 != 0 and b2 != 0 and c2 !=0:
      eq1 = Eq(a1*x**2 + b1*x + c1, y)
      eq2 = Eq(a2*x**2 + b2*x + c2, y)
      solution = solve([eq1, eq2], [x, y], dict=True)
      if len(solution) == 2:
        x_int_1, y_int_1, x_int_2, y_int_2 = solution[0].get(x), solution[0].get(y), solution[1].get(x), solution[1].get(y)
        if (x_int_1 % 0.025 == 0 or x_int_1 % 0.03125 == 0) and (x_int_2 % 0.025 == 0 or x_int_2 % 0.03125 == 0) and (y_int_1 % 0.025 == 0 or y_int_1 % 0.03125 == 0) and (y_int_2 % 0.025 == 0 or y_int_2 % 0.03125 == 0):
          if ((y_int_2 > 20 or y_int_2 < -20) and (-10 < y_int_1 < 10)) or ((y_int_1 > 20 or y_int_1 < -20) and (-10 < y_int_2 < 10)):
            break
  x_coord = np.linspace(-15, 15, 250)
  y_first = a1 * x_coord ** 2 + b1 * x_coord + c1
  y_second = a2 * x_coord ** 2 + b2 * x_coord + c2
  x_int_1, y_int_1, x_int_2, y_int_2 = [(int(param) if (float(param).is_integer()) else float(param)) for param in (x_int_1, y_int_1, x_int_2, y_int_2)]
  return x_coord, y_first, y_second, x_int_1, y_int_1, x_int_2, y_int_2, a1, b1, c1, a2, b2, c2

def function_graph(x, y_first, y_second, point_A, a1, b1, c1, a2, b2, c2):
    """Функция стоит две параболы по переданным параметрам"""
    fig, ax = plot()
    ax.plot(x, y_first)
    ax.plot(x, y_second)
    plt.xlim(point_A[0] - 10, point_A[0] + 10)
    plt.ylim(point_A[1] -10, point_A[1] + 10)
    for x_point in range(-10, 10, 1):
      y_point_1 = a1 * x_point ** 2 + b1 * x_point + c1
      y_point_2 = a2 * x_point ** 2 + b2 * x_point + c2
      scatter(x_point, y_point_1)
      scatter(x_point, y_point_2)
    plt.scatter(point_A[0], point_A[1], color='black', s=15)
    plt.text(point_A[0] + 0.3, point_A[1] + 0.3, 'A', fontsize=18)
    plt.show()


def function_result():
    """Функция генерирует задание, выводит правильный ответ и график"""
    x_coord, y_first, y_second, x_int_1, y_int_1, x_int_2, y_int_2, a1, b1, c1, a2, b2, c2 = input_parameters()

    def signs_of_digits():
      digits = (a1, b1, c1, a2, b2, c2)
      str_digits = []
      for digit in digits:
        if str(digit).find("-") != -1:
          digit =  ' ' + ((str(digit))[0]) + ' ' + ((str(digit))[1:])
        else:
          digit =  ' + ' + (str(digit))[0:]
        str_digits.append(digit)
      equation2 = f'g(x)= {a2}x^2{str_digits[4]}x{str_digits[5]}'
      if a1 == 1:
          equation1 = f'f(x)= x^2{str_digits[1]}x{str_digits[2]}'
      elif a1 == -1:
        equation1 = f'f(x)= -x^2{str_digits[1]}x{str_digits[2]}'
      else:
        equation1 = f'f(x)= {a1}x^2{str_digits[1]}x{str_digits[2]}'
      return str_digits, equation1, equation2

    tr_digits, equation1, equation2 = signs_of_digits()

    if y_int_2 > 10 or y_int_2 < -10:
      point_B = [x_int_2, y_int_2]
      point_A = [x_int_1, y_int_1]
    else:
      point_A = [x_int_2, y_int_2]
      point_B = [x_int_1, y_int_1]
    solution = None
    task_random = randint(0,1)
    if task_random == 1:
      answer = point_B[1]
      axis = f'ординату'
    else:
      answer = point_B[0]
      axis = f'абциссу'
    task = f'На рисунке изображены графики функций \({equation1}\) и \(g(x) = ax^2 + bx + c\), которые пересекаются в точках A и B. Найдите {axis} точки B.'

    def paint():
        function_graph(x_coord, y_first, y_second, point_A, a1, b1, c1, a2, b2, c2)
    return answer, task, paint, solution


# Задача 3 №562285 c сайта https://math-ege.sdamgia.ru/problem?id=562285
# Парабола вида y = a * x ** 2 + b * x + c
def input_parameters():
    """Функция формирует две точки, через которые строится парабола"""
    while True:
        x1, y1, x2, y2 = np.random.randint(-4, 5, size=4) #parabola_vertex = (x1, y1) #parabola_point = (x2, y2)
        if (x2 - x1) != 0 and (y2 - y1) !=0:
            a = (y2 - y1) / ((x2 - x1) ** 2)
            if float(a).is_integer():
              a = int(a)
              if a != 0:
                b = int(-2 * a * x1)
                c = int(y2 - a * x2 ** 2 - b * x2)
                x = np.linspace(x1 - 3, x1 + 3, 100)
                y = a * x ** 2 + b * x + c
                break
    return x, y, a, b, c, x1, y1, x2, y2


def function_graph_parabola(x, y, a, b, c, x1, y1):
    """Функция стоит параболу по переданным параметрам"""
    fig, ax = plot()
    ax.plot(x, y)
    if a > 0:
        plt.ylim((y1 - 2), (y1 + 8))
    else:
        plt.ylim((y1 - 8), (y1 + 2))
    plt.xlim((x1 - 5), (x1 + 5))
    for x_point in range(x1 - 3, x1 + 3):
        y_point = a * x_point ** 2 + b * x_point + c
        scatter(x_point, y_point)
    plt.show()

def function_result():
  """Функция генерирует задание, выводит правильный ответ и график"""
  x_task = randint(-5, 5)
  x, y, a, b, c, x1, y1, x2, y2 = input_parameters()
  answer = int(a * x_task ** 2 + b * x_task + c)
  task = f'Вычислите \(f({x_task})\) для функции вида \(f(x) = ax^2 + bx + c\)'
  def paint():
    function_graph_parabola(x, y, a, b, c, x1, y1)

  if x1 >= 0:
    if y1 >= 0:
      if b >= 0:
        if c >= 0:
          solution = f'Из рисунка видно, что вершина параболы расположена в точке \(x0 = {x1}\), при этом при \(y0 = f(x) = {y1}\). Следовательно, \(f(x) = a(x - {x1})^2 + {y1}\), заметим, что \(f({x2}) = {y2}\), откуда \(a = {a}, b = {b}, c = {c}\). Значит \(f(x) = {a}x^2 + {b}x + {c}\), а \(f({x_task}) = {answer}\))'
        else:
          solution = f'Из рисунка видно, что вершина параболы расположена в точке \(x0 = {x1}\), при этом при \(y0 = f(x) = {y1}\). Следовательно, \(f(x) = a(x - {x1})^2 + {y1}\), заметим, что \(f({x2}) = {y2}\), откуда \(a = {a}, b = {b}, c = {c}\). Значит \(f(x) = {a}x^2 + {b}x - {abs(c)}\), а \(f({x_task}) = {answer}\))'
      else:
        if c >= 0:
          solution = f'Из рисунка видно, что вершина параболы расположена в точке \(x0 = {x1}\), при этом при \(y0 = f(x) = {y1}\). Следовательно, \(f(x) = a(x - {x1})^2 + {y1}\), заметим, что \(f({x2}) = {y2}\), откуда \(a = {a}, b = {b}, c = {c}\). Значит \(f(x) = {a}x^2 - {abs(b)}x + {c}\), а \(f({x_task}) = {answer}\))'
        else:
          solution = f'Из рисунка видно, что вершина параболы расположена в точке \(x0 = {x1}\), при этом при \(y0 = f(x) = {y1}\). Следовательно, \(f(x) = a(x - {x1})^2 + {y1}\), заметим, что \(f({x2}) = {y2}\), откуда \(a = {a}, b = {b}, c = {c}\). Значит \(f(x) = {a}x^2 - {abs(b)}x - {abs(c)}\), а \(f({x_task}) = {answer}\))'
    else:
      if b >= 0:
        if c >= 0:
          solution = f'Из рисунка видно, что вершина параболы расположена в точке \(x0 = {x1}\), при этом при \(y0 = f(x) = {y1}\). Следовательно, \(f(x) = a(x - {x1})^2 - {abs(y1)}\), заметим, что \(f({x2}) = {y2}\), откуда \(a = {a}, b = {b}, c = {c}\). Значит \(f(x) = {a}x^2 + {b}x + {c}\), а \(f({x_task}) = {answer}\))'
        else:
          solution = f'Из рисунка видно, что вершина параболы расположена в точке \(x0 = {x1}\), при этом при \(y0 = f(x) = {y1}\). Следовательно, \(f(x) = a(x - {x1})^2 - {abs(y1)}\), заметим, что \(f({x2}) = {y2}\), откуда \(a = {a}, b = {b}, c = {c}\). Значит \(f(x) = {a}x^2 + {b}x - {abs(c)}\), а \(f({x_task}) = {answer}\))'
      else:
        if c >= 0:
          solution = f'Из рисунка видно, что вершина параболы расположена в точке \(x0 = {x1}\), при этом при \(y0 = f(x) = {y1}\). Следовательно, \(f(x) = a(x - {x1})^2 - {abs(y1)}\), заметим, что \(f({x2}) = {y2}\), откуда \(a = {a}, b = {b}, c = {c}\). Значит \(f(x) = {a}x^2 - {abs(b)}x + {c}\), а \(f({x_task}) = {answer}\))'
        else:
          solution = f'Из рисунка видно, что вершина параболы расположена в точке \(x0 = {x1}\), при этом при \(y0 = f(x) = {y1}\). Следовательно, \(f(x) = a(x - {x1})^2 - {abs(y1)}\), заметим, что \(f({x2}) = {y2}\), откуда \(a = {a}, b = {b}, c = {c}\). Значит \(f(x) = {a}x^2 - {abs(b)}x - {abs(c)}\), а \(f({x_task}) = {answer}\))'
  else:
    if y1 >= 0:
      if b >= 0:
        if c >= 0:
          solution = f'Из рисунка видно, что вершина параболы расположена в точке \(x0 = {x1}\), при этом при \(y0 = f(x) = {y1}\). Следовательно, \(f(x) = a(x + {abs(x1)})^2 + {y1}\), заметим, что \(f({x2}) = {y2}\), откуда \(a = {a}, b = {b}, c = {c}\). Значит \(f(x) = {a}x^2 + {b}x + {c}\), а \(f({x_task}) = {answer}\))'
        else:
          solution = f'Из рисунка видно, что вершина параболы расположена в точке \(x0 = {x1}\), при этом при \(y0 = f(x) = {y1}\). Следовательно, \(f(x) = a(x + {abs(x1)})^2 + {y1}\), заметим, что \(f({x2}) = {y2}\), откуда \(a = {a}, b = {b}, c = {c}\). Значит \(f(x) = {a}x^2 + {b}x - {abs(c)}\), а \(f({x_task}) = {answer}\))'
      else:
        if c >= 0:
          solution = f'Из рисунка видно, что вершина параболы расположена в точке \(x0 = {x1}\), при этом при \(y0 = f(x) = {y1}\). Следовательно, \(f(x) = a(x + {abs(x1)})^2 + {y1}\), заметим, что \(f({x2}) = {y2}\), откуда \(a = {a}, b = {b}, c = {c}\). Значит \(f(x) = {a}x^2 - {abs(b)}x + {c}\), а \(f({x_task}) = {answer}\))'
        else:
          solution = f'Из рисунка видно, что вершина параболы расположена в точке \(x0 = {x1}\), при этом при \(y0 = f(x) = {y1}\). Следовательно, \(f(x) = a(x + {abs(x1)})^2 + {y1}\), заметим, что \(f({x2}) = {y2}\), откуда \(a = {a}, b = {b}, c = {c}\). Значит \(f(x) = {a}x^2 - {abs(b)}x - {abs(c)}\), а \(f({x_task}) = {answer}\))'
    else:
      if b >= 0:
        if c >= 0:
          solution = f'Из рисунка видно, что вершина параболы расположена в точке \(x0 = {x1}\), при этом при \(y0 = f(x) = {y1}\). Следовательно, \(f(x) = a(x + {abs(x1)})^2 - {abs(y1)}\), заметим, что \(f({x2}) = {y2}\), откуда \(a = {a}, b = {b}, c = {c}\). Значит \(f(x) = {a}x^2 + {b}x + {c}\), а \(f({x_task}) = {answer}\))'
        else:
          solution = f'Из рисунка видно, что вершина параболы расположена в точке \(x0 = {x1}\), при этом при \(y0 = f(x) = {y1}\). Следовательно, \(f(x) = a(x + {abs(x1)})^2 - {abs(y1)}\), заметим, что \(f({x2}) = {y2}\), откуда \(a = {a}, b = {b}, c = {c}\). Значит \(f(x) = {a}x^2 + {b}x - {abs(c)}\), а \(f({x_task}) = {answer}\))'
      else:
        if c >= 0:
          solution = f'Из рисунка видно, что вершина параболы расположена в точке \(x0 = {x1}\), при этом при \(y0 = f(x) = {y1}\). Следовательно, \(f(x) = a(x + {abs(x1)})^2 - {abs(y1)}\), заметим, что \(f({x2}) = {y2}\), откуда \(a = {a}, b = {b}, c = {c}\). Значит \(f(x) = {a}x^2 - {abs(b)}x + {c}\), а \(f({x_task}) = {answer}\))'
        else:
          solution = f'Из рисунка видно, что вершина параболы расположена в точке \(x0 = {x1}\), при этом при \(y0 = f(x) = {y1}\). Следовательно, \(f(x) = a(x + {abs(x1)})^2 - {abs(y1)}\), заметим, что \(f({x2}) = {y2}\), откуда \(a = {a}, b = {b}, c = {c}\). Значит \(f(x) = {a}x^2 - {abs(b)}x - {abs(c)}\), а \(f({x_task}) = {answer}\))'

  return answer, task, paint, solution


# Задача 4 https://math-ege.sdamgia.ru/problem?id=562061
# Парабола вида y = (x ** 2) / a + b * x + c
def input_parameters():
    """Функция формирует две точки, через которые строится парабола"""
    while True:
      x1, y1 = np.random.randint(-3, 4, size=2)
      x2, y2 = np.random.randint(x1 - 5, x1 + 6, size=2)
      #parabola_vertex = (x1, y1) #parabola_point = (x2, y2)
      if (x2 - x1) != 0 and (y2 - y1) !=0:
        a = ((y2 - y1) / ((x2 - x1) ** 2))
        if a != 0 and a > -1 and a < 1 and float(1/a).is_integer():
          b = -2 * a * x1
          c = y2 - a * x2 ** 2 - b * x2
          x = np.linspace(x1 - 6, x1 + 6, 400)
          y = a * x ** 2 + b * x + c
          break
    return x, y, a, b, c, x1, y1, x2, y2


def function_graph_parabola(x, y, a, b, c, x1, y1, x2, y2):
    """Функция стоит параболу по переданным параметрам"""
    fig, ax = plot()
    ax.plot(x, y)
    if a > 0:
        plt.ylim((y1 - 2), (y1 + 10))
    else:
        plt.ylim((y1 - 10), (y1 + 2))
    plt.xlim((x1 - 6), (x1 + 6))
    plt.scatter(x1, y1, c='black')
    plt.scatter(x2, y2, c='black')
    plt.show()

def function_result():
  """Функция генерирует задание, выводит правильный ответ и график"""
  x, y, a, b, c, x1, y1, x2, y2 = input_parameters()
  while True:
    x_task = randint(-40, 40)
    answer = a * x_task ** 2 + b * x_task + c
    if x_task != x1 and x_task != x2 and float(answer).is_integer() and answer != y2:
      answer = int(answer)
      break
  task = f'На рисунке изображён график функции вида \(f(x) = \frac{{x^2}}{{a}} + bx + c\), где числа a, b и c — целые. Найдите значение уравнения при \(f({x_task})\). '
  solution = None


  def paint():
    function_graph_parabola(x, y, a, b, c, x1, y1, x2, y2)

  return answer, task, paint, solution


# Задача 5 https://math-ege.sdamgia.ru/problem?id=508903
# одна прямая вида f(x) = kx + b
def input_parameters():
    while True:
        x1, y1, x2, y2 = np.random.randint(-8, 9, size=4)
        if x1 != x2 and y1 != y2:
          x = np.linspace(-9, 9, 50)
          if (x2 - x1) != 0:
            y = (((x-x1)*(y2-y1))/(x2-x1)) + y1
            a = y2 - y1
            b = x1 - x2
            c = (y1 * x2) - (x1 * y2)
            break
    return x, y, x1, y1, x2, y2, a ,b, c


def function_graph_line(x, y, x1, y1, x2, y2):
    """Функция стоит прямую по переданным параметрам"""
    fig, ax = plot()
    ax.plot(x, y)
    ax.grid(True)
    plt.ylim(-9, 9)
    plt.xlim(-9, 9)
    plt.scatter(x1, y1, c='blue')
    plt.scatter(x2, y2, c='blue')
    plt.show()


def function_result ():
    """Функция генерирует задание, выводит правильный ответ и график"""
    x, y, x1, y1, x2, y2, a ,b, c = input_parameters()
    task_random = randint(0,1)
    while True:
      x_y_random = choice(list(set([x for x in range(-50, 50)]) - set([x for x in range(-8, 8)])))
      if task_random == 1:
        task = f'На рисунке изображён график функции \(f(x) = kx + b\). Найдите значение x, при котором \(f(x) = {x_y_random}\).' #ордината - y
        answer = (-b*x_y_random - c)/a
        if float(answer).is_integer():
          break
      else:
        task = f'На рисунке изображён график функции \(f(x) = kx + b\). Найдите значение \(f({x_y_random})\).'  # абцисса - x
        answer = (-a*x_y_random - c)/b
        if float(answer).is_integer():
          break
    solution = None

    def paint():
        function_graph_line(x, y, x1, y1, x2, y2)
    return answer, task, paint, solution


# Задача 6 https://math-ege.sdamgia.ru/problem?id=635152
# Парабола вида y = |a * x ** 2 + b * x + c|
def input_parameters():
    """Функция формирует две точки, через которые строится парабола"""
    while True:
        x1, x2, y2 = np.random.randint(-7, 8, size=3) #parabola_vertex = (x1, y1) #parabola_point = (x2, y2)
        y1 = np.random.randint(-5, 0, size=1)
        if (x2 - x1) != 0 and (y2 - y1) !=0:
            a = (y2 - y1) / ((x2 - x1) ** 2)
            if float(a).is_integer() and a > 0:
              a = int(a)
              if a != 0:
                b = int(-2 * a * x1)
                c = int(y2 - a * x2 ** 2 - b * x2)
                x = np.linspace(x1 - 10, x1 + 10, 400)
                y = abs(a * x ** 2 + b * x + c)
                break
    return x, y, a, b, c, x1, y1, x2, y2


def function_graph(x, y, a, b, c, x1, y1, x2, y2):
    """Функция стоит параболу по переданным параметрам"""
    fig, ax = plot()
    ax.plot(x, y)

    ax.grid(True)
    plt.ylim((abs(y1) - 6), (abs(y1) + 10))
    plt.xlim((x1 - 8), (x1 + 8))
    plt.scatter(x1, abs(y1), c='black')
    plt.scatter(x2, abs(y2), c='black')
    plt.show()

def function_result():
  """Функция генерирует задание, выводит правильный ответ и график"""
  x_task = randint(-5, 5)
  x, y, a, b, c, x1, y1, x2, y2 = input_parameters()
  answer = (abs(a * x_task ** 2 + b * x_task + c))
  task = f'На рисунке изображён график фуıкции вида \(f(x) = |ax^2 + bx + c|\), где a, b и c — целые числа. Вычислите \(f({x_task})\).'
  solution = None

  def paint():
    function_graph(x, y, a, b, c, x1, y1, x2, y2)

  return answer, task, paint, solution


# Задача 7 https://math-ege.sdamgia.ru/problem?id=508971
# Гипербола вида y = k / (x + a)
def input_parameters():
    """Функция формирует точки, через которые строится график"""
    while True:
      k = randint(-10, 10)
      if k != 0:
        a = randint(-5, 5)
        x1 = np.linspace(-15, -a - 0.0001, 400)
        x2 = np.linspace(-a + 0.0001, 15, 400)
        y1 = k / (x1 + a)
        y2 = k / (x2 + a)
        break
    return x1, x2, y1, y2, a, k


def function_graph(x1, x2, y1, y2, a, k):
    """Функция стоит график по переданным параметрам"""
    fig, ax = plot()
    ax.plot(x1, y1, c='orange')
    ax.plot(x2, y2, c='orange')
    x_dash = [int(-a), int(-a)]
    y_dash = [x_dash[0] -50, x_dash[1] + 50]
    ax.plot(x_dash, y_dash, linestyle='dashed', c='black')
    plt.ylim(-10, 10)
    plt.xlim(-a - 10, -a + 10)
    for x_point in range(-20, 20):
      if (x_point + a) != 0:
        y_point = k / (x_point + a)
        scatter(x_point, y_point)
    plt.show()

def function_result():
  """Функция генерирует задание, выводит правильный ответ и график"""
  x1, x2, y1, y2, a, k = input_parameters()
  while True:
    x_task = randint(-60, 60)
    if (x_task + a) != 0:
      y_task = k / (x_task + a)
      if (y_task % 0.025 == 0 or y_task % 0.003125 == 0) and not float(y_task).is_integer():
        break
  random_task = randint(0,1)
  if random_task == 1:
    task = f'На рисунке изображён график функции вида \(f(x) = \frac{{k}}{{x + a}}\). Найдите значение \(f({x_task})\)'
    answer = y_task
  else:
    task = f'На рисунке изображён график функции вида \(f(x) = \frac{{k}}{{x + a}}\). Найдите значение x, при котором \(f(x) = {y_task}\)'
    answer = x_task
  solution = None

  def paint():
    function_graph(x1, x2, y1, y2, a, k)

  return answer, task, paint, solution


# Задача 8 https://math-ege.sdamgia.ru/problem?id=508961
# Гипербола вида y = (k / x) + a
def input_parameters():
    """Функция формирует точки, через которые строится график"""
    while True:
      k = randint(-10, 10)
      if k != 0:
        a = randint(-5, 5)
        x1 = np.linspace(-15, -0.0001, 400)
        x2 = np.linspace(0.0001, 15, 400)
        y1 = (k / x1) + a
        y2 = (k / x2) + a
        break
    return x1, x2, y1, y2, a, k


def function_graph(x1, x2, y1, y2, a, k):
    """Функция строит график по переданным параметрам"""
    fig, ax = plot()
    ax.plot(x1, y1, c='orange')
    ax.plot(x2, y2, c='orange')
    y_dash = [int(a), int(a)]
    x_dash = [y_dash[0] -50, y_dash[1] + 50]
    ax.plot(x_dash, y_dash, linestyle='dashed', c='black')
    plt.xlim(-10, 10)
    plt.ylim(-10 + a, 10 + a)
    for x_point in range(-20, 20):
      if x_point != 0:
        y_point = (k / x_point) + a
        scatter(x_point, y_point)
    plt.show()

def function_result():
  """Функция генерирует задание, выводит правильный ответ и график"""
  x1, x2, y1, y2, a, k = input_parameters()
  while True:
    y_task = randint(-100, 100)
    if y_task - a != 0:
      x_task = k / (y_task - a)
      if (x_task % 0.025 == 0 or x_task % 0.003125 == 0) and not float(x_task).is_integer():
        break
  random_task = randint(0,1)
  if random_task == 1:
    task = f'На рисунке изображён график функции вида \(f(x) = \frac{{k}}{{x}} + a\). Найдите значение \(f({x_task})\)'
    answer = y_task
  else:
    task = f'На рисунке изображён график функции вида \(f(x) = \frac{{k}}{{x}} + a\). Найдите значение x, при котором \(f(x) = {y_task}\)'
    answer = x_task
  solution = None

  def paint():
    function_graph(x1, x2, y1, y2, a, k)

  return answer, task, paint, solution


# Задача 9 https://math-ege.sdamgia.ru/problem?id=564963
# Гипербола вида y = (ax + b) / (x + c)
def input_parameters():
    """Функция формирует точки, через которые строится график"""
    break_out_flag = True
    while break_out_flag:
      a, b, c = np.random.randint(-3, 4,size=3)
      if a != 0 and b != 0 and c != 0 and a != b and b != c and c != -1 and c != 1 and a != -1:
        x1 = np.linspace(-15, - c - 0.00001, 400)
        x2 = np.linspace(- c + 0.00001, 15, 400)
        y1 = (a * x1 + b) / (x1 + c)
        y2 = (a * x2 + b) / (x2 + c)
        for x in range(-10 - c, 10 - c):
          if (x + c) != 0:
            y = (a * x + b) / (x + c)
            if float(y).is_integer():
              break_out_flag = False
              break

    return x1, x2, y1, y2, a, b, c


def function_graph(x1, x2, y1, y2, a, b, c):
    """Функция строит график по переданным параметрам"""
    fig, ax = plot()
    ax.plot(x1, y1, c='orange')
    ax.plot(x2, y2, c='orange')
    y_dash1 = [int(a), int(a)]
    x_dash1 = [y_dash1[0] -50, y_dash1[1] + 50]
    x_dash2 = [int(-c), int(-c)]
    y_dash2 = [x_dash2[0] -50, x_dash2[1] + 50]
    ax.plot(x_dash1, y_dash1, linestyle='dashed', c='black')
    ax.plot(x_dash2, y_dash2, linestyle='dashed', c='black')
    plt.xlim(-10 - c, 10 - c)
    plt.ylim(-10 + a, 10 + a)
    for x_point in range(-20, 20):
      if (x_point + c) != 0:
        y_point = (a * x_point + b) / (x_point + c)
        scatter(x_point, y_point)
    arrow_length = 10
    ax.annotate('x', xy=(1, 0), xycoords=('axes fraction', 'data'),
                xytext=(0, arrow_length), textcoords='offset points',
                ha='center', va='bottom')
    ax.annotate('y', xy=(0, 1), xycoords=('data', 'axes fraction'),
                xytext=(arrow_length, 0), textcoords='offset points',
                ha='center', va='bottom')
    plt.show()

def function_result():
  """Функция генерирует задание, выводит правильный ответ и график"""
  x1, x2, y1, y2, a, b, c = input_parameters()

  def paint():
    function_graph(x1, x2, y1, y2, a, b, c)

  random_task = randint(0,4)
  if random_task == 0:
    task = f'На рисунке изображён график функции вида \(f(x) = \\frac{{ax + b}}{{x + c}}\), где числа a, b и c — целые. Найдите значение a.'
    answer = a
  elif random_task == 1:
    task = f'На рисунке изображён график функции вида \(f(x) = \\frac{{ax + b}}{{x + c}}\), где числа a, b и c — целые. Найдите значение c.'
    answer = c
  elif random_task == 2:
    task = f'На рисунке изображён график функции вида \(f(x) = \\frac{{kx + a}}{{x + b}}\). Найдите значение k.'
    # k, a, b = a, b, c
    answer = a
  else:
    task = f'На рисунке изображён график функции вида \(f(x) = \\frac{{ax + b}}{{x + c}}\), Найдите значение b.'
    # k, a, b = a, b, c
    answer = c
  solution = None

  return answer, task, paint, solution


# Задача 10 https://math-ege.sdamgia.ru/problem?id=509113
# Функция вида f(x) = k*sqrt(x)
def input_parameters():
    """Функция формирует точки, через которые строится график"""
    while True:
      k = randint(-10, 10)
      if k != 0:
        x = np.linspace(0.00001, 20, 400)
        y = k*(x**0.5)
        break
    return x, y, k


def function_graph(x, y, k):
    """Функция строит график по переданным параметрам"""
    fig, ax = plot()
    ax.plot(x, y, c='orange')
    plt.xlim(0, 20)
    if k > 0:
      plt.ylim(0, 20)
    else:
      plt.ylim(-20, 0)
    for x_point in range(2, 20):
      y_point = k*(x_point**0.5)
      scatter(x_point, y_point)
    plt.show()

def function_result():
  """Функция генерирует задание, выводит правильный ответ и график"""
  x, y, k = input_parameters()
  while True:
    x_task = (d.Decimal(str(randint(1,3))) + d.Decimal(str(randrange(1, 10, 1))) / d.Decimal(str(10)))**d.Decimal(str(2))
    y_task = (d.Decimal(str(k))*(x_task**d.Decimal(str(0.5)))).quantize(d.Decimal("1.00"))
    if (x_task % d.Decimal(str(0.01))) == 0 and (y_task % d.Decimal(str(0.01))) == 0:
      break
  random_task = randint(0, 1)
  if random_task == 1:
    task = f'На рисунке изображён график функции \(f(x) = k\sqrt{{x}}\). Найдите \(f({x_task})\).'
    answer = y_task
  else:
    task = f'На рисунке изображён график функции \(f(x) = k\sqrt{{x}}\). Найдите \(f(x) = {y_task}\).'
    answer = x_task
  solution = None

  def paint():
    function_graph(x, y, k)

  return answer, task, paint, solution


# Задача 11 https://math-ege.sdamgia.ru/problem?id=509009
# Логарифмическая функция f(x)=b + loga(x)
def input_parameters():
    """Функция формирует точки, через которые строится график"""
    while True:
      a = randint(3, 10)
      b = randint(-5, 5)
      if a != 0:
        x = list(np.linspace(0.00001, 20, 400))
        for numb in x:
          if numb + a == 0:
            x.remove(numb)
          else:
            y = [b + m.log(numb, a) for numb in x]
        break
    return x, y, a, b


def function_graph(x, y, a, b):
    """Функция строит график по переданным параметрам"""
    fig, ax = plot()
    ax.plot(x, y, c='orange')
    ax.grid(True)
    plt.xlim(0, 11)
    plt.ylim(b-5, b + 5)
    for x_point in range(1, 11):
      y_point = b + m.log(x_point, a)
      scatter(x_point, y_point)
    plt.show()

def function_result():
  """Функция генерирует задание, выводит правильный ответ и график"""
  x, y, a, b = input_parameters()
  while True:
    x_task = d.Decimal(randint(10, 300))
    y_task = d.Decimal(b) + d.Decimal(m.log(x_task, d.Decimal(a)))
    if float(y_task).is_integer():
      break
  random_task = randint(0, 1)
  if random_task == 1:
    task = f'На рисунке изображён график функции \(f(x)=b + \log_{{a}}x\). Найдите \(f({x_task})\).'
    answer = y_task
  else:
    task = f'На рисунке изображён график функции \(f(x)=b + \log_{{a}}x\). Найдите \(f(x) = {y_task}\).'
    answer = x_task
  solution = None
  def paint():
    function_graph(x, y, a, b)
  print('a', a, 'b', b)

  return answer, task, paint, solution


# Задача 12 https://math-ege.sdamgia.ru/problem?id=509042
# Логарифмическая функция f(x)=loga(x + b)
def input_parameters():
    """Функция формирует точки, через которые строится график"""
    while True:
      b = randint(1, 7)
      a = randint(2, 10 - b)
      if a != 0:
        x = list(np.linspace(-b + 0.00001, 20, 400))
        y = [m.log((b + numb), a) for numb in x]
        break
    return x, y, a, b


def function_graph(x, y, a, b):
    """Функция строит график по переданным параметрам"""
    fig, ax = plot()
    ax.plot(x, y, c='orange')
    plt.xlim(-b - 1, -b + 11)
    plt.ylim(-5, + 5)
    for x_point in range(-b + 2, 11):
      y_point = m.log((x_point + b), a)
      scatter(x_point, y_point)
    plt.show()

def function_result():
  """Функция генерирует задание, выводит правильный ответ и график"""
  x, y, a, b = input_parameters()
  while True:
    x_task = randint(b + 10, 500)
    y_task = m.log((x_task + b), a)
    if float(y_task).is_integer():
      y_task = int(y_task)
      break
  random_task = randint(0, 1)
  if random_task == 1:
    task = f'На рисунке изображён график функции \(f(x)=\log_{{a}}(x + b)\). Найдите \(f({x_task})\).'
    answer = y_task
  else:
    task = f'На рисунке изображён график функции \(f(x)=\log_{{a}}(x + b)\). Найдите значение \(x\), при котором \(f(x) = {y_task}\).'
    answer = x_task
  solution = None
  def paint():
    function_graph(x, y, a, b)

  return answer, task, paint, solution


# Задача 13 https://math-ege.sdamgia.ru/problem?id=639672
# Логарифмическая функция f(x)=loga(x)
def input_parameters():
    """Функция формирует точки, через которые строится график"""
    while True:
      a = randint(2, 10)
      if a != 0:
        x = list(np.linspace(0.00001, 15, 300))
        y = [m.log((numb), a) for numb in x]
        break
    return x, y, a


def function_graph(x, y, a):
    """Функция строит график по переданным параметрам"""
    fig, ax = plot()
    ax.plot(x, y, c='orange')
    plt.xlim(0, 10)
    plt.ylim(-5, 5)
    for x_point in range(1, 10):
      y_point = m.log((x_point), a)
      scatter(x_point, y_point)
    plt.show()

def function_result():
  """Функция генерирует задание, выводит правильный ответ и график"""
  x, y, a = input_parameters()
  while True:
    x_task = randint(10, 500)
    y_task = m.log((x_task), a)
    if float(y_task).is_integer():
      y_task = int(y_task)
      break
  random_task = randint(0, 1)
  if random_task == 1:
    task = f'На рисунке изображён график функции \(f(x)=\log_{{a}}x\). Найдите \(f({x_task})\).'
    answer = y_task
  else:
    task = f'На рисунке изображён график функции \(f(x)=\log_{{a}}x\). Найдите значение \(x\), при котором \(f(x) = {y_task}\).'
    answer = x_task
  solution = None
  def paint():
    function_graph(x, y, a)

  return answer, task, paint, solution


# Задача 14 https://math-ege.sdamgia.ru/problem?id=509089
# Логарифмическая функция f(x) = a^x + b
def input_parameters():
    """Функция формирует точки, через которые строится график"""
    while True:
      b = randint(-6, 2)
      a = randint(2, b + 7)
      if a != 0 and b != 0:
        x = np.linspace(-20, 20, 400)
        y = a**x + b
        break
    return x, y, a, b


def function_graph(x, y, a, b):
    """Функция строит график по переданным параметрам"""
    fig, ax = plot()
    ax.plot(x, y, c='orange')
    plt.xlim(-5, 5)
    plt.ylim(b - 2, b + 8)
    for x_point in range(1, 11):
      y_point = a**x_point + b
      scatter(x_point, y_point)
    plt.show()

def function_result():
  """Функция генерирует задание, выводит правильный ответ и график"""
  x, y, a , b = input_parameters()
  while True:
    x_task = randint(3, 7)
    y_task = a**x_task + b
    if float(y_task).is_integer() and y_task < 10000:
      break
  random_task = randint(0, 1)
  if random_task == 1:
    task = f'На рисунке изображён график функции \(f(x)=a^x + b\). Найдите \(f({x_task})\).'
    answer = int(y_task)
  else:
    task = f'На рисунке изображён график функции \(f(x)=a^x + b\). Найдите значение \(x\), при котором \(f(x) = {y_task}\).'
    answer = int(x_task)
  solution = None
  def paint():
    function_graph(x, y, a, b)

  return answer, task, paint, solution


# Задача 15 https://math-ege.sdamgia.ru/problem?id=509101
# Логарифмическая функция f(x) = a^(x + b)
def input_parameters():
    """Функция формирует точки, через которые строится график"""
    while True:
      b = randint(-5, 4)
      a = randint(2, 8)
      if a != 0 and b != 0:
        x = np.linspace(-20, 20, 400)
        y = a**(x + b)
        break
    return x, y, a, b


def function_graph(x, y, a, b):
    """Функция строит график по переданным параметрам"""
    fig, ax = plot()
    ax.plot(x, y, c='orange')
    plt.xlim(-b - 5, -b + 5)
    plt.ylim(-1, 9)
    for x_point in range(-b, -b + 11):
      y_point = a**(x_point + b)
      scatter(x_point, y_point)
    plt.show()

def function_result():
  """Функция генерирует задание, выводит правильный ответ и график"""
  x, y, a , b = input_parameters()
  while True:
    x_task = d.Decimal(randint(-b - 4, -b + 15))
    y_task = d.Decimal(d.Decimal(a)**(x_task + d.Decimal(b)))
    if  x_task < -b and (y_task % d.Decimal(0.0625) == 0 or y_task % d.Decimal(0.015625) == 0 or y_task % d.Decimal(0.01) == 0):
      break
    elif x_task > -b + 3 and float(y_task).is_integer() and y_task < d.Decimal(10000):
      break
  random_task = randint(0, 1)
  if random_task == 1:
    task = f'На рисунке изображён график функции \(f(x)=a^{{x + b}}\). Найдите \(f({x_task})\).'
    answer = y_task
  else:
    task = f'На рисунке изображён график функции \(f(x)=a^{{x + b}}\). Найдите значение \(x\), при котором \(f(x) = {y_task}\).'
    answer = x_task
  solution = None
  def paint():
    function_graph(x, y, a, b)

  return answer, task, paint, solution


# Задача 16 https://math-ege.sdamgia.ru/problem?id=639480
# Логарифмическая функция f(x) = a^x
def input_parameters():
    """Функция формирует точки, через которые строится график"""
    while True:
      a = choice([0.5, 1, 2, 3, 4, 5, 6, 7, 8])
      if a != 0 and a != 1:
        x = np.linspace(-10, 10, 400)
        y = a**(x)
        break
    return x, y, a


def function_graph(x, y, a):
    """Функция строит график по переданным параметрам"""
    fig, ax = plot()
    ax.plot(x, y, c='orange')
    plt.xlim( - 5, 5)
    plt.ylim(-1, 9)
    for x_point in range(-5, 5):
      y_point = a**(x_point)
      scatter(x_point, y_point)
    plt.show()

def function_result():
  """Функция генерирует задание, выводит правильный ответ и график"""
  x, y, a= input_parameters()
  while True:
    x_task = d.Decimal(randint(-8, 8))
    y_task = d.Decimal(d.Decimal(a)**(x_task))
    if x_task != 0 and x_task != 1 and (y_task % d.Decimal(0.0625) == 0 or y_task % d.Decimal(0.015625) == 0 or y_task % d.Decimal(0.01) == 0) and y_task < 10000:
      break
  random_task = randint(0, 1)
  if random_task == 1:
    task = f'На рисунке изображён график функции \(f(x)=a^x\). Найдите \(f({x_task})\).'
    answer = y_task
  else:
    task = f'На рисунке изображён график функции \(f(x)=a^x\). Найдите значение \(x\), при котором \(f(x) = {y_task}\).'
    answer = x_task
  solution = None
  def paint():
    function_graph(x, y, a)

  return answer, task, paint, solution