import random
import numpy as np
import math
import fractions
from sympy import *
import re

def take_derivatives_in_point(prototype):
    '''данная функция находит значение производной функции
     со случайными коэффициентами в точке x_0'''
    x = Symbol('x')
    equation = prototype
    while True:
        pattern = r"\b(?:(?!x)[a-z]+)\b"
        constants = re.findall(pattern, equation)
        constants_values = {}
        for constant in constants:
            constants_values[constant] = random.randint(1, 10)
        symbols_dict = {constant: symbols(constant) for constant in constants}
        substituted_eq = sympify(equation).subs(symbols_dict)
        for constant, value in constants_values.items():
            substituted_eq = substituted_eq.subs(symbols_dict[constant], value)
        a = np.random.randint(1, 100)
        prime = substituted_eq.diff(x)
        trig_functions = ['sin', 'asin', 'cos', 'acos', 'tan', 'atan', 'cot', 'acot']
        pattern_1 = "|".join(trig_functions)
        if random.randint(0, 1) == 0:
            text = r'Найдите значение производной заданной функции: \( y= '
        else:
            text = r'Вычислите скорость изменения функции: \( y= '
        if re.search(pattern_1, equation):
            result = simplify(prime)
            answer = result.subs(x, pi/a)
            task = text + str(latex(substituted_eq)) + r"\) в точке \(x_0 = " + str(
                latex(pi / a) + r"\)")
            if ask(Q.integer(answer*10000)) is True:
                break
        else:
            answer = prime.subs(x, a)
            task = text + str(latex(substituted_eq)) + r"\) в точке \(x_0 = " + str(
                a) + "\)"
            if ask(Q.integer(answer*10000)) is True and abs(answer)<10000:
                break
    answer_float = float(answer)
    return {
      "condition": task,
      "answer": answer_float
    }

'''Задача № 13274 c портала https://kuzovkin.info/one_exercise_1/13274
 Выписать производную в заданной точке (точках) x0:
f(x) = (1 + tg^2(2x))**3, x0 = π/8'''

prototype_13274 = "(1 + (tan(2*x))**2)**3"

'''Задача № 42911 c портала https://kuzovkin.info/one_exercise_1/42911 вида:
 k*(sqrt(x))
 Найдите значение производной заданной функции в точке x0: y = sqrt(x), x0 = 4'''

prototype_42911 = "k*(sqrt(x)) + m*x + n"

'''Задача № 42912 c портала https://kuzovkin.info/one_exercise_1/42912 вида:
 m*(x**k)
 Найдите значение производной заданной функции в точке x0: y = x**2, x0 = −7'''

prototype_42912 = "k*(x**p) + m*x + n"

'''Задача № 42913 c портала https://kuzovkin.info/one_exercise_1/42913 вида:
 -k*x - m
 Найдите значение производной заданной функции в точке x0: y = −3x − 11, x0 = −3'''

prototype_42913 = "k*(x**p) + m*x + n"

'''Задача № 42914 c портала https://kuzovkin.info/one_exercise_1/42914 вида:
 -k*x - m
 Найдите значение производной заданной функции в точке x0: y = 1/x, x0 = 0.5'''

prototype_42914 = "k/x"

'''Задача № 42915 c портала https://kuzovkin.info/one_exercise_1/42915 вида:
 k*sin(m*x)
 Найдите значение производной заданной функции в точке x0: y = sinx, x0 = −π/2'''

prototype_42915 = "k*sin(m*x)"

'''Задача № 42916 c портала https://kuzovkin.info/one_exercise_1/42916 вида:
 k*cos(m*x)
 Найдите значение производной заданной функции в точке x0: y = cosx, x0 = π/6'''

prototype_42916 = "k*cos(m*x)"

'''Задача № 42918 c портала https://kuzovkin.info/one_exercise_1/42918 вида:
 k*sin(m*x)
 Найдите значение производной заданной функции в точке x0: y = sinx, x0 = 0'''

prototype_42918 = "k*sin(m*x)"

'''Задача № 42919 c портала https://kuzovkin.info/one_exercise_1/42919 вида:
 k*x - m
 Найдите значение производной заданной функции в точке x0: y = 6x − 9, x0 = 3'''

prototype_42919 = "k*(x**p) + m*x + n"

'''Задача № 42920 c портала https://kuzovkin.info/one_exercise_1/42920 вида:
 k*(x**3) - (m*x) + n
 Найдите значение производной заданной функции в точке x0: y = x^3 − 3x + 2, x0 = 1'''

prototype_42920 = "k*(x**p) + m*x + n"

'''Задача № 42921 c портала https://kuzovkin.info/one_exercise_1/42921 вида:
 k*x - m
 Найдите значение производной заданной функции в точке x0: y = 5x − 8, x0 = 2'''

prototype_42921 = "k*(x**p) + m*x + n"

'''Задача № 42922 c портала https://kuzovkin.info/one_exercise_1/42922 вида:
 k*(x**2) + (m*x) - n
 Найдите значение производной заданной функции в точке x0: y = x^2 + 3x − 4, x0 = 1'''

prototype_42922 = "k*(x**p) + m*x + n"

'''Задача № 42923 c портала https://kuzovkin.info/one_exercise_1/42923 вида:
 k/x - x/m
 Найдите значение производной заданной функции в точке x0: y = (2/x) − (x/2), x0 = 3'''

prototype_42923 = "k/x - (x**p)/m"

'''Задача № 42924 c портала https://kuzovkin.info/one_exercise_1/42924 вида:
 k*(sqrt(x)) + m
 Найдите значение производной заданной функции в точке x0: y = sqrt(x) + 4, x0 = 9'''

prototype_42924 = "k*(sqrt(x)) + m*x + n"

'''Задача № 42925 c портала https://kuzovkin.info/one_exercise_1/42925 вида:
 k/x - (x**3)/m
 Найдите значение производной заданной функции в точке x0:
 y = (8/x) − ((x^3)/3), x0 = 1'''

prototype_42925 = "k/x - (x**p)/m"

'''Задача № 42926 c портала https://kuzovkin.info/one_exercise_1/42926 вида:
 k*(sqrt(x)) + m*x
 Найдите значение производной заданной функции в точке x0: y = sqrt(x) + 5x, x0 = 4'''

prototype_42926 = "k*(sqrt(x)) + m*x + n"

'''Задача № 42927 c портала https://kuzovkin.info/one_exercise_1/42927 вида:
 k*sin(m*x) - n*cos(v*x)
 Найдите значение производной заданной функции в точке x0: y = 2sinx − 13cosx, x0 = π/2'''

prototype_42927 = "k*sin(m*x) - n*cos(v*x)"

'''Задача № 42928 c портала https://kuzovkin.info/one_exercise_1/42928 вида:
 (-k)*cos(m*x) - (n/pi)*(x**2)
 Найдите значение производной заданной функции в точке x0:
 y = −cosx + (1/π)*(x**2), x0 = π/6'''

prototype_42928 = "(-k)*cos(m*x) + (n/pi)*(x**2)"

'''Задача № 42929 c портала https://kuzovkin.info/one_exercise_1/42929 вида:
 (-k)*sin(m*x) - n
 Найдите значение производной заданной функции в точке x0: y = −sinx − 3, x0 = π/3'''

prototype_42929 = "(-k)*sin(m*x) - n"

'''Задача № 42930 c портала https://kuzovkin.info/one_exercise_1/42930 вида:
 k*cos(m*x) + sqrt(n)*x
 Найдите значение производной заданной функции в точке x0:
 y = 4cosx + xsqrt(2), x0 = π/4'''

prototype_42930 = "k*cos(m*x) + sqrt(n)*x"

'''Задача № 42931 c портала https://kuzovkin.info/one_exercise_1/42931 вида:
 k*(tan(x)) + x*(sqrt(pi))*(sqrt(x))
 Найдите значение производной заданной функции в точке x0:
 y = tgx + x*sqrt(π)*sqrt(x), x0 = π/4'''

# prototype_42931 = "k*(tan(x)) + x*(sqrt(pi))*(sqrt(x))"
# этот прототип не работает

'''Задача № 42932 c портала https://kuzovkin.info/one_exercise_1/42932 вида:
 k*(cot(m*x)) - n*(tan(v*x))
 Найдите значение производной заданной функции в точке x0: y = 2ctgx − 3tgx, x0 = π/3'''

prototype_42932 = "k*(cot(m*x)) - n*(tan(v*x))"

'''Задача № 42934 c портала https://kuzovkin.info/one_exercise_1/42934 вида:
 (k*x + m)**2 - n*(tan(v*x))
 Найдите значение производной заданной функции в точке x0:
 y = (2x + 3)^2 − 4tgx, x0 = 0'''

# prototype_42934 = "(k*x + m)**2 - n*(tan(v*x))"
# этот прототип не работает

'''Задача № 42935 c портала https://kuzovkin.info/one_exercise_1/42935 вида:
 sin(x)/x
 Найдите значение производной заданной функции в точке x0:
 y = sinx/x, x0 = π/2'''

# prototype_42935 = "sin(x)/x"
# этот прототип не работает

'''Задача № 42936 c портала https://kuzovkin.info/one_exercise_1/42936 вида:
 (k*x + m)/(n*x + v)
 Найдите значение производной заданной функции в точке x0:
 y = (x+1)/(x−1), x0 = 2'''

prototype_42936 = "(k*x + m)/(n*x + v)"

'''Задача № 42937 c портала https://kuzovkin.info/one_exercise_1/42937 вида:
cos(x)/x
 Найдите значение производной заданной функции в точке x0:
 y = cosx/x, x0 = π'''

# prototype_42937 = "cos(x)/x"
# этот прототип не работает

'''Задача № 42938 c портала https://kuzovkin.info/one_exercise_1/42938 вида:
 (k*x + m)/(n*x + v)
 Найдите значение производной заданной функции в точке x0:
 y = 2x/(x+1), x0 = 0'''

prototype_42938 = "(k*x + m)/(n*x + v)"

prototype_43087 = "sqrt(k*x + m)"

prototype_43088 = "sin(k*x - (pi/m))"

prototype_43089 = "cot((pi/m) - k*x)"

prototype_43090 = "cos((pi/m) - k*x)"

prototype_43091 = "tan(k*x - (pi/m))"

prototype_43092 = "(x**2 - k*x + m)**p"

prototype_43093 = "sqrt((k*x + m)/(n*x + v))"

prototype_43094 = "sqrt((k*x - m)*(n*x - v))"

prototype_43095 = "((x**2 + n)/(x**2 + v))**3"

prototype_43096 = "(tan(k*x))**3"

# prototype_43097 = "sin(sqrt(x))"
# этот прототип не работает

prototype_43098 = "cos(x**p)"

prototype_43099 = "(cot(x))**2 - m"

prototype_43100 = "(k*x + m)**p"

prototype_43101 = "sqrt(k*x - m)"

prototype_43102 = "n/(k*x - m)"

prototype_43103 = "sqrt(m - k*x)"

prototype_43104 = "sin(k*x - (pi/m))"

prototype_43105 = "tan(k*x)"

prototype_43106 = "cos((pi/m) - k*x)"

prototype_43107 = "cot(x/k)"

prototype_43108 = "sqrt(k*(x**p) - m*x + n)"

prototype_43109 = "sqrt((sin(x))**2 - k*sin(x) + m)"

prototype_43110 = "sqrt(n - m*x + k*(x**2))"

prototype_43111 = "sqrt(n - cos(x) + (1/k)*(cos(x))**2)"

prototype_43112 = "(k*x - m*sin(x))**2"

# prototype_43113 = "sqrt((m - sin(x))/cos(x))"
# этот прототип не работает

prototype_43114 = "sqrt((sin(x) + m)*cos(x))"

prototype_43115 = "(tan(x) - m)**p"

# prototype_43158 = "k*(acos(x))**3"
# этот прототип не работает

# prototype_43159 = "(n/sqrt(3))*(atan((k*x + m)/sqrt(3)))"
# этот прототип не работает

# prototype_43160 = "k*(asin(sqrt(x)))"
# этот прототип не работает

# prototype_43161 = "acos((m - x)/(x*sqrt(n)))"
# этот прототип не работает

# prototype_43162 = "atan(m - k*x)"
# этот прототип не работает

# prototype_43163 = "k*asin(sqrt(x))"
# этот прототип не работает

# prototype_43164 = "acos(k*x - m)"
# этот прототип не работает

# prototype_43165 = "k*(sqrt(acot(x)))"
# этот прототип не работает


def find_extremes(prototype):
    '''данная функция находит экстремумы функции
     со случайными коэффициентами
     (эта функция решает все задачи, кроме задач 13317 и 43501-43525)'''
    x = Symbol('x')
    equation = prototype
    while True:
        pattern = r"\b(?:(?!x)[a-z]+)\b"
        constants = re.findall(pattern, equation)
        constants_values = {}
        for constant in constants:
            constants_values[constant] = random.randint(1, 10)
        symbols_dict = {constant: symbols(constant) for constant in constants}
        substituted_eq = sympify(equation).subs(symbols_dict)
        for constant, value in constants_values.items():
            substituted_eq = substituted_eq.subs(symbols_dict[constant], value)
        prime = substituted_eq.diff(x)
        trig_functions = ['sin', 'asin', 'cos', 'acos', 'tan', 'atan', 'cot', 'acot']
        pattern_1 = "|".join(trig_functions)
        if random.randint(0, 2) == 0:
            text = r'Найти критическую точку функции: \( y= '
        elif random.randint(0, 2) == 1:
            text = r'Найти точку экстремума функции: \( y= '
        else:
            text = r'Найти экстремум функции: \( y= '
        if re.search(pattern_1, equation):
            prime_final = simplify(prime)
            eq_diff = Eq(prime_final, 0)
            critical_points = solve(eq_diff, x)
            condition = all(Mul(number, 10000).is_Integer and Mul(number, 10000).as_real_imag()[0] % 10 == 0 for
                            number in critical_points)
            if condition is True:
                break
        else:
            eq_diff = Eq(prime, 0)
            critical_points = solve(eq_diff, x)
            condition = all(Mul(number, 10000).is_Integer and Mul(number, 10000).as_real_imag()[0] % 10 == 0 for
                            number in critical_points)
            if condition is True:
                break
    if len(critical_points) > 1:
        note = r'значений больше 1, в ответе пишем все значения'
    elif len(critical_points) == 1:
        note = r'есть только одно значение'
    else:
        note = r'если решений нет, тогда в ответе пишем 0'
    task = text + str(latex(substituted_eq)) + '\)' + ', ' + note
    answer = [float(number) for number in critical_points]
    return {
      "condition": task,
      "answer": answer
    }

prototype_3034 = "k*x**2 + m*x + n"

# prototype_3036 = "(x**3 + m*x**2 + n)/(x**2)"
# этот прототип не работает

prototype_3042 = "k*x**2 - m*x + n"

prototype_3046 = "k*(x**p)*(sqrt(m + (n*x)))"

prototype_3047 = "k*x + (m/x) + n*x**2"

prototype_3064 = "(x**2)/k - ln(x**2 - m)"

prototype_3122 = "m*x - k*x**2"

prototype_3128 = "k*(x**p) + m*(x**q) + n"

prototype_6908 = "k*(x**p) + m*(x**q) + n"

# prototype_6910 = "k*x**2 + (m/x)"
# этот прототип не работает

prototype_6928 = "k*x**3 - m*x**2 + n*x + v"

prototype_6931 = "(-k)*x**3 + m*x**2 + n*x + v"

prototype_6933 = "k*x**3 - m*x"

prototype_6938 = "k*x**3 - m*x + n"

prototype_13213 = "k**(m*x + n) - p*(k**(s*x + t))"

prototype_13214 = "k*(x**p) - m*(x**q) + n"

prototype_13215 = "(k/x) - (m/(x**2))"

prototype_13218 = "k*x - sqrt(m + n*x)"

prototype_13219 = "k*x**2 + m*x"

prototype_13220 = "(k/x**p) - (m/(x**q))"

prototype_13224 = "k*x**2 + m*x**3 - n"

prototype_13228 = "k*x**3 - m*x**2"

prototype_13229 = "k*x**2 + m*x**3"

prototype_13232 = "k*x - m*x**3"

prototype_13234 = "(k*x**2 + m)/(n*x)"

prototype_13235 = "(x/k) + (m/x)"

prototype_13236 = "(-k)*x**3 + m*x + n"

prototype_13239 = "k*x + m"

# prototype_13287 = "m + sin(k*x)"
# этот прототип не работает

prototype_13288 = "(-k)*x**2 - m*x + n"

prototype_13289 = "x**4 - k*x**3 - k*x**2"

prototype_13293 = "k*(x**3) - m*(x**2) - n*x + v"

prototype_13298 = "(k/m)*x**3 - n*x**2 + v*x - p"

prototype_13303 = "k*x + exp((-m)*x)"

# prototype_13304 = "((x**4)/k) - m*x"
# этот прототип не работает

prototype_13305 = "k*x**4 - m*x**3 - n*x**2 + v*x - p"

prototype_13306 = "m*(x**p) + k*(x**q)"

prototype_13313 = "k*x**3 + m*x**2 - n*x + v"

prototype_13315 = "(k*x)/(n*x**2 + m)"

prototype_13316 = "((x**3)/k) + m*x**2 - n*x"

prototype_13318 = "((k*x - m)**3)*((n*x - v)**2)"


def determine_max_min_values(prototype):
    '''данная функция находит наибольшее и наименьшее
     значение функции без модуля и тригонометрии
     со случайными коэффициентами'''
    x = Symbol('x')
    equation = prototype
    while True:
        pattern = r"C\d+"
        constants = re.findall(pattern, equation)
        constants_values = {}
        for constant in constants:
            constants_values[constant] = random.randint(1, 10)
        symbols_dict = {constant: symbols(constant) for constant in constants}
        substituted_eq = sympify(equation).subs(symbols_dict)
        for constant, value in constants_values.items():
            substituted_eq = substituted_eq.subs(symbols_dict[constant], value)
        prime = substituted_eq.diff(x)
        eq_diff = Eq(prime, 0)
        critical_points = solve(eq_diff, x)
        condition = all(Mul(number, 10000).is_Integer and Mul(number, 10000).as_real_imag()[0] % 10 == 0 for
                        number in critical_points)
        if condition is True:
            break
    while True:
        values = []
        a = random.randint(-10, 10)
        b = random.randint(a + 1, 12)
        interval = Interval(a, b)
        for number in critical_points:
            if number >= a and number <= b:
                values.append(substituted_eq.subs(x, number))
        values.extend([substituted_eq.subs(x, a), substituted_eq.subs(x, b)])
        condition = all(Mul(point, 10000).is_Integer and Mul(point, 10000).as_real_imag()[0] % 10 == 0 for
                            point in values) and all(abs(point) < 10000 for point in values)
        if condition is True:
            break
    maximum = max(values)
    minimum = min(values)
    max_min = [minimum, maximum]
    if len(max_min) > 1:
        result = random.choice(values)
        if result == maximum:
            text = r'Найти наибольшее значение функции: \( y= '
        else:
            text = r'Найти наименьшее значение функции: \( y= '
    elif len(max_min) == 1:
        result = 0
        text = r'Наибольшее и наименьшее значение функции: \( y= '
    else:
        result = 0
        text = r'Найти наибольшее и наименьшее значение функции: \( y= '
    note_interval = r'на отрезке' + ' ' + '\(' + str(latex(interval)) + '\)'
    task = text + str(latex(substituted_eq)) + '\)' + ', ' + note_interval
    answer = float(result)
    return {
      "condition": task,
      "answer": answer
    }

def determine_max_min_values_mod(prototype):
    '''данная функция находит наибольшее и наименьшее
     значение функции с модулем со случайными коэффициентами'''
    x = Symbol('x')
    equation = prototype
    while True:
        pattern = r"C\d+"
        constants = re.findall(pattern, equation)
        constants_values = {}
        for constant in constants:
            constants_values[constant] = random.randint(1, 10)
        symbols_dict = {constant: symbols(constant) for constant in constants}
        substituted_eq = sympify(equation).subs(symbols_dict)
        for constant, value in constants_values.items():
            substituted_eq = substituted_eq.subs(symbols_dict[constant], value)
        a = random.randint(-10, 10)
        b = random.randint(a + 1, 12)
        interval = Interval(a, b)
        minimum = min([substituted_eq.subs(x, i) for i in range(a, b)])
        maximum = max([substituted_eq.subs(x, i) for i in range(a, b)])
        max_min = [minimum, maximum]
        result = random.choice(max_min)
        if result == maximum:
            text = r'Найти наибольшее значение функции: \( y= '
        else:
            text = r'Найти наименьшее значение функции: \( y= '
        note_interval = r'на отрезке' + ' ' + '\(' + str(latex(interval)) + '\)'
        condition = abs(result) < 10000 and Mul(result, 10000).is_Integer and Mul(result, 10000).as_real_imag()[0] % 10 == 0
        if condition is True:
            break
    task = text + str(latex(substituted_eq)) + '\)' + ', ' + note_interval
    answer = float(result)
    return {
      "condition": task,
      "answer": answer
    }

def determine_max_min_values_trig(prototype):
    '''данная функция находит наибольшее и наименьшее
     значение функции с тригонометрией со случайными коэффициентами'''
    x = Symbol('x')
    equation = prototype
    while True:
        pattern = r"C\d+"
        constants = re.findall(pattern, equation)
        constants_values = {}
        for constant in constants:
            constants_values[constant] = random.randint(1, 10)
        symbols_dict = {constant: symbols(constant) for constant in constants}
        substituted_eq = sympify(equation).subs(symbols_dict)
        for constant, value in constants_values.items():
            substituted_eq = substituted_eq.subs(symbols_dict[constant], value)
        prime = substituted_eq.diff(x)
        prime_final = simplify(prime)
        eq_diff = Eq(prime_final, 0)
        a = random.randint(-10, 10)
        b = random.randint(a + 1, 12)
        interval = Interval(a * pi, b * pi)
        critical_points = solve(eq_diff, x)
        selected_critical_points = [number for number in critical_points if number in interval]
        critical_points_pi = [number / pi for number in selected_critical_points]
        condition = all(Mul(point, 10000).is_Integer and Mul(point, 10000).as_real_imag()[0] % 10 == 0 for
                        point in critical_points_pi)
        if condition is True:
            break
    while True:
        values = []
        for point in critical_points_pi:
            if point >= a and point <= b:
                values.append(substituted_eq.subs(x, point * pi))
        values.extend([substituted_eq.subs(x, a * pi), substituted_eq.subs(x, b * pi)])
        condition = all(Mul(number, 10000).is_Integer and Mul(number, 10000).as_real_imag()[0] % 10 == 0 for
                            number in values) and all(abs(number) < 10000 for number in values)
        if condition is True:
            break
    maximum = max(values)
    minimum = min(values)
    max_min = [minimum, maximum]
    if len(max_min) > 1:
        result = random.choice(values)
        if result == maximum:
            text = r'Найти наибольшее значение функции: \( y= '
        else:
            text = r'Найти наименьшее значение функции: \( y= '
    elif len(max_min) == 1:
        result = 0
        text = r'Наибольшее и наименьшее значение функции: \( y= '
    else:
        result = 0
        text = r'Найти наибольшее и наименьшее значение функции: \( y= '
    note_interval = r'на отрезке' + ' ' + '\(' + str(latex(interval)) + '\)'
    task = text + str(latex(substituted_eq)) + '\)' + ', ' + note_interval
    answer = float(result)
    return {
      "condition": task,
      "answer": answer
    }

prototype_3093 = "(C1/C2)*(x**C3) - C4*x"
# обычная функция

prototype_3098 = "(root(x**C1, 3))*(C2*x - C3)"
# обычная функция

# prototype_6958 = "C1*x + C2/((C3*x - C4)**2)"
# обычная функция
# этот прототип не работает

prototype_6959 = "C1*(sqrt(C2*x)) - C3*x"
# обычная функция

prototype_6960 = "(1/C1)*(x**C2) - (C3/C4)*(x**C5) + C6"
# обычная функция

prototype_6961 = "(-C1)*(x**C2) - C3*(x*C5) + C6"
# обычная функция

prototype_6963 = "(C1*(x**C2))/C3 + C4/(C5*(x**C6))"
# обычная функция

prototype_6967 = "(-C1)*x**C2 + C3*x**C4 + C5"
# обычная функция

prototype_7276 = "(sqrt(C1 - C2*(x**2)))"
# обычная функция

prototype_7286 = "-C1*(x**C2) + C3*Abs(x) - C4"
# функция для модуля

prototype_7291 = "root((C1*(x**2))/(C3*x - C4), 3)"
# обычная функция

prototype_7296 = "C1*(sin(C2*x)) + C3*(cos(C4*x))"
# функция для тригонометрии

prototype_7301 = "-C1*(x**C2) + C3*Abs(C4*x - C5) + C6"
# функция для модуля

prototype_7302 = "-C1*(x**C2) + C3*Abs(C4*x + C5) - C6"
# функция для модуля

# prototype_7306 = "Abs(sqrt(C1*x - (x**C2) - C3) - C4) + sqrt(C1*x - (x**C2) - C3) + x**C4 - C5*(x**C6)"
# функция для модуля
# этот прототип не работает

# prototype_7307 = "Abs(C1 - sqrt(C2 - C3*(x**C4))) + x**C5 - C6*(x**C7) + sqrt(C2 - C3*(x**C4))"
# функция для модуля
# этот прототип не работает

prototype_7310 = "((C1*x - C2)**C3)*(C4 - C5*x)"
# обычная функция

prototype_13255 = "C1/(C2*x - C3) + (C4*x)/C5"
# обычная функция

prototype_13256 = "C1*(x**C2) - C3*(x**C4) - C5"
# обычная функция

prototype_13257 = "-C1*(x**C2) - C3*(x**C4) + C5"
# обычная функция

prototype_13262 = "C3*(x**C2)*(C4*x - C5)"
# обычная функция

prototype_13264 = "-C1*(x**C2) - C3*(x**C4) + C5*x - C6"
# обычная функция

# prototype_13265 = "(C1*x)/(C2*x - C3*(x**C4) - C5)"
# обычная функция
# этот прототип не работает

prototype_13268 = "C1*(x**C2) - C3*(x**C4)"
# обычная функция

prototype_13269 = "(C1*(x**C2))/(C3*(C4*x + C5))"
# обычная функция

prototype_13580 = "C1*(x**C2) - C3*x + C4 - C5*(root((C6*x - C7)**4, 3)) + C8*(root((C6*x - C7)**2, 3))"
# обычная функция

# prototype_13581 = "C1*x*(ln(C2)) - C3*x*(ln(x))"
# обычная функция - этот прототип не работает
# функция для модуля - этот прототип не работает

# prototype_13582 = "(C1/(ln(C2)))*(C2**x + C2**(-x))"
# обычная функция - этот прототип не работает
# функция для модуля - этот прототип не работает

prototype_13584 = "C1*(sin(C2*x)) + C3*(cos(C4*x))"
# функция для тригонометрии

prototype_13588 = "C1*(x**C2) - C3*x*Abs(C4*x - C5)"
# функция для модуля

prototype_13589 = "-C1*(x**C2) + C3*Abs(C4*x - C5) + C6"
# функция для модуля

prototype_13590 = "C1*sqrt(C2 - C3*(x**C4))"
# обычная функция

prototype_13591 = "C1*sqrt(C2*(x**C3) - C4*x - C5)"
# обычная функция

prototype_13593 = "C1*(x**C2) - C3*x + C4 - C5*(root((C6*x - C7)**4, 3)) + C8*(root((C6*x - C7)**2, 3))"
# обычная функция

# prototype_13594 = "C1*x*(ln(C2)) - C3*x*(ln(x))"
# обычная функция - этот прототип не работает
# функция для модуля - этот прототип не работает

prototype_13596 = "C1*(C2**(C3*x)) - C4*(C1**(C1*x)) + C1*(C2**(C5*x))"
# обычная функция - этот прототип не работает
# функция для модуля

prototype_13598 = "C1*(cos(C2*x)) - C3*(cos(C4*x)) + C5"
# функция для тригонометрии

# prototype_13599 = "C1/(C2 + (sqrt(C1))*(sin(C3*x + (pi/C4))))"
# функция для тригонометрии
# этот прототип не работает

prototype_13604 = "-C1*(x**C2) + C3*Abs(C4*x + C5) - C6"
# функция для модуля

# prototype_13605 = "Abs(sqrt(C1 - C2*(x**C3)) - C4) + sqrt(C1 - C2*(x**C3)) + x**C5 + C6*x**C7"
# функция для модуля
# этот прототип не работает

# prototype_13606 = "C1*(x**C2) - C3*(x**C4) + Abs(C5 - sqrt(C6*x + C7 - C8*(x**C9))) + sqrt(C6*x + C7 - C8*(x**C9))"
# функция для модуля
# этот прототип не работает

prototype_13609 = "(C1*(x**C2) + C3*x - C4)**C5"
# обычная функция

prototype_13610 = "((C1*x + C2)**C3)*(C4 - C5*x)"
# обычная функция
