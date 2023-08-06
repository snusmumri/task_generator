import matplotlib.pyplot as plt
from random import randint
import numpy as np
import math as m
import decimal as d


# Задача 1 №509213 c сайта https://math-ege.sdamgia.ru/problem?id=509213
# пересечение двух прямых
def input_parameters():
    while True:
        x1, y1, x2, y2, x3, y3, x4, y4 = np.random.randint(-8, 9, size=8)
        if x1 != x2 and x2 != x3 and x3 != x4 and x1 != x4 and y1 != y2 and y2 != y3 and y3 != y4 and y1 != y4:
            x = np.linspace(-9, 9, 50)
            if (x2 - x1) != 0 and (x4 - x3) != 0:
                y_first = (((x-x1)*(y2-y1))/(x2-x1)) + y1
                y_second = (((x-x3)*(y4-y3))/(x4-x3)) + y3
                a1 = y2 - y1
                b1 = x1 - x2
                c1 = (y1 * x2) - (x1 * y2)
                a2 = y4 - y3
                b2 = x3 - x4
                c2 = (y3 * x4) - (x3 * y4)
                determinant = (a1 * b2) - (a2 * b1)
                if determinant == 0:
                    intersection_point = "Прямые параллельны"
                else:
                    x_int = (((b1 * c2) - (b2 * c1)) / determinant)
                    y_int = (((a2 * c1) - (a1 * c2)) / determinant)
                    intersection_point = [x_int, y_int]
                    if ((x_int % 0.025 == 0 and y_int % 0.025 == 0) or (x_int % 0.03125 == 0 and y_int % 0.03125 == 0)) and x_int != x1 and x_int != x2 and x_int != x3 and x_int != x4 :
                      break
    return x, y_first, y_second, x1, y1, x2, y2, x3, y3, x4, y4, intersection_point, determinant


def function_graph(x, y_first, y_second, x1, y1, x2, y2, x3, y3, x4, y4):
    """Функция стоит две прямые по переданным параметрам"""
    fig = plt.figure()
    ax = plt.axes()
    fig.add_axes(ax)
    ax.spines[["left", "bottom"]].set_position('zero')
    ax.spines[["top", "right"]].set_visible(False)
    ax.plot(1, 0, ">k", transform=ax.get_yaxis_transform(), clip_on=False)
    ax.plot(0, 1, "^k", transform=ax.get_xaxis_transform(), clip_on=False)
    ax.plot(x, y_first)
    ax.plot(x, y_second)
    plt.xticks(np.arange(-10,10,1)) #устанавливаю шаг сетки
    plt.yticks(np.arange(-10,10,1))
    ax.grid(True)
    plt.ylim(-9, 9)
    plt.xlim(-9, 9)

    plt.scatter(x1, y1, c='blue')
    plt.scatter(x2, y2, c='blue')
    plt.scatter(x3, y3, c='red')
    plt.scatter(x4, y4, c='red')
    arrow_length = 10
    ax.annotate('x', xy=(1, 0), xycoords=('axes fraction', 'data'),
                xytext=(0, arrow_length), textcoords='offset points',
                ha='center', va='bottom')
    ax.annotate('y', xy=(0, 1), xycoords=('data', 'axes fraction'),
                xytext=(arrow_length, 0), textcoords='offset points',
                ha='center', va='bottom')
    plt.show()


def function_result ():
    """Функция генерирует задание, выводит правильный ответ и график"""
    x, y_first, y_second, x1, y1, x2, y2, x3, y3, x4, y4, intersection_point, determinant = input_parameters()
    task_random = randint(0,1)
    if task_random == 1:
        task = f'На рисунке изображены графики двух линейных функций. Найдите ординату точки пересечения графиков.' #ордината - y
    else:
        task = f'На рисунке изображены графики двух линейных функций. Найдите абциссу точки пересечения графиков.'  # абцисса - x
    if determinant == 0:
        solution = f'Для решения задачи мы будем использовать уравнения прямых в общем виде. ' \
                   f'Найдем по графику координаты двух точек для первой прямой \(A(x1,y1)\) и \(B(x2,y2)\), и для второй \(C(x3,y3)\) и \(D(x4,y4)\). ' \
                   f'Запишем уравнение первой прямой в общем виде: \(a1x + b1y + c1 = 0\). ' \
                   f'Где \(a1 = y2 - y1, b1 = x1 - x2, c1 = x2y1 - x1y2\).' \
                   f'Запишем уравнение второй прямой в общем виде: \(a2x + b2y + c2 = 0\).' \
                   f'Где \(a2 = y4 - y3, b2 = x3 - x4, c2 = x4y3 - x3y4\).' \
                   f'Получим: \((a1 * b2) - (a2 * b1) = {determinant}\)' \
                   f'Поскольку выражение равно \(0\), прямые параллельны'
    else:
        solution = f'Для решения задачи мы будем использовать уравнения прямых в общем виде. ' \
                   f'Найдем по графику координаты двух точек для первой прямой \(A(x1,y1)\) и \(B(x2,y2)\), и для второй \(C(x3,y3)\) и \(D(x4,y4)\). ' \
                   f'Запишем уравнение первой прямой в общем виде: \(a1x + b1y + c1 = 0\). ' \
                   f'Где \(a1 = y2 - y1, b1 = x1 - x2, c1 = x2y1 - x1y2\).' \
                   f'Запишем уравнение второй прямой в общем виде: \(a2x + b2y + c2 = 0\).' \
                   f'Где \(a2 = y4 - y3, b2 = x3 - x4, c2 = x4y3 - x3y4\).' \
                   f'Получим: \((a1 * b2) - (a2 * b1) = {determinant}\)' \
                   f'Найдем значение точек x и y воспользовавшись вырежениями:' \
                   f'\(x = (b1 * c2) - (b2 * c1)) / (a1 * b2) - (a2 * b1) = {intersection_point[0]}\)' \
                   f'\(y = ((a2 * c1) - (a1 * c2)) / (a1 * b2) - (a2 * b1) = {intersection_point[0]}\)'
    answer = intersection_point[task_random]
    def paint():
        function_graph(x, y_first, y_second, x1, y1, x2, y2, x3, y3, x4, y4)
    return answer, task, paint, solution


# Задача 2 https://math-ege.sdamgia.ru/problem?id=509259
# Пересечение двух парабол
def input_parameters():
    """Функция формирует точки, через которые строятся 2 параболы"""
    while True:
        x1, y1, x3, y3 = np.random.randint(-5, 6, size=4) # parabola_vertex_first = (x1, y1), common_point = (x3, y3)
        x2, y2 = np.random.randint(-2, 3, size=2) # parabola_vertex_second = (x2, y2)
        if (x3 - x1) != 0 and (y3 - y1) !=0 and (x3 - x2) != 0 and (y3 - y2) != 0 and x1 != x2:
            a1 = (y3 - y1) / ((x3 - x1) ** 2)
            a2 = (y3 - y2) / ((x3 - x2) ** 2)
            if float(a1).is_integer() and float(a2).is_integer() and (a1 - a2) != 0:
              a1 = int(a1)
              a2 = int(a2)
              if a1 != 0 and a2 != 0:
                b1 = int(-2 * a1 * x1)
                b2 = int(-2 * a2 * x2)
                c1 = int(y3 - a1 * x3 ** 2 - b1 * x3)
                c2 = int(y3 - a2 * x3 ** 2 - b2 * x3)
                x = np.linspace(-15, 15, 250)
                y_first = a1 * x ** 2 + b1 * x + c1
                y_second = a2 * x ** 2 + b2 * x + c2

                a1a2 = a1 - a2
                b1b2 = b1 - b2
                c1c2 = c1 - c2
                discr = b1b2 ** 2 - 4 * a1a2 * c1c2
                if discr > 0:
                  x1_= round((-b1b2 + discr ** 0.5) / (2 * a1a2),2)
                  x2_ = round((-b1b2 - discr ** 0.5) / (2 * a1a2),2)
                  y1_ = round((a2 * x1_ ** 2 + b2 * x1_ + c2), 2)
                  y2_ = round((a2 * x2_ ** 2 + b2 * x2_ + c2), 2)
                  if x1_ == x3 and y1_ == y3:
                    x4 = x2_
                    y4 = y2_
                  elif x2_ == x3 and y2_ == y3:
                    x4 = x1_
                    y4 = y1_
                  if x4 < -9 or x4 > 9:
                    break
    return x, y_first, y_second , a1, b1, c1, a2, b2, c2, x1, y1, x2, y2, x3, y3, x4, y4


def function_graph(x, y_first, y_second , a1, b1, c1, a2, b2, c2, x1, y1, x2, y2, x3, y3):
    """Функция стоит две параболы по переданным параметрам"""
    fig = plt.figure()
    ax = plt.axes()
    fig.add_axes(ax)
    ax.spines[["left", "bottom"]].set_position('zero')
    ax.spines[["top", "right"]].set_visible(False)
    ax.plot(1, 0, ">k", transform=ax.get_yaxis_transform(), clip_on=False)
    ax.plot(0, 1, "^k", transform=ax.get_xaxis_transform(), clip_on=False)
    ax.plot(x, y_first)
    ax.plot(x, y_second)
    plt.xticks(np.arange(-20,20,1)) #устанавливаю шаг сетки
    plt.yticks(np.arange(-20,20,1))
    ax.grid(True)
    if a1 > 0:
      if y1 >= y2:
        plt.ylim((y2 - 2), (y2 + 14))
      else:
        plt.ylim((y1 - 2), (y1 + 14))
    else:
      if y1 >= y2:
        plt.ylim((y1 - 14), (y1 + 2))
      else:
        plt.ylim((y2 - 14), (y2 + 2))

    plt.xlim(-8, 8)

    for x in range(x1 - 3, x1 + 3):
        y = a1 * x ** 2 + b1 * x + c1
        plt.scatter(x, y, c='blue')
    for x in range(x2 - 3, x2 + 3):
        y = a2 * x ** 2 + b2 * x + c2
        plt.scatter(x, y, c='red')
    plt.text (x3 + 0.3, y3 + 0.3, 'A', fontsize=18,)
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
    x, y_first, y_second , a1, b1, c1, a2, b2, c2, x1, y1, x2, y2, x3, y3, x4, y4 = input_parameters()
    task_random = randint(0,1)

    def answer():
      if task_random == 1:
        answer = y4
      else:
        answer = x4
      return answer


    def signs_of_digits():
      digits = (a1, b1, c1, a2, b2, c2, x1, y1, x2, y2, x3, y3)
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


    def task():
      str_digits, equation1, equation2 = signs_of_digits()
      if task_random == 1:
        axis = f'ординату'
      else:
        axis = f'абциссу'
      task = f'На рисунке изображены графики функций \({equation1}\) и \(g(x) = ax^2 + bx + c\), которые пересекаются в точках A и B. Найдите {axis} точки B.'
      return task

    def solution ():
      str_digits, equation1, equation2 = signs_of_digits()
      third_point = a2 * (x2 + 1) ** 2 + b2 * (x2 + 1) + c2
      solution = f'График функции \({equation1}\) должен пересекать ось ординат в точке {c1}. Значит, график \(y = f(x)\) изображен синим цветом, а график \(у = g(x)\) — оранжевым. По рисунку определяем, что \(g({x3}) = {y3}, g({x2}) = {y2}\), \(g({x2+1}) = {third_point}\).\n' \
                 f'Тогда:\n' \
                 f'\(g({x3})-g({x2})=a({x3**2}-{x2**2})+b({x3}-{x2}={x3**2-x2**2}a-{x3-x2}b)={y3}-{y2}={y3-y2}\)\n' \
                 f'\(g({x2})-g({x2+1})=a({x2**2}-{x2+1**2})+b({x2}-{x2+1}={x2**2-x2+1**2}a-{x2-x2+1}b)={y2}-{third_point}={y2-third_point}\).\n' \
                 f'Решая полученную систему, получаем: \(a = {a2}\), \(b = {b2}\), из \(g(0) = {c2}\) получим \(c = {c2}\). Теперь найдём абсциссу точки B:\n' \
                 f'Приравняем полученные уравнения и найдем их корни: \({equation1[6:]} = {equation2[6:]}\)\n' \
                 f'Получим координаты точки пересечения \(В({x4}, {y4})\)' \

      return solution
    def paint():
        function_graph(x, y_first, y_second , a1, b1, c1, a2, b2, c2, x1, y1, x2, y2, x3, y3)
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
    fig = plt.figure()
    ax = plt.axes()
    fig.add_axes(ax)
    ax.spines[["left", "bottom"]].set_position('zero')
    ax.spines[["top", "right"]].set_visible(False)
    ax.plot(1, 0, ">k", transform=ax.get_yaxis_transform(), clip_on=False)
    ax.plot(0, 1, "^k", transform=ax.get_xaxis_transform(), clip_on=False)
    ax.plot(x, y)
    plt.xticks(np.arange(-10, 10, 1))
    plt.yticks(np.arange(-10, 10, 1))
    ax.grid(True)
    if a > 0:
        plt.ylim((y1 - 2), (y1 + 8))
    else:
        plt.ylim((y1 - 8), (y1 + 2))
    plt.xlim((x1 - 5), (x1 + 5))
    for x in range(x1 - 3, x1 + 3):
        y = a * x ** 2 + b * x + c
        plt.scatter(x, y, c='black')
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
    fig = plt.figure()
    ax = plt.axes()
    fig.add_axes(ax)
    ax.spines[["left", "bottom"]].set_position('zero')
    ax.spines[["top", "right"]].set_visible(False)
    ax.plot(1, 0, ">k", transform=ax.get_yaxis_transform(), clip_on=False)
    ax.plot(0, 1, "^k", transform=ax.get_xaxis_transform(), clip_on=False)
    ax.plot(x, y)
    plt.xticks(np.arange(-20, 20, 1))
    plt.yticks(np.arange(-20, 20, 1))
    ax.grid(True)
    if a > 0:
        plt.ylim((y1 - 2), (y1 + 10))
    else:
        plt.ylim((y1 - 10), (y1 + 2))
    plt.xlim((x1 - 6), (x1 + 6))
    plt.scatter(x1, y1, c='black')
    plt.scatter(x2, y2, c='black')
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
    fig = plt.figure()
    ax = plt.axes()
    fig.add_axes(ax)
    ax.spines[["left", "bottom"]].set_position('zero')
    ax.spines[["top", "right"]].set_visible(False)
    ax.plot(1, 0, ">k", transform=ax.get_yaxis_transform(), clip_on=False)
    ax.plot(0, 1, "^k", transform=ax.get_xaxis_transform(), clip_on=False)
    ax.plot(x, y)
    plt.xticks(np.arange(-10,10,1)) #устанавливаю шаг сетки
    plt.yticks(np.arange(-10,10,1))
    ax.grid(True)
    plt.ylim(-9, 9)
    plt.xlim(-9, 9)
    plt.scatter(x1, y1, c='blue')
    plt.scatter(x2, y2, c='blue')
    arrow_length = 10
    ax.annotate('x', xy=(1, 0), xycoords=('axes fraction', 'data'),
                xytext=(0, arrow_length), textcoords='offset points',
                ha='center', va='bottom')
    ax.annotate('y', xy=(0, 1), xycoords=('data', 'axes fraction'),
                xytext=(arrow_length, 0), textcoords='offset points',
                ha='center', va='bottom')
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
    fig = plt.figure()
    ax = plt.axes()
    fig.add_axes(ax)
    ax.spines[["left", "bottom"]].set_position('zero')
    ax.spines[["top", "right"]].set_visible(False)
    ax.plot(1, 0, ">k", transform=ax.get_yaxis_transform(), clip_on=False)
    ax.plot(0, 1, "^k", transform=ax.get_xaxis_transform(), clip_on=False)
    ax.plot(x, y)
    plt.xticks(np.arange(-20, 20, 1))
    plt.yticks(np.arange(-20, 20, 1))
    ax.grid(True)
    plt.ylim((abs(y1) - 6), (abs(y1) + 10))
    plt.xlim((x1 - 8), (x1 + 8))
    plt.scatter(x1, abs(y1), c='black')
    plt.scatter(x2, abs(y2), c='black')
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
    fig = plt.figure()
    ax = plt.axes()
    fig.add_axes(ax)
    ax.spines[["left", "bottom"]].set_position('zero')
    ax.spines[["top", "right"]].set_visible(False)
    ax.plot(1, 0, ">k", transform=ax.get_yaxis_transform(), clip_on=False)
    ax.plot(0, 1, "^k", transform=ax.get_xaxis_transform(), clip_on=False)
    ax.plot(x1, y1, c='orange')
    ax.plot(x2, y2, c='orange')
    x_dash = [int(-a), int(-a)]
    y_dash = [x_dash[0] -50, x_dash[1] + 50]
    ax.plot(x_dash, y_dash, linestyle='dashed', c='black')
    plt.xticks(np.arange(-20, 20, 1), fontsize=8)
    plt.yticks(np.arange(-20, 20, 1), fontsize=8)
    ax.grid(True)
    plt.ylim(-10, 10)
    plt.xlim(-a - 10, -a + 10)
    for x in range(-20, 20):
      if (x + a) != 0:
        y = k / (x + a)
        if float(y).is_integer():
          plt.scatter(x, y, c='black')
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
    fig = plt.figure()
    ax = plt.axes()
    fig.add_axes(ax)
    ax.spines[["left", "bottom"]].set_position('zero')
    ax.spines[["top", "right"]].set_visible(False)
    ax.plot(1, 0, ">k", transform=ax.get_yaxis_transform(), clip_on=False)
    ax.plot(0, 1, "^k", transform=ax.get_xaxis_transform(), clip_on=False)
    ax.plot(x1, y1, c='orange')
    ax.plot(x2, y2, c='orange')
    y_dash = [int(a), int(a)]
    x_dash = [y_dash[0] -50, y_dash[1] + 50]
    ax.plot(x_dash, y_dash, linestyle='dashed', c='black')
    plt.xticks(np.arange(-20, 20, 1), fontsize=8)
    plt.yticks(np.arange(-20, 20, 1), fontsize=8)
    ax.grid(True)
    plt.xlim(-10, 10)
    plt.ylim(-10 + a, 10 + a)
    for x in range(-20, 20):
      if x != 0:
        y = (k / x) + a
        if float(y).is_integer():
          plt.scatter(x, y, c='black')
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
    fig = plt.figure()
    ax = plt.axes()
    fig.add_axes(ax)
    ax.spines[["left", "bottom"]].set_position('zero')
    ax.spines[["top", "right"]].set_visible(False)
    ax.plot(1, 0, ">k", transform=ax.get_yaxis_transform(), clip_on=False)
    ax.plot(0, 1, "^k", transform=ax.get_xaxis_transform(), clip_on=False)
    ax.plot(x1, y1, c='orange')
    ax.plot(x2, y2, c='orange')
    y_dash1 = [int(a), int(a)]
    x_dash1 = [y_dash1[0] -50, y_dash1[1] + 50]
    x_dash2 = [int(-c), int(-c)]
    y_dash2 = [x_dash2[0] -50, x_dash2[1] + 50]
    ax.plot(x_dash1, y_dash1, linestyle='dashed', c='black')
    ax.plot(x_dash2, y_dash2, linestyle='dashed', c='black')
    plt.xticks(np.arange(-20, 20, 1), fontsize=8)
    plt.yticks(np.arange(-20, 20, 1), fontsize=8)
    ax.grid(True)
    plt.xlim(-10 - c, 10 - c)
    plt.ylim(-10 + a, 10 + a)
    for x in range(-20, 20):
      if (x + c) != 0:
        y = (a * x + b) / (x + c)
        if float(y).is_integer():
          plt.scatter(x, y, c='black')
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
    fig = plt.figure()
    ax = plt.axes()
    fig.add_axes(ax)
    ax.spines[["left", "bottom"]].set_position('zero')
    ax.spines[["top", "right"]].set_visible(False)
    ax.plot(1, 0, ">k", transform=ax.get_yaxis_transform(), clip_on=False)
    ax.plot(0, 1, "^k", transform=ax.get_xaxis_transform(), clip_on=False)
    ax.plot(x, y, c='orange')
    plt.xticks(np.arange(0, 20, 1), fontsize=8)
    plt.yticks(np.arange(-20, 20, 1), fontsize=8)
    ax.grid(True)
    plt.xlim(0, 20)
    if k > 0:
      plt.ylim(0, 20)
    else:
      plt.ylim(-20, 0)
    for x in range(2, 20):
      y = k*(x**0.5)
      if float(y).is_integer():
        plt.scatter(x, y, c='black')
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
        y = [b + m.log(numb, a) for numb in x]
        break
    return x, y, a, b


def function_graph(x, y, a, b):
    """Функция строит график по переданным параметрам"""
    fig = plt.figure()
    ax = plt.axes()
    fig.add_axes(ax)
    ax.spines[["left", "bottom"]].set_position('zero')
    ax.spines[["top", "right"]].set_visible(False)
    ax.plot(1, 0, ">k", transform=ax.get_yaxis_transform(), clip_on=False)
    ax.plot(0, 1, "^k", transform=ax.get_xaxis_transform(), clip_on=False)
    ax.plot(x, y, c='orange')
    plt.xticks(np.arange(0, 20, 1), fontsize=8)
    plt.yticks(np.arange(-20, 20, 1), fontsize=8)
    ax.grid(True)
    plt.xlim(0, 11)
    plt.ylim(b-5, b + 5)
    for x_point in range(1, 11):
      y_point = b + m.log(x_point, a)
      if float(y_point).is_integer():
        plt.scatter(x_point, y_point, c='black')
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
  x, y, a, b = input_parameters()
  while True:
    x_task = randint(10, 500)
    y_task = b + m.log(x_task, a)
    if float(y_task).is_integer():
      break
  random_task = randint(0, 1)
  if random_task == 1:
    task = f'На рисунке изображён график функции \(f(x)=b + \log_{{a}}x\). Найдите \(f({x_task})\).'
    answer = int(y_task)
  else:
    task = f'На рисунке изображён график функции \(f(x)=b + \log_{{a}}x\). Найдите \(f(x) = {y_task}\).'
    answer = int(x_task)
  solution = None

  def paint():
    function_graph(x, y, a, b)
  return answer, task, paint, solution








