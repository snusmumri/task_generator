import matplotlib.pyplot as plt
from random import randint, choice, randrange
import numpy as np
import math as m
import decimal as d
from sympy import Point, Line, solve, symbols, Eq
from sympy.abc import x, y
from utilities.converting import save_to_base64

def function_graph(x_coord, y_coord, x_points, y_points, point_A=[], lim=[[-9, 9], [-9, 9]], dash=[], trigonometry=False, color=['orange', 'blue']):
    """Функция строит график(и) по переданным параметрам"""
    fig = plt.figure()
    ax = plt.axes()
    fig.add_axes(ax)
    ax.spines[["left", "bottom"]].set_position('zero')
    ax.spines[["top", "right"]].set_visible(False)
    ax.plot(1, 0, ">k", transform=ax.get_yaxis_transform(), clip_on=False)
    ax.plot(0, 1, "^k", transform=ax.get_xaxis_transform(), clip_on=False)
    if trigonometry:
        radian_values = [-2 * np.pi, -7 * np.pi / 4, -6 * np.pi / 4, -5 * np.pi / 4, -np.pi, -3 * np.pi / 4, -np.pi / 2,
                         -np.pi / 4, 0, np.pi / 4, np.pi / 2, 3 * np.pi / 4, np.pi, 5 * np.pi / 4, 6 * np.pi / 4,
                         7 * np.pi / 4, 2 * np.pi]
        plt.xticks(radian_values,
                   [r'$-2\pi$', '', '', '', r'$-\pi$', '', '', '', '', '', '', '', r'$+\pi$', '', '', '', r'$+2\pi$'],
                   fontsize=10)
        y_values = np.arange(-4, 4.5, 0.5)
        plt.yticks(y_values, ['', '', '', '', '', '', '-1', '', 'O', '', '1', '', '', '', '', '', ''], fontsize=10)
    else:
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
    for i in range(len(y_coord)):
        ax.plot(x_coord[i], y_coord[i], c=color[i])
    for i in range(len(y_points)):
        plt.scatter(x_points[i], y_points[i], c='black', s=15)
    if point_A:
        plt.scatter(point_A[0], point_A[1], color='black', s=15)
        plt.text(point_A[0] + 0.3, point_A[1] + 0.3, 'A', fontsize=18)
    if dash:
        for i in range(len(dash)):
            ax.plot(dash[i][0], dash[i][1], linestyle='dashed', c='gray')
    plt.xlim(lim[0][0], lim[0][1])
    plt.ylim(lim[1][0], lim[1][1])

    plt_base64 = save_to_base64(plt)
    plt.close()

    return plt_base64


# Задача 1 №509213 c сайта https://math-ege.sdamgia.ru/problem?id=509213
# пересечение двух прямых
def two_lines():
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
                        if (x_int % 0.025 == 0 or x_int % 0.03125 == 0) and (
                                y_int % 0.03125 == 0 or y_int % 0.025 == 0) and (x_int > 9 or x_int < -9) and (
                                y_int > 9 or y_int < -9):
                            x_coord = np.linspace(-9, 9, 50)
                            y_first = (((x_coord - x1) * (y2 - y1)) / (x2 - x1)) + y1
                            y_second = (((x_coord - x3) * (y4 - y3)) / (x4 - x3)) + y3
                            x_coord = [x_coord, x_coord]
                            x_int, y_int = [(int(param) if (float(param).is_integer()) else float(param)) for param in (x_int, y_int)]
                            break
                except TypeError:
                    pass
        x_points, y_points = [x1, x2, x3, x4], [y1, y2, y3, y4]
        y = [y_first, y_second]
        return x_coord, y, x_int, y_int, x_points, y_points

    def function_result():
        """Функция генерирует задание, выводит правильный ответ и график"""
        x, y, x_int, y_int, x_points, y_points = input_parameters()
        task_random = randint(0, 1)
        if task_random == 1:
            task = f'На рисунке изображены графики двух линейных функций. Найдите ординату точки пересечения графиков.'  # ордината - y
            answer = y_int
        else:
            task = f'На рисунке изображены графики двух линейных функций. Найдите абсциссу точки пересечения графиков.'  # абсцисса - x
            answer = x_int
        solution = None

        paint = function_graph(x, y, x_points, y_points)

        return answer, task, paint, solution

    answer, task, paint, solution = function_result()

    return {
        "condition": task,
        "answer": answer,
        "image": paint,
        "solution": solution
        }


# Задача 2 https://math-ege.sdamgia.ru/problem?id=509259
# Пересечение двух парабол
def two_parabolas():
    def input_parameters():
        """Функция формирует точки, через которые строятся 2 параболы"""
        while True:
            a1, b1, c1, a2, b2, c2 = symbols('a1 b1 c1 a2 b2 c2')
            a1, b1, c1, a2, b2, c2 = np.random.randint(-10, 11, size=6)
            if a1 != 0 and b1 != 0 and c1 != 0 and a2 != 0 and b2 != 0 and c2 != 0:
                eq1 = Eq(a1 * x ** 2 + b1 * x + c1, y)
                eq2 = Eq(a2 * x ** 2 + b2 * x + c2, y)
                solution = solve([eq1, eq2], [x, y], dict=True)
                if len(solution) == 2:
                    x_int_1, y_int_1, x_int_2, y_int_2 = solution[0].get(x), solution[0].get(y), solution[1].get(x), \
                    solution[1].get(y)
                    if (x_int_1 % 0.025 == 0 or x_int_1 % 0.03125 == 0) and (
                            x_int_2 % 0.025 == 0 or x_int_2 % 0.03125 == 0) and (
                            y_int_1 % 0.025 == 0 or y_int_1 % 0.03125 == 0) and (
                            y_int_2 % 0.025 == 0 or y_int_2 % 0.03125 == 0):
                        if ((y_int_2 > 20 or y_int_2 < -20) and (-10 < y_int_1 < 10)) or (
                                (y_int_1 > 20 or y_int_1 < -20) and (-10 < y_int_2 < 10)):
                            break
        x_coord = np.linspace(-15, 15, 250)
        y_coord = [a1 * x_coord ** 2 + b1 * x_coord + c1, a2 * x_coord ** 2 + b2 * x_coord + c2]
        x_coord = [x_coord, x_coord]
        x_int_1, y_int_1, x_int_2, y_int_2 = [(int(param) if (float(param).is_integer()) else float(param)) for param in
                                              (x_int_1, y_int_1, x_int_2, y_int_2)]
        intersection = [[x_int_1, y_int_1], [x_int_2, y_int_2]]
        x_points = []
        y_points = []
        for x_point in range(-15, 15, 1):
            y_point_1 = a1 * x_point ** 2 + b1 * x_point + c1
            if float(y_point_1).is_integer() and (-15 < y_point_1 < 15):
                x_points.append(x_point)
                y_points.append(y_point_1)
            y_point_2 = a2 * x_point ** 2 + b2 * x_point + c2
            if float(y_point_2).is_integer() and (-15 < y_point_2 < 15):
                x_points.append(x_point)
                y_points.append(y_point_2)
        coef = [a1, b1, c1, a2, b2, c2]
        return x_coord, y_coord, x_points, y_points, intersection, coef

    def function_result():
        """Функция генерирует задание, выводит правильный ответ и график"""
        x_coord, y, x_points, y_points, intersection, coef = input_parameters()

        def signs_of_digits():
            str_digits = []
            for digit in coef:
                if str(digit).find("-") != -1:
                    digit = ' ' + ((str(digit))[0]) + ' ' + ((str(digit))[1:])
                else:
                    digit = ' + ' + (str(digit))[0:]
                str_digits.append(digit)
            equation2 = f'g(x)= {coef[3]}x^2{str_digits[4]}x{str_digits[5]}'
            if coef[0] == 1:
                equation1 = f'f(x)= x^2{str_digits[1]}x{str_digits[2]}'
            elif coef[0] == -1:
                equation1 = f'f(x)= -x^2{str_digits[1]}x{str_digits[2]}'
            else:
                equation1 = f'f(x)= {coef[0]}x^2{str_digits[1]}x{str_digits[2]}'
            return str_digits, equation1, equation2

        tr_digits, equation1, equation2 = signs_of_digits()

        if intersection[1][1] > 10 or intersection[1][1] < -10:
            point_B = [intersection[1][0], intersection[1][1]]
            point_A = [intersection[0][0], intersection[0][1]]
        else:
            point_A = [intersection[1][0], intersection[1][1]]
            point_B = [intersection[0][0], intersection[0][1]]
        solution = None
        task_random = randint(0, 1)
        if task_random == 1:
            answer = point_B[1]
            axis = f'ординату'
        else:
            answer = point_B[0]
            axis = f'абсциссу'
        task = f'На рисунке изображены графики функций \({equation1}\) и \(g(x) = ax^2 + bx + c\), которые пересекаются в точках A и B. Найдите {axis} точки B.'
        lim = [[point_A[0] - 9, point_A[0] + 9], [point_A[1] - 9, point_A[1] + 9]]

        paint = function_graph(x_coord, y, x_points, y_points, point_A, lim)
            
        return answer, task, paint, solution

    answer, task, paint, solution = function_result()
    return {
        "condition": task,
        "answer": answer,
        "image": paint,
        "solution": solution
        }


# Задача 3 №562285 c сайта https://math-ege.sdamgia.ru/problem?id=562285
# Парабола вида y = a * x ** 2 + b * x + c
def single_parabola_1():
    def input_parameters():
        """Функция формирует две точки, через которые строится парабола"""
        while True:
            x1, y1, x2, y2 = np.random.randint(-4, 5, size=4)  # parabola_vertex = (x1, y1) #parabola_point = (x2, y2)
            if (x2 - x1) != 0 and (y2 - y1) != 0:
                a = (y2 - y1) / ((x2 - x1) ** 2)
                if float(a).is_integer():
                    a = int(a)
                    if a != 0:
                        b = int(-2 * a * x1)
                        c = int(y2 - a * x2 ** 2 - b * x2)
                        x = np.linspace(x1 - 3, x1 + 3, 100)
                        y = [a * x ** 2 + b * x + c]
                        x = [x]
                        break
        if a > 0:
            ylim = [y1 - 3, y1 + 7]
        else:
            ylim = [y1 - 7, y1 + 3]
        xlim = [x1 - 5, x1 + 5]
        lim = [xlim, ylim]
        coef = [a, b, c]
        x_points = []
        y_points = []
        for x_point in range(x1 - 3, x1 + 3):
            y_point = a * x_point ** 2 + b * x_point + c
            if float(y_point).is_integer():
                x_points.append(x_point)
                y_points.append(y_point)
        return x, y, coef, x_points, y_points, lim

    def function_result():
        """Функция генерирует задание, выводит правильный ответ и график"""
        x, y, coef, x_points, y_points, lim = input_parameters()
        x_task = randint(-5, 5)
        answer = (coef[0] * x_task ** 2 + coef[1] * x_task + coef[2])
        task = f'Вычислите \(f({x_task})\) для функции вида \(f(x) = ax^2 + bx + c\)'

        paint = function_graph(x, y, x_points, y_points, lim=lim)

        solution = None
        return answer, task, paint, solution

    answer, task, paint, solution = function_result()
    return {
        "condition": task,
        "answer": answer,
        "image": paint,
        "solution": solution
    }


# Задача 4 https://math-ege.sdamgia.ru/problem?id=562061
# Парабола вида y = (x ** 2) / a + b * x + c
def single_parabola_2():
    def input_parameters():
        """Функция формирует две точки, через которые строится парабола"""
        while True:
            x1, y1 = np.random.randint(-3, 4, size=2)
            x2, y2 = np.random.randint(x1 - 5, x1 + 6, size=2)
            if (x2 - x1) != 0 and (y2 - y1) != 0:
                a = ((y2 - y1) / ((x2 - x1) ** 2))
                if a != 0 and a > -1 and a < 1 and float(1 / a).is_integer():
                    b = -2 * a * x1
                    c = y2 - a * x2 ** 2 - b * x2
                    x = np.linspace(x1 - 6, x1 + 6, 400)
                    y = [a * x ** 2 + b * x + c]
                    x = [x]
                    break
        if a > 0:
            ylim = [y1 - 3, y1 + 7]
        else:
            ylim = [y1 - 7, y1 + 3]
        xlim = [x1 - 5, x1 + 5]
        lim = [xlim, ylim]
        coef = [a, b, c]
        x_points = []
        y_points = []
        for x_point in range(-15, 15):
            y_point = a * x_point ** 2 + b * x_point + c
            if float(y_point).is_integer():
                x_points.append(x_point)
                y_points.append(y_point)
        return x, y, coef, x_points, y_points, lim

    def function_result():
        """Функция генерирует задание, выводит правильный ответ и график"""
        x, y, coef, x_points, y_points, lim = input_parameters()
        while True:
            x_task = randint(-40, 40)
            answer = coef[0] * x_task ** 2 + coef[1] * x_task + coef[2]
            if (-10 > answer or answer > 10) and float(answer).is_integer():
                answer = int(answer)
                break
        task = f'На рисунке изображён график функции вида \(f(x) = \\frac{{x^2}}{{a}} + bx + c\), где числа a, b и c — целые. Найдите значение уравнения при \(f({x_task})\). '
        solution = None

        paint = function_graph(x, y, x_points, y_points, lim=lim)

        return answer, task, paint, solution

    answer, task, paint, solution = function_result()
    return {
        "condition": task,
        "answer": answer,
        "image": paint,
        "solution": solution
        }


# Задача 5 https://math-ege.sdamgia.ru/problem?id=508903
# одна прямая вида f(x) = kx + b
def single_line():
    def input_parameters():
        while True:
            x1, y1, x2, y2 = np.random.randint(-8, 9, size=4)
            if x1 != x2 and y1 != y2:
                x = np.linspace(-9, 9, 50)
                if (x2 - x1) != 0:
                    y = [(((x - x1) * (y2 - y1)) / (x2 - x1)) + y1]
                    x = [x]
                    a = y2 - y1
                    b = x1 - x2
                    c = (y1 * x2) - (x1 * y2)
                    break
        x_points, y_points = [[x1, x2], [y1, y2]]
        coef = [a, b, c]
        return x, y, x_points, y_points, coef

    def function_result():
        """Функция генерирует задание, выводит правильный ответ и график"""
        x, y, x_points, y_points, coef = input_parameters()
        task_random = randint(0, 1)
        while True:
            x_y_random = choice(list(set([x for x in range(-50, 50)]) - set([x for x in range(-8, 8)])))
            if task_random == 1:
                task = f'На рисунке изображён график функции \(f(x) = kx + b\). Найдите значение x, при котором \(f(x) = {x_y_random}\).'  # ордината - y
                answer = (-coef[1] * x_y_random - coef[2]) / coef[0]
                if float(answer).is_integer():
                    answer = int(answer)
                    break
            else:
                task = f'На рисунке изображён график функции \(f(x) = kx + b\). Найдите значение \(f({x_y_random})\).'  # абсцисса - x
                answer = (-coef[1] * x_y_random - coef[2]) / coef[0]
                if float(answer).is_integer():
                    answer = int(answer)
                    break
        solution = None

        paint = function_graph(x, y, x_points, y_points)

        return answer, task, paint, solution

    answer, task, paint, solution = function_result()
    return {
        "condition": task,
        "answer": answer,
        "image": paint,
        "solution": solution
        }


# Задача 6 https://math-ege.sdamgia.ru/problem?id=635152
# Парабола вида y = |a * x ** 2 + b * x + c|
def abs_parabola():
    def input_parameters():
        """Функция формирует две точки, через которые строится парабола"""
        while True:
            x1, x2, y2 = np.random.randint(-7, 8, size=3)
            y1 = randint(-5, -1)
            if (x2 - x1) != 0 and (y2 - y1) !=0:
                a = float((y2 - y1) / ((x2 - x1) ** 2))
                if a.is_integer() and a > 0:
                    a = int(a)
                    b = int(-2 * a * x1)
                    c = int(y2 - a * x2 ** 2 - b * x2)
                    x = np.linspace(x1 - 10, x1 + 10, 400)
                    y = [abs(a * x ** 2 + b * x + c)]
                    x = [x]
                    break
        lim = [[(x1 - 7), (x1 + 7)], [(abs(y1) - 6), (abs(y1) + 9)]]
        x_points, y_points = [x1, x2], [abs(y1), abs(y2)]
        coef = [a, b, c]
        return x, y, x_points, y_points, lim, coef

    def function_result():
        """Функция генерирует задание, выводит правильный ответ и график"""
        x, y, x_points, y_points, lim, coef = input_parameters()
        x_task = randint(-5, 5)
        answer = (abs(coef[0] * x_task ** 2 + coef[1] * x_task + coef[2]))
        task = f'На рисунке изображён график фуıкции вида \(f(x) = |ax^2 + bx + c|\), где a, b и c — целые числа. Вычислите \(f({x_task})\).'
        solution = None

        paint = function_graph(x, y, x_points, y_points, lim=lim)

        return answer, task, paint, solution

    answer, task, paint, solution = function_result()
    return {
        "condition": task,
        "answer": answer,
        "image": paint,
        "solution": solution
        }


# Задача 7 https://math-ege.sdamgia.ru/problem?id=508971
# Гипербола вида y = k / (x + a)
def giperbola_1():
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
        x_points = []
        y_points = []
        for x_point in range(-20, 20):
            if (x_point + a) != 0 and float(k / (x_point + a)).is_integer():
                y_points.append(k / (x_point + a))
                x_points.append(x_point)
        coef = [a, k]
        lim = [[-a - 10, -a + 10], [-10, 10]]
        x_coord, y_coord = [x1, x2], [y1, y2]
        dash = [[[int(-a), int(-a)],[int(-a) - 50, int(-a) + 50]]]
        color = ['orange', 'orange']
        return x_coord, y_coord, x_points, y_points, lim, dash, coef, color

    def function_result():
      """Функция генерирует задание, выводит правильный ответ и график"""
      x_coord, y_coord, x_points, y_points, lim, dash, coef, color = input_parameters()
      while True:
        x_task = randint(-60, 60)
        if (x_task + coef[0]) != 0:
          y_task = coef[1] / (x_task + coef[0])
          if (y_task % 0.025 == 0 or y_task % 0.003125 == 0) and not float(y_task).is_integer():
            break
      random_task = randint(0,1)
      if random_task == 1:
        task = f'На рисунке изображён график функции вида \(f(x) = \\frac{{k}}{{x + a}}\). Найдите значение \(f({x_task})\)'
        answer = y_task
      else:
        task = f'На рисунке изображён график функции вида \(f(x) = \\frac{{k}}{{x + a}}\). Найдите значение x, при котором \(f(x) = {y_task}\)'
        answer = x_task
      solution = None

      paint = function_graph(x_coord, y_coord, x_points, y_points, lim=lim, dash=dash, color=color)

      return answer, task, paint, solution
    
    answer, task, paint, solution = function_result()
    return {
        "condition": task,
        "answer": answer,
        "image": paint,
        "solution": solution
        }


# Задача 8 https://math-ege.sdamgia.ru/problem?id=508961
# Гипербола вида y = (k / x) + a
def giperbola_2():
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
        x_points = []
        y_points = []
        for x_point in range(-20, 20):
            if x_point != 0 and float((k / x_point) + a).is_integer():
                y_points.append((k / x_point) + a)
                x_points.append(x_point)
        coef = [a, k]
        lim = [[-10, 10], [-10 + a, 10 + a]]
        x_coord, y_coord = [x1, x2], [y1, y2]
        dash = [[[int(a) - 50, int(a) + 50], [int(a), int(a)]]]
        color = ['orange', 'orange']
        return x_coord, y_coord, x_points, y_points, lim, dash, coef, color

    def function_result():
        """Функция генерирует задание, выводит правильный ответ и график"""
        x_coord, y_coord, x_points, y_points, lim, dash, coef, color = input_parameters()
        while True:
            y_task = randint(-100, 100)
            if y_task - coef[0] != 0:
                x_task = coef[1] / (y_task - coef[0])
                if (x_task % 0.025 == 0 or x_task % 0.003125 == 0) and not float(x_task).is_integer():
                    break
        random_task = randint(0, 1)
        if random_task == 1:
            task = f'На рисунке изображён график функции вида \(f(x) = \\frac{{k}}{{x}} + a\). Найдите значение \(f({x_task})\)'
            answer = y_task
        else:
            task = f'На рисунке изображён график функции вида \(f(x) = \\frac{{k}}{{x}} + a\). Найдите значение x, при котором \(f(x) = {y_task}\)'
            answer = x_task
        solution = None

        paint = function_graph(x_coord, y_coord, x_points, y_points, lim=lim, dash=dash, color=color)

        return answer, task, paint, solution

    answer, task, paint, solution = function_result()
    return {
        "condition": task,
        "answer": answer,
        "image": paint,
        "solution": solution
        }


# Задача 9 https://math-ege.sdamgia.ru/problem?id=564963
# Гипербола вида y = (ax + b) / (x + c)
def giperbola_3():
    def input_parameters():
        """Функция формирует точки, через которые строится график"""
        break_out_flag = True
        while break_out_flag:
            a, b, c = np.random.randint(-3, 4, size=3)
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
        x_points = []
        y_points = []
        for x_point in range(-20, 20):
            if (x_point + c) != 0 and float((a * x_point + b) / (x_point + c)).is_integer():
                y_points.append((a * x_point + b) / (x_point + c))
                x_points.append(x_point)
        coef = [a, b, c]
        lim = [[-10 - c, 10 - c], [-10 + a, 10 + a]]
        x_coord, y_coord = [x1, x2], [y1, y2]
        dash = [[[int(a) - 50, int(a) + 50], [int(a), int(a)]], [[int(-c), int(-c)], [int(-c) - 50, int(-c) + 50]]]
        color = ['orange', 'orange']
        return x_coord, y_coord, x_points, y_points, lim, dash, coef, color


    def function_result():
        """Функция генерирует задание, выводит правильный ответ и график"""
        x_coord, y_coord, x_points, y_points, lim, dash, coef, color = input_parameters()

        paint = function_graph(x_coord, y_coord, x_points, y_points, lim=lim, dash=dash, color=color)

        random_task = randint(0, 4)
        if random_task == 0:
            task = f'На рисунке изображён график функции вида \(f(x) = \\frac{{ax + b}}{{x + c}}\), где числа a, b и c — целые. Найдите значение a.'
            answer = coef[0]
        elif random_task == 1:
            task = f'На рисунке изображён график функции вида \(f(x) = \\frac{{ax + b}}{{x + c}}\), где числа a, b и c — целые. Найдите значение c.'
            answer = coef[2]
        elif random_task == 2:
            task = f'На рисунке изображён график функции вида \(f(x) = \\frac{{kx + a}}{{x + b}}\). Найдите значение k.'
            # k, a, b = a, b, c
            answer = coef[0]
        else:
            task = f'На рисунке изображён график функции вида \(f(x) = \\frac{{ax + b}}{{x + c}}\), Найдите значение b.'
            # k, a, b = a, b, c
            answer = coef[2]
        solution = None

        return answer, task, paint, solution

    answer, task, paint, solution = function_result()
    if answer % 1 == 0:
        answer = int(answer)
    else:
        answer = float(answer)
    return {
        "condition": task,
        "answer": answer,
        "image": paint,
        "solution": solution
        }


# Задача 10 https://math-ege.sdamgia.ru/problem?id=509113
# Функция вида f(x) = k*sqrt(x)
def sqrt():
    def input_parameters():
        """Функция формирует точки, через которые строится график"""
        while True:
            k = randint(-10, 10)
            if k != 0:
                x_coord = np.linspace(0.00001, 20, 400)
                y_coord = [k * (x_coord ** 0.5)]
                x_coord = [x_coord]
                break
        x_points = []
        y_points = []
        for x_point in range(2, 20):
            y_point = k * (x_point ** 0.5)
            if float(y_point).is_integer():
                y_points.append(y_point)
                x_points.append(x_point)
        if k > 0:
            lim = [[0, 10], [0, 10]]
        else:
            lim = [[0, 10], [-10, 0]]
        coef = [k]
        return x_coord, y_coord, x_points, y_points, lim, coef

    def function_result():
        """Функция генерирует задание, выводит правильный ответ и график"""
        x_coord, y_coord, x_points, y_points, lim, coef = input_parameters()
        while True:
            x_task = (d.Decimal(str(randint(1, 3))) + d.Decimal(str(randrange(1, 10, 1))) / d.Decimal(
                str(10))) ** d.Decimal(str(2))
            y_task = (d.Decimal(str(coef[0])) * (x_task ** d.Decimal(str(0.5)))).quantize(d.Decimal("1.00"))
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

        paint = function_graph(x_coord, y_coord, x_points, y_points, lim=lim)

        return answer, task, paint, solution

    answer, task, paint, solution = function_result()
    return {
        "condition": task,
        "answer": answer,
        "image": paint,
        "solution": solution
        }


# Задача 11 https://math-ege.sdamgia.ru/problem?id=509009
# Логарифмическая функция f(x)=b + loga(x)
def logarythm_1():
    def input_parameters():
        """Функция формирует точки, через которые строится график"""
        while True:
            a = randint(3, 10)
            b = randint(-5, 5)
            if a != 0:
                x_coord = list(np.linspace(0.00001, 20, 400))
                for numb in x_coord:
                    if numb + a == 0:
                        x_coord.remove(numb)
                    else:
                        y_coord = [b + m.log(numb, a) for numb in x_coord]
                x_coord, y_coord = [x_coord], [y_coord]
                break
        coef = [a, b]
        x_points = []
        y_points = []
        for x_point in range(1, 10):
            if (b + m.log(x_point, a)).is_integer():
                y_points.append(b + m.log(x_point, a))
                x_points.append(x_point)
        lim = [[0, 11], [b - 5, b + 5]]
        return x_coord, y_coord, x_points, y_points, lim, coef

    def function_result():
        """Функция генерирует задание, выводит правильный ответ и график"""
        x_coord, y_coord, x_points, y_points, lim, coef = input_parameters()
        while True:
            x_task = d.Decimal(randint(10, 300))
            y_task = d.Decimal(coef[1]) + d.Decimal(m.log(x_task, d.Decimal(coef[0])))
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

        paint = function_graph(x_coord, y_coord, x_points, y_points, lim=lim)

        return answer, task, paint, solution

    answer, task, paint, solution = function_result()
    return {
        "condition": task,
        "answer": answer,
        "image": paint,
        "solution": solution
        }


# Задача 12 https://math-ege.sdamgia.ru/problem?id=509042
# Логарифмическая функция f(x)=loga(x + b)
def logarythm_2():
    def input_parameters():
        """Функция формирует точки, через которые строится график"""
        while True:
            b = randint(1, 7)
            a = randint(2, 10 - b)
            if a != 0:
                x_coord = list(np.linspace(-b + 0.00001, 20, 400))
                y_coord = [m.log((b + numb), a) for numb in x_coord]
                x_coord, y_coord = [x_coord], [y_coord]
                break
        coef = [a, b]
        x_points = []
        y_points = []
        for x_point in range(-b + 2, 11):
            if (m.log((x_point + b), a)).is_integer():
                y_points.append(m.log((x_point + b), a))
                x_points.append(x_point)
        lim = [[-b - 1, -b + 11], [-5, 5]]
        return x_coord, y_coord, x_points, y_points, lim, coef

    def function_result():
        """Функция генерирует задание, выводит правильный ответ и график"""
        x_coord, y_coord, x_points, y_points, lim, coef = input_parameters()
        while True:
            x_task = randint(coef[1] + 10, 500)
            y_task = m.log((x_task + coef[1]), coef[0])
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

        paint = function_graph(x_coord, y_coord, x_points, y_points, lim=lim)

        return answer, task, paint, solution

    answer, task, paint, solution = function_result()
    return {
        "condition": task,
        "answer": answer,
        "image": paint,
        "solution": solution
        }


# Задача 13 https://math-ege.sdamgia.ru/problem?id=639672
# Логарифмическая функция f(x)=loga(x)
def logarythm_3():
    def input_parameters():
        """Функция формирует точки, через которые строится график"""
        while True:
            a = randint(2, 10)
            if a != 0:
                x_coord = list(np.linspace(0.00001, 15, 300))
                y_coord = [m.log((numb), a) for numb in x_coord]
                x_coord, y_coord = [x_coord], [y_coord]
                break
        coef = [a]
        x_points = []
        y_points = []
        for x_point in range(1, 10):
            if (m.log((x_point), a)).is_integer():
                y_points.append(m.log((x_point), a))
                x_points.append(x_point)
        lim = [[0, 10], [-5, 5]]
        return x_coord, y_coord, x_points, y_points, lim, coef

    def function_result():
        """Функция генерирует задание, выводит правильный ответ и график"""
        x_coord, y_coord, x_points, y_points, lim, coef = input_parameters()
        while True:
            x_task = randint(10, 500)
            y_task = m.log((x_task), coef[0])
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

        paint = function_graph(x_coord, y_coord, x_points, y_points, lim=lim)

        return answer, task, paint, solution

    answer, task, paint, solution = function_result()
    return {
        "condition": task,
        "answer": answer,
        "image": paint,
        "solution": solution
        }


# Задача 14 https://math-ege.sdamgia.ru/problem?id=509089
# Логарифмическая функция f(x) = a^x + b
def exponent_1():
    def input_parameters():
        """Функция формирует точки, через которые строится график"""
        while True:
            b = randint(-6, 2)
            a = randint(2, b + 7)
            if a != 0 and b != 0:
                x_coord = np.linspace(-20, 20, 400)
                y_coord = [a ** x_coord + b]
                x_coord = [x_coord]
                break
        coef = [a, b]
        x_points = []
        y_points = []
        for x_point in range(1, 11):
            if float((a**x_point + b)).is_integer():
                y_points.append(a**x_point + b)
                x_points.append(x_point)
        lim = [[-5, 5], [b - 2, b + 8]]
        return x_coord, y_coord, x_points, y_points, lim, coef

    def function_result():
        """Функция генерирует задание, выводит правильный ответ и график"""
        x_coord, y_coord, x_points, y_points, lim, coef = input_parameters()
        while True:
            x_task = randint(3, 7)
            y_task = coef[0] ** x_task + coef[1]
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

        paint = function_graph(x_coord, y_coord, x_points, y_points, lim=lim)

        return answer, task, paint, solution

    answer, task, paint, solution = function_result()
    return {
        "condition": task,
        "answer": answer,
        "image": paint,
        "solution": solution
        }


# Задача 15 https://math-ege.sdamgia.ru/problem?id=509101
# Логарифмическая функция f(x) = a^(x + b)
def exponent_2():
    def input_parameters():
        """Функция формирует точки, через которые строится график"""
        while True:
            b = randint(-5, 4)
            a = randint(2, 8)
            if a != 0 and b != 0:
                x_coord = np.linspace(-20, 20, 400)
                y_coord = [a ** (x_coord + b)]
                x_coord = [x_coord]
                break
        coef = [a, b]
        x_points = []
        y_points = []
        for x_point in range(-b, -b + 11):
            if float(a**(x_point + b)).is_integer():
                y_points.append(a**(x_point + b))
                x_points.append(x_point)
        lim = [[-b - 5, -b + 5], [-1, 9]]
        return x_coord, y_coord, x_points, y_points, lim, coef

    def function_result():
        """Функция генерирует задание, выводит правильный ответ и график"""
        x_coord, y_coord, x_points, y_points, lim, coef = input_parameters()
        while True:
            x_task = d.Decimal(randint(-coef[1] - 4, -coef[1] + 15))
            y_task = d.Decimal(d.Decimal(coef[0]) ** (x_task + d.Decimal(coef[1])))
            if x_task < -coef[1] and (
                    y_task % d.Decimal(0.0625) == 0 or y_task % d.Decimal(0.015625) == 0 or y_task % d.Decimal(
                    0.01) == 0):
                break
            elif x_task > -coef[1] + 3 and float(y_task).is_integer() and y_task < d.Decimal(10000):
                break
        random_task = randint(0, 1)
        if random_task == 1:
            task = f'На рисунке изображён график функции \(f(x)=a^{{x + b}}\). Найдите \(f({x_task})\).'
            answer = y_task
        else:
            task = f'На рисунке изображён график функции \(f(x)=a^{{x + b}}\). Найдите значение \(x\), при котором \(f(x) = {y_task}\).'
            answer = x_task
        solution = None

        paint = function_graph(x_coord, y_coord, x_points, y_points, lim=lim)

        return answer, task, paint, solution

    answer, task, paint, solution = function_result()
    return {
        "condition": task,
        "answer": answer,
        "image": paint,
        "solution": solution
        }


# Задача 16 https://math-ege.sdamgia.ru/problem?id=639480
# Логарифмическая функция f(x) = a^x
def exponent_3():
    def input_parameters():
        """Функция формирует точки, через которые строится график"""
        while True:
            a = choice([0.5, 1, 2, 3, 4, 5, 6, 7, 8])
            if a != 0 and a != 1:
                x_coord = np.linspace(-10, 10, 400)
                y_coord = [a ** (x_coord)]
                x_coord = [x_coord]
                break
        coef = [a]
        x_points = []
        y_points = []
        for x_point in range(-5, 5):
            if float(a**(x_point)).is_integer():
                y_points.append(a**(x_point))
                x_points.append(x_point)
        lim = [[- 5, 5], [-1, 9]]
        return x_coord, y_coord, x_points, y_points, lim, coef

    def function_result():
        """Функция генерирует задание, выводит правильный ответ и график"""
        x_coord, y_coord, x_points, y_points, lim, coef = input_parameters()
        while True:
            x_task = d.Decimal(randint(-8, 8))
            y_task = d.Decimal(d.Decimal(coef[0]) ** (x_task))
            if x_task != 0 and x_task != 1 and (
                    y_task % d.Decimal(0.0625) == 0 or y_task % d.Decimal(0.015625) == 0 or y_task % d.Decimal(
                    0.01) == 0) and y_task < 10000:
                break
        random_task = randint(0, 1)
        if random_task == 1:
            task = f'На рисунке изображён график функции \(f(x)=a^x\). Найдите \(f({x_task})\).'
            answer = y_task
        else:
            task = f'На рисунке изображён график функции \(f(x)=a^x\). Найдите значение \(x\), при котором \(f(x) = {y_task}\).'
            answer = x_task
        solution = None

        paint = function_graph(x_coord, y_coord, x_points, y_points, lim=lim)

        return answer, task, paint, solution

    answer, task, paint, solution = function_result()
    return {
        "condition": task,
        "answer": answer,
        "image": paint,
        "solution": solution
        }


# Задача 17 https://math-ege.sdamgia.ru/problem?id=509123
# Триганометрическая функция f(x) = acosx + b
def trigonometric_1():
    def input_parameters():
        """Функция формирует точки, через которые строится график"""
        a = choice([0.5, 1.5, 2])
        b = choice([-1.5, -1, -0.5, 0.5, 1, 1.5])
        x_coord = np.linspace(-2*np.pi,2*np.pi,600,endpoint=True)
        y_coord = [a*np.cos(x_coord) + b]
        x_coord = [x_coord]
        coef = [a, b]
        x_points = []
        y_points = []
        for x_point in [0, -np.pi / 2, np.pi]:
            x_points.append(x_point)
            y_points.append(a * np.cos(x_point) + b)
        lim = [[-7*np.pi/4, 7*np.pi/4], [-3.5, 3.5]]
        return x_coord, y_coord, x_points, y_points, lim, coef

    def function_result():
        """Функция генерирует задание, выводит правильный ответ и график"""
        x_coord, y_coord, x_points, y_points, lim, coef = input_parameters()
        random_task = randint(0, 1)
        if random_task == 1:
            task = f'На рисунке изображён график функции \(f(x)=acosx + b\). Найдите \(a\)).'
            answer = coef[0]
        else:
            task = f'На рисунке изображён график функции \(f(x)=acosx + b\). Найдите \(b\).'
            answer = coef[1]
        solution = None

        paint = function_graph(x_coord, y_coord, x_points, y_points, lim=lim, trigonometry=True)

        return answer, task, paint, solution

    answer, task, paint, solution = function_result()
    return {
        "condition": task,
        "answer": answer,
        "image": paint,
        "solution": solution
        }


# Задача 18 https://math-ege.sdamgia.ru/problem?id=509287
# Триганометрическая функция f(x) = asinx + b
def trigonometric_2():
    def input_parameters():
        """Функция формирует точки, через которые строится график"""
        a = choice([0.5, 1.5, 2])
        b = choice([-1.5, -1, -0.5, 0.5, 1, 1.5])
        x_coord = np.linspace(-2*np.pi,2*np.pi,600,endpoint=True)
        y_coord = [a*np.sin(x_coord) + b]
        x_coord = [x_coord]
        coef = [a, b]
        x_points = []
        y_points = []
        for x_point in [0, -np.pi / 2, np.pi]:
            x_points.append(x_point)
            y_points.append(a * np.sin(x_point) + b)
        lim = [[-7*np.pi/(4), 7*np.pi/(4)], [-3.5, 3.5]]
        return x_coord, y_coord, x_points, y_points, lim, coef

    def function_result():
        """Функция генерирует задание, выводит правильный ответ и график"""
        x_coord, y_coord, x_points, y_points, lim, coef = input_parameters()
        random_task = randint(0, 1)
        if random_task == 1:
            task = f'На рисунке изображён график функции \(f(x)=asinx + b\). Найдите \(a\)).'
            answer = coef[0]
        else:
            task = f'На рисунке изображён график функции \(f(x)=asinx + b\). Найдите \(b\).'
            answer = coef[1]
        solution = None

        paint = function_graph(x_coord, y_coord, x_points, y_points, lim=lim, trigonometry=True)

        return answer, task, paint, solution

    answer, task, paint, solution = function_result()
    return {
        "condition": task,
        "answer": answer,
        "image": paint,
        "solution": solution
        }


# Задача 19 https://math-ege.sdamgia.ru/problem?id=509143
# Триганометрическая функция f(x) = atanx + b
def trigonometric_3():
    def input_parameters():
        """Функция формирует точки, через которые строится график"""
        a = choice([-2, -1.5, -0.5, 0.5, 1.5, 2])
        b = choice([-1.5, -1, -0.5, 0.5, 1, 1.5])
        x1 = np.linspace(-5 * np.pi / 2 + 0.0001, -3 * np.pi / 2 - 0.0001, 200, endpoint=True)
        x2 = np.linspace(-3 * np.pi / 2 + 0.0001, -np.pi / 2 - 0.0001, 200, endpoint=True)
        x3 = np.linspace(-np.pi / 2 + 0.0001, np.pi / 2 - 0.0001, 200, endpoint=True)
        x4 = np.linspace(np.pi / 2 + 0.0001, 3 * np.pi / 2 - 0.0001, 200, endpoint=True)
        x5 = np.linspace(3 * np.pi / 2 + 0.0001, 5 * np.pi / 2 - 0.0001, 200, endpoint=True)
        y1, y2, y3, y4, y5 = a * np.tan(x1) + b, a * np.tan(x2) + b, a * np.tan(x3) + b, a * np.tan(x4) + b,  a * np.tan(x5) + b
        x1, x2, x3, x4, x5, y1, y2, y3, y4, y5 = [list(val) for val in [x1, x2, x3, x4, x5, y1, y2, y3, y4, y5]]
        x_coord, y_coord = [x1, x2, x3, x4, x5], [y1, y2, y3, y4, y5]
        coef = [a, b]
        x_points = []
        y_points = []
        for x_point in [-np.pi / 4, np.pi / 4]:
            x_points.append(x_point)
            y_points.append(a * np.tan(x_point) + b)
        lim = [[-7*np.pi/4, 7*np.pi/4], [-3.5, 3.5]]
        dash = []
        y_dash = [-50, 50]
        for x_dash in [[-3 * np.pi / 2, -3 * np.pi / 2], [-np.pi / 2, -np.pi / 2], [np.pi / 2, np.pi / 2],
                       [3 * np.pi / 2, 3 * np.pi / 2]]:
            dash.append([x_dash, y_dash])
        color = ['orange', 'orange', 'orange', 'orange', 'orange']
        return x_coord, y_coord, x_points, y_points, lim, dash, coef, color

    def function_result():
        """Функция генерирует задание, выводит правильный ответ и график"""
        x_coord, y_coord, x_points, y_points, lim, dash, coef, color = input_parameters()
        random_task = randint(0, 1)
        if random_task == 1:
            task = f'На рисунке изображён график функции \(f(x)=atgx + b\). Найдите \(a\)).'
            answer = coef[0]
        else:
            task = f'На рисунке изображён график функции \(f(x)=atgx + b\). Найдите \(b\).'
            answer = coef[1]
        solution = None

        paint = function_graph(x_coord, y_coord, x_points, y_points, lim=lim, dash=dash, trigonometry=True, color=color)

        return answer, task, paint, solution

    answer, task, paint, solution = function_result()
    return {
        "condition": task,
        "answer": answer,
        "image": paint,
        "solution": solution
        }


# Задача 20 https://math-ege.sdamgia.ru/problem?id=509149
# пересечение параболы и прямой
def line_and_parab():
    def input_parameters():
        """Функция формирует точки, через которые строится график"""
        while True:
            a, b, c, k, d = np.random.randint(-6, 7, size=5)
            if a != 0 and b != 0 and c != 0 and k != 0 and d != 0:
                eq1 = (a * x ** 2 + b * x + c - y)
                eq2 = (k * x + d - y)
                solution = solve([eq1, eq2], x, y, dict=True)
                if len(solution) == 2:
                    x_int_1, y_int_1 = solution[0].get(x), solution[0].get(y)
                    x_int_2, y_int_2 = solution[1].get(x), solution[1].get(y)
                    if (x_int_1 % 0.025 == 0 or x_int_1 % 0.03125 == 0) and (
                            x_int_2 % 0.025 == 0 or x_int_2 % 0.03125 == 0) and (
                            y_int_1 % 0.025 == 0 or y_int_1 % 0.03125 == 0) and (
                            y_int_2 % 0.025 == 0 or y_int_2 % 0.03125 == 0):
                        if ((y_int_2 > 20 or y_int_2 < -20) and (-10 < y_int_1 < 10)) or (
                                (y_int_1 > 20 or y_int_1 < -20) and (-10 < y_int_2 < 10)):
                            break
        x_int_1, y_int_1, x_int_2, y_int_2 = [(int(param) if (float(param).is_integer()) else float(param)) for param in
                                              (x_int_1, y_int_1, x_int_2, y_int_2)]
        intersection = [[x_int_1, y_int_1], [x_int_2, y_int_2]]
        x_coords = np.linspace(-15, 15, 250)
        y_coord = [list(a * x_coords ** 2 + b * x_coords + c), list(k * x_coords + d)]
        x_coord = [list(x_coords), list(x_coords)]
        coef = [a, b, c, k, d]
        lim = [[-9, 9], [-9, 9]]
        x_points = []
        y_points = []
        for x_point in range(-10, 10, 2):
            y_point_1 = a * x_point ** 2 + b * x_point + c
            if float(y_point_1).is_integer():
                x_points.append(x_point)
                y_points.append(y_point_1)
            y_point_2 = k * x_point + d
            if float(y_point_2).is_integer():
                x_points.append(x_point)
                y_points.append(y_point_2)
        return x_coord, y_coord, x_points, y_points, lim, coef, intersection


    def function_result():
        """Функция генерирует задание, выводит правильный ответ и график"""
        x_coord, y_coord, x_points, y_points, lim, coef, intersection = input_parameters()
        if intersection[1][1] > 10 or intersection[1][1] < -10:
            point_B = [intersection[1][0], intersection[1][1]]
            point_A = [intersection[0][0], intersection[0][1]]
        else:
            point_A = [intersection[1][0], intersection[1][1]]
            point_B = [intersection[0][0], intersection[0][1]]
        task_random = randint(0, 1)
        if task_random == 1:
            answer = point_B[1]
            task = f'На рисунке изображены графики функций \(f(x) = kx + d\) и \(g(x) = ax^2 + bx + c\). Найдите ординату точки пересечения графиков.'  # ордината - y
        else:
            answer = point_B[0]
            task = f'На рисунке изображены графики функций \(f(x) = kx + d\) и \(g(x) = ax^2 + bx + c\). Найдите абсциссу точки пересечения графиков.'  # абсцисса  - x

        solution = None

        paint = function_graph(x_coord, y_coord, x_points, y_points, point_A, lim)

        return answer, task, paint, solution

    answer, task, paint, solution = function_result()
    return {
        "condition": task,
        "answer": answer,
        "image": paint,
        "solution": solution
        }


# Задача 21 https://math-ege.sdamgia.ru/problem?id=509167
# пересечение гиперболы и прямой
def line_and_giperbola():
    def input_parameters():
        """Функция формирует точки, через которые строится график"""
        while True:
            a, b, k = np.random.randint(-9, 10, size=3)
            if a != 0 and b != 0 and k != 0:
                eq1 = (a * x + b - y)
                eq2 = (k / x - y)
                solution = solve([eq1, eq2], x, y, dict=True)
                if len(solution) == 2:
                    x_int_1, y_int_1 = solution[0].get(x), solution[0].get(y)
                    x_int_2, y_int_2 = solution[1].get(x), solution[1].get(y)
                    if (x_int_1 % 0.025 == 0 or x_int_1 % 0.03125 == 0) and (
                            x_int_2 % 0.025 == 0 or x_int_2 % 0.03125 == 0) and (
                            y_int_1 % 0.025 == 0 or y_int_1 % 0.03125 == 0) and (
                            y_int_2 % 0.025 == 0 or y_int_2 % 0.03125 == 0):
                        if (x_int_1 < 0 and x_int_2 > 0) or (x_int_2 < 0 and x_int_1 > 0):
                            break
        x_int_1, y_int_1, x_int_2, y_int_2 = [(int(param) if (float(param).is_integer()) else float(param)) for param in
                                              (x_int_1, y_int_1, x_int_2, y_int_2)]
        x_coord_1 = np.linspace(-15, 15, 250)
        x_coord_2 = np.linspace(-15, -0000.1, 250)
        x_coord_3 = np.linspace(0000.1, 15, 250)
        y_coord = [list(a * x_coord_1 + b), list(k / x_coord_2), list(k / x_coord_3)]
        x_coord = [list(x_) for x_ in [x_coord_1, x_coord_2, x_coord_3]]
        coef = [a, b, k]
        if y_int_2 > 10 or y_int_2 < -10:
            point_B = [x_int_2, y_int_2]
            point_A = [x_int_1, y_int_1]
        else:
            point_A = [x_int_2, y_int_2]
            point_B = [x_int_1, y_int_1]
        if point_A[1] > 0:
            lim = [[-3, 11], [-3, 11]]
        else:
            lim = [[-3, 11], [-11, 3]]
        x_points = []
        y_points = []
        for x_point in range(-10, 10, 1):
            if x_point == 0:
                continue
            y_point_1 = a * x_point + b
            if float(y_point_1).is_integer():
                x_points.append(x_point)
                y_points.append(y_point_1)
            y_point_2 = k / x_point
            if float(y_point_2).is_integer():
                x_points.append(x_point)
                y_points.append(y_point_2)
        color = ['blue', 'orange', 'orange']
        return x_coord, y_coord, x_points, y_points, lim, coef, point_A, point_B, color

    def function_result():
        """Функция генерирует задание, выводит правильный ответ и график"""
        x_coord, y_coord, x_points, y_points, lim, coef, point_A, point_B, color = input_parameters()
        task_random = randint(0, 1)
        if task_random == 1:
            answer = point_B[1]
            task = f'На рисунке изображены графики функций \(f(x) = ax + b\) и \(g(x) = \\frac{{k}}{{x}}\). Найдите ординату точки пересечения графиков.'  # ордината - y
        else:
            answer = point_B[0]
            task = f'На рисунке изображены графики функций \(f(x) = ax + b\) и \(g(x) = \\frac{{k}}{{x}}\). Найдите абсциссу точки пересечения графиков.'  # абсцисса - x
        solution = None

        paint = function_graph(x_coord, y_coord, x_points, y_points, point_A, lim, color=color)

        return answer, task, paint, solution

    answer, task, paint, solution = function_result()
    return {
        "condition": task,
        "answer": answer,
        "image": paint,
        "solution": solution
        }


# Задача 22 https://math-ege.sdamgia.ru/problem?id=509279
# пересечение коренной функции и прямой
def line_and_sqrt():
    def input_parameters():
        """Функция формирует точки, через которые строится график"""
        while True:
            a, b, k = np.random.randint(-30, 30, size=3)
            if a != 0 and b != 0 and k != 0:
                eq1 = (k * x + b - y)
                eq2 = (a * x ** 0.5 - y)
                solution = solve([eq1, eq2], x, y, dict=True)
                if len(solution) == 1:
                    x_int_1, y_int_1 = solution[0].get(x), solution[0].get(y)
                    if (x_int_1 % 0.00025 == 0 or x_int_1 % 0.0003125 == 0) and (
                            y_int_1 % 0.00025 == 0 or y_int_1 % 0.0003125 == 0) and (
                            (x_int_1 >= 10) or ((x_int_1 < 10) and (y_int_1 >= 10))):
                        break
        x_int_1, y_int_1 = [(int(param) if (float(param).is_integer()) else float(param)) for param in
                            (x_int_1, y_int_1)]
        x_coord_1 = np.linspace(-15, 15, 250)
        x_coord_2 = np.linspace(0, 15, 250)
        x_coord = [list(x_coord_1), list(x_coord_2)]
        y_first, y_second = list(k * x_coord_1 + b), list(a * (x_coord_2 ** 0.5))
        y_coord = [y_first, y_second]
        coef = [a, b, k]
        point_A = [x_int_1, y_int_1]
        if point_A[1] > 0:
            lim = [[-5, 10], [-5, 10]]
        else:
            lim = [[-5, 10], [-10, 5]]
        x_points = []
        y_points = []
        for x_point in range(-10, 10, 1):
            y_point_1 = k * x_point + b
            if float(y_point_1).is_integer():
                x_points.append(x_point)
                y_points.append(y_point_1)
            if x_point > 0:
                y_point_2 = a * (x_point ** 0.5)
                if float(y_point_2).is_integer():
                    x_points.append(x_point)
                    y_points.append(y_point_2)
        return x_coord, y_coord, x_points, y_points, lim, coef, point_A

    def function_result():
        """Функция генерирует задание, выводит правильный ответ и график"""
        x_coord, y_coord, x_points, y_points, lim, coef, point_A = input_parameters()
        task_random = randint(0, 1)
        if task_random == 1:
            answer = point_A[1]
            task = f'На рисунке изображены графики функций \(f(x) = a\sqrt{{x}}\) и \(g(x) = kx + b\), которые пересекаются в точке \(A\). Найдите ординату точки \(A\).'  # ордината - y
        else:
            answer = point_A[0]
            task = f'На рисунке изображены графики функций ](f(x) = a\sqrt{{x}}\) и \(g(x) = kx + b\), которые пересекаются в точке \(A\). Найдите абсциссу точки \(A\).'   # абсцисса - x

        solution = None

        paint = function_graph(x_coord, y_coord, x_points, y_points, point_A, lim)

        return answer, task, paint, solution

    answer, task, paint, solution = function_result()
    return {
        "condition": task,
        "answer": answer,
        "image": paint,
        "solution": solution
        }
