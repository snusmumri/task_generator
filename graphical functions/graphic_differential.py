import random
import numpy as np
import math
import fractions
from sympy import *
import matplotlib.pyplot as plt
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
    return task, answer_float

def take_derivatives_in_point_1(prototype):
    '''данная функция находит значение производной функции
     со случайными коэффициентами в точке x_0'''
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
    return task, answer_float

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
    return task, answer

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


def determine_nature_extremum_trig(prototype):
    '''данная функция находит экстремумы тригонометрической функции
     со случайными коэффициентами и определяет их характер
     (эта функция решает задачи 43501-43525)'''
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
        if random.randint(0, 2) == 0:
            text = r'Найти критическую точку функции: \( y= '
        elif random.randint(0, 2) == 1:
            text = r'Найти точку экстремума функции: \( y= '
        else:
            text = r'Найти экстремум функции: \( y= '
        prime_final = simplify(prime)
        eq_diff = Eq(prime_final, 0)
        if random.randint(0, 1) == 0:
            a = random.randint(-10, 10)
            b = random.randint(a + 1, 12)
            interval = Interval(a * pi, b * pi)
            critical_points = solve(eq_diff, x)
            selected_critical_points = [number for number in critical_points if number in interval]
        else:
            interval = Interval(S.NegativeInfinity, S.Infinity)
            selected_critical_points = solve(eq_diff, x)
        critical_points_pi = [number/pi for number in selected_critical_points]
        double_prime = prime.diff(x)
        double_prime_final = simplify(double_prime)
        results = []
        for point in critical_points_pi:
            value = double_prime_final.subs(x, point * pi)
            latex_point_pi = latex(point*pi)
            if im(value) == 0:
                if value > 0:
                    results.append(f"\( {latex_point_pi} \)")
                elif value < 0:
                    results.append(f"\( {latex_point_pi} \)")
                else:
                    results.append(f"\( {latex_point_pi} \)")
            else:
                results.append(f"\( {latex_point_pi} \)")
        note_interval = '\(' + r"x \in " + str(latex(interval)) + '\)' + ', '
        condition = all(Mul(point, 10000).is_Integer and Mul(point, 10000).as_real_imag()[0] % 10 == 0 for
                            point in critical_points_pi)
        if condition is True:
            break
    if len(selected_critical_points) > 1:
        note_solution = r'значений больше 1, в ответе пишем все значения'
    elif len(selected_critical_points) == 1:
        note_solution = r'есть только одно значение'
    else:
        note_solution = r'если решений нет, тогда в ответе пишем 0'
    task = text + str(latex(substituted_eq)) + '\)' + ', ' + note_interval + note_solution
    answer = ', '.join(results)
    return task, answer

def determine_nature_extremum(prototype):
    '''данная функция находит экстремумы функции
     со случайными коэффициентами и определяет их характер
     (эта функция решает задачи 43501-43525)'''
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
        if random.randint(0, 2) == 0:
            text = r'Найти критическую точку функции: \( y= '
        elif random.randint(0, 2) == 1:
            text = r'Найти точку экстремума функции: \( y= '
        else:
            text = r'Найти экстремум функции: \( y= '
        eq_diff = Eq(prime, 0)
        selected_critical_points = solve(eq_diff, x)
        note_interval = ''
        condition = all(Mul(number, 10000).is_Integer and Mul(number, 10000).as_real_imag()[0] % 10 == 0 for
                            number in selected_critical_points)
        if condition is True:
            break
    double_prime = prime.diff(x)
    float_critical_points = [float(number) for number in selected_critical_points]
    results = []
    for point in float_critical_points:
        value = double_prime.subs(x, point)
        if im(value) == 0:
            if value > 0:
                results.append(f"{point}")
            elif value < 0:
                results.append(f"{point}")
            else:
                results.append(f"{point}")
        else:
            results.append(f"{point}")
    if len(selected_critical_points) > 1:
        note_solution = r'значений больше 1, в ответе пишем все значения'
    elif len(selected_critical_points) == 1:
        note_solution = r'есть только одно значение'
    else:
        note_solution = r'если решений нет, тогда в ответе пишем 0'
    task = text + str(latex(substituted_eq)) + '\)' + ', ' + note_interval + note_solution
    answer = ', '.join(results)
    return task, answer

prototype_43501 = "k*(x**p) - m*(x**q) + n"

prototype_43502 = "n - m*(x**q) - k*(x**p)"

prototype_43502 = "k*(x**p) - m*(x**q) - n"

prototype_43503 = "k*(x**p) - m*(x**q) - n"

prototype_43504 = "(-k)*(x**p) - m*(x**q) + n"

prototype_43505 = "(x**p)/k - (m/n)*(x**2) + v*x - t"

prototype_43506 = "k*(x**p) - m*(x**q) + n"

prototype_43507 = "k*(x**p) - m*(x**q) - n*(x**t) + n"

prototype_43508 = "k*(x**p) - m*(x**q) + n"

prototype_43509 = "k*(x**p) - m*(x**q)"

prototype_43510 = "k*(x**p) - m*(x**3) - n*(x**2) + v"

prototype_43511 = "k*(x**p) - m*(x**q)"

prototype_43512 = "k*(x**p) + m*(x**4) - n*(x**3) + v"

prototype_43513 = "k*(x**p) + (m/(x**p))"

prototype_43514 = "(k*(x**p) + m)/(x**q)"

prototype_43515 = "k*x - m*(sqrt(n*x - v))"

prototype_43516 = "sqrt(k*x + m) + sqrt(n - v*x)"

prototype_43517 = "k*(sqrt(m*x - n)) - v*x"

prototype_43518 = "(sqrt(k*x)) + m*(sqrt(n - v*x))"

prototype_43519 = "v*x - k*cos(m*x)"

prototype_43520 = "k*sin(m*x) - v*x"

prototype_43521 = "(k*(x**p) - m*(x**q))**t"

prototype_43522 = "sqrt(k*(x**p) - m*(x**q))"

prototype_43523 = "(k*(x**p) - m*(x**q))**t"

prototype_43524 = "sqrt(k*(x**p) - m*(x**q))"

prototype_43525 = "k*asin(x**p)"


def determine_nature_extremum_1(prototype):
    '''данная функция находит экстремумы функции
     со случайными коэффициентами и определяет их характер
     (эта функция решает задачи 43501-43525)'''
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
        if random.randint(0, 2) == 0:
            text = r'Найти критическую точку функции: \( y= '
        elif random.randint(0, 2) == 1:
            text = r'Найти точку экстремума функции: \( y= '
        else:
            text = r'Найти экстремум функции: \( y= '
        eq_diff = Eq(prime, 0)
        selected_critical_points = solve(eq_diff, x)
        note_interval = ''
        condition = all(Mul(number, 10000).is_Integer and Mul(number, 10000).as_real_imag()[0] % 10 == 0 for
                            number in selected_critical_points)
        if condition is True:
            break
    double_prime = prime.diff(x)
    float_critical_points = [float(number) for number in selected_critical_points]
    results = []
    for point in float_critical_points:
        value = double_prime.subs(x, point)
        if im(value) == 0:
            if value > 0:
                results.append(f"{point}")
            elif value < 0:
                results.append(f"{point}")
            else:
                results.append(f"{point}")
        else:
            results.append(f"{point}")
    if len(selected_critical_points) > 1:
        note_solution = r'значений больше 1, в ответе пишем все значения'
    elif len(selected_critical_points) == 1:
        note_solution = r'есть только одно значение'
    else:
        note_solution = r'если решений нет, тогда в ответе пишем 0'
    task = text + str(latex(substituted_eq)) + '\)' + ', ' + note_interval + note_solution
    answer = ', '.join(results)
    return task, answer

def determine_nature_extremum_trig_1(prototype):
    '''данная функция находит экстремумы тригонометрической функции
     со случайными коэффициентами и определяет их характер
     (эта функция решает задачи 43501-43525)'''
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
        if random.randint(0, 2) == 0:
            text = r'Найти критическую точку функции: \( y= '
        elif random.randint(0, 2) == 1:
            text = r'Найти точку экстремума функции: \( y= '
        else:
            text = r'Найти экстремум функции: \( y= '
        prime_final = simplify(prime)
        eq_diff = Eq(prime_final, 0)
        if random.randint(0, 1) == 0:
            a = random.randint(-10, 10)
            b = random.randint(a + 1, 12)
            interval = Interval(a * pi, b * pi)
            critical_points = solve(eq_diff, x)
            selected_critical_points = [number for number in critical_points if number in interval]
        else:
            interval = Interval(S.NegativeInfinity, S.Infinity)
            selected_critical_points = solve(eq_diff, x)
        critical_points_pi = [number/pi for number in selected_critical_points]
        double_prime = prime.diff(x)
        double_prime_final = simplify(double_prime)
        results = []
        for point in critical_points_pi:
            value = double_prime_final.subs(x, point * pi)
            latex_point_pi = latex(point*pi)
            if im(value) == 0:
                if value > 0:
                    results.append(f"\( {latex_point_pi} \)")
                elif value < 0:
                    results.append(f"\( {latex_point_pi} \)")
                else:
                    results.append(f"\( {latex_point_pi} \)")
            else:
                results.append(f"\( {latex_point_pi} \)")
        note_interval = '\(' + r"x \in " + str(latex(interval)) + '\)' + ', '
        condition = all(Mul(point, 10000).is_Integer and Mul(point, 10000).as_real_imag()[0] % 10 == 0 for
                            point in critical_points_pi)
        if condition is True:
            break
    if len(selected_critical_points) > 1:
        note_solution = r'значений больше 1, в ответе пишем все значения'
    elif len(selected_critical_points) == 1:
        note_solution = r'есть только одно значение'
    else:
        note_solution = r'если решений нет, тогда в ответе пишем 0'
    task = text + str(latex(substituted_eq)) + '\)' + ', ' + note_interval + note_solution
    answer = ', '.join(results)
    return task, answer

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
    return task, answer

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
    return task, answer

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
    return task, answer




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


'''Новые шаблоны:'''

prototype_49379 = "C1*(x**C2) - C3*x*Abs(C4*x - C5)"
# determine_max_min_values_mod(prototype)

prototype_49349 = "(-C1)*x - (C2/x)"
# determine_max_min_values(prototype)

prototype_49350 = "C1*(sin(C2*x)) - C3*(cos(C4*x))"
# determine_max_min_values_trig(prototype)

# prototype_49351 = "(sqrt(C1))*x - C2*(cos(C3*x))"
# determine_max_min_values_trig(prototype) - этот прототип не работает

prototype_49352 = "(sqrt(C1))*(sin(C2*x)) + C3*(cos(C2*x))"
# determine_max_min_values_trig(prototype)

prototype_49353 = "C1*(cos(C2*x + (pi/C3)))"
# determine_max_min_values_trig(prototype)

prototype_49356 = "C1*(sin(C2*x)) + C3*(cos(C4*x))"
# determine_max_min_values_trig(prototype)

prototype_49357 = "(sqrt(C1))*(sin(C2*x)) + C3*(cos(C2*x)) - C4"
# determine_max_min_values_trig(prototype)

prototype_49358 = "C1*(cos(C2*x)) - C3*(sin(C4*x))"
# determine_max_min_values_trig(prototype)

# prototype_49359 = "C1*(sqrt(C2))*(cos(C3*x)) + C1*(sin(C3*x))"
# determine_max_min_values_trig(prototype) - этот прототип не работает

prototype_49378 = "(-C1)*(x**C2) + C3*x*Abs(C4*x - C5)"
# determine_max_min_values_mod(prototype)

prototype_49347 = "(C1*x)/(C2*(x**2) + C3)"
# determine_max_min_values(prototype)

prototype_49348 = "((C1*x - C2)**C3)*((C4*x + C5)**C6)"
# determine_max_min_values(prototype)

prototype_49346 = "C1*sqrt(C2 + C3*x - C4*(x**C5))"
# determine_max_min_values(prototype)

prototype_49345 = "(C1/x) + (x/C2)"
# determine_max_min_values(prototype)

prototype_49344 = "((C1*x + C2)**C3)*((C4*x - C5)**C6)"
# determine_max_min_values(prototype)

prototype_49343 = "C1*sqrt(C2*(x**C3) + C4*x + C5)"
# determine_max_min_values(prototype)

prototype_49334 = "C1*(x**C2) - C3*(x**C4)"
# determine_max_min_values(prototype)

prototype_49335 = "C1*(x**C2) - C3*(x**C4) + C5"
# determine_max_min_values(prototype)

prototype_49336 = "C1*(x**C2) + C3*(x**C4) - C5*x - C6"
# determine_max_min_values(prototype)

prototype_49337 = "(C1*(x**C2) + C3)/(C4*(x**C5) - C6)"
# determine_max_min_values(prototype) - этот прототип не работает
# determine_max_min_values_mod(prototype)

prototype_49338 = "(1/C1)*(x**C2) - C3*x"
# determine_max_min_values(prototype)

prototype_49075 = "(C1 - C2*x)/(C3*x + C4)"
# take_derivatives_in_point_1(prototype)

prototype_49076 = "(C1 + C2*x)*sqrt(C3*x)"
# take_derivatives_in_point_1(prototype)

prototype_49077 = "C1*(root(C2*x, C3)) - C4*(root(C5*x, C6))"
# take_derivatives_in_point_1(prototype)

prototype_49078 = "(C1*x)*(C2*(sin(C3*x)))"
# take_derivatives_in_point_1(prototype)

prototype_49079 = "C1*sqrt(C2*x) - C3*x"
# take_derivatives_in_point_1(prototype)

# prototype_49080 = "(C1*(cos(C2*x)))/(C3 - C4*x)"
# take_derivatives_in_point_1(prototype) - этот прототип не работает

prototype_49081 = "C1*(x**(-C2)) - C3*(x**(-C4))"
# take_derivatives_in_point_1(prototype)

prototype_49082 = "(C1*(x**C2) - C3*x - C4)/(C5*x + C6)"
# take_derivatives_in_point_1(prototype)

prototype_49271 = "C1*x - C2*(x**C3)"
# determine_nature_extremum_1(prototype)

prototype_49272 = "C1*(x**C2) - C3*(x**C4) + C5"
# determine_nature_extremum_1(prototype)

prototype_49273 = "C1*(x**C2) - C3*(x**C4) - C5*x + C6"
# determine_nature_extremum_1(prototype)

prototype_49274 = "C1*(x**C2) - (C3*(x**C4))/C5"
# determine_nature_extremum_1(prototype)

prototype_49275 = "C1*x - (1/C2)*(x**C3)"
# determine_nature_extremum_1(prototype)

prototype_49276 = "(x**C1)/C2 + C3*(x**C4) - C5*x + C6"
# determine_nature_extremum_1(prototype)

prototype_49277 = "C1*(x**C2) - C3*(x**C4) + C5"
# determine_nature_extremum_1(prototype)

prototype_49278 = "C1 + C2*(x**2) + C3*(x**3) - C4*(x**C5)"
# determine_nature_extremum_1(prototype)


prototype_49272 = "C1*(x**C2) - C3*(x**C4) + C5"

prototype = prototype_49272

def plot_graph_and_draw_tangent_to_graph_at_point_1(prototype):
    '''данная функция строит график и проводит
     касательную к графику в точке x_0'''
    x = Symbol('x')
    equation = prototype
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
    a = np.random.randint(-100, 100)
    y_0 = substituted_eq.subs(x, a)
    prime_value = prime.subs(x, a)
    tangent = prime_value * (x - a) + y_0
    substituted_eq_lambdified = lambdify(x, substituted_eq, modules=['numpy'])
    tangent_lambdified = lambdify(x, tangent, modules=['numpy'])
    x_values = np.linspace(a - 100, a + 100, 400)
    y_values = substituted_eq_lambdified(x_values)
    tangent_values = tangent_lambdified(x_values)
    plt.plot(x_values, y_values, label='f(x)')
    plt.plot(x_values, tangent_values, label='Tangent')
    plt.axhline(color='black')
    plt.axvline(color='black')
    plt.xlabel('x')
    plt.ylabel('y')
    plt.title('Graph of f(x) and its tangent')
    plt.legend()
    plt.show()
    text = r'Найдите значение производной заданной функции: \( y= '
    task = text + str(latex(substituted_eq)) + r"\) в точке \(x_0 = " + str(
                a) + "\)"
    answer = float(prime_value)
    return task, answer

def plot_graph_and_draw_tangent_to_graph_at_point_2(prototype):
    '''данная функция строит график и проводит
     касательную к графику в точке x_0'''
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
        a = np.random.randint(-100, 100)
        y_0 = substituted_eq.subs(x, a)
        prime_value = prime.subs(x, a)
        if ask(Q.integer(prime_value * 10000)) is True and abs(prime_value) < 10000:
            break
    tangent = prime_value * (x - a) + y_0
    substituted_eq_lambdified = lambdify(x, substituted_eq, modules=['numpy'])
    tangent_lambdified = lambdify(x, tangent, modules=['numpy'])
    x_values = np.linspace(a - 100, a + 100, 400)
    y_values = substituted_eq_lambdified(x_values)
    tangent_values = tangent_lambdified(x_values)
    plt.plot(x_values, y_values, label='f(x)')
    plt.plot(x_values, tangent_values, label='Tangent')
    plt.axhline(color='black')
    plt.axvline(color='black')
    plt.xlabel('x')
    plt.ylabel('y')
    plt.title('Graph of f(x) and its tangent')
    plt.legend()
    plt.show()
    text = r'Найдите значение производной заданной функции: \( y= '
    task = text + str(latex(substituted_eq)) + r"\) в точке \(x_0 = " + str(
                a) + "\)"
    answer = float(prime_value)
    return task, answer

def plot_graph_and_draw_tangent_to_graph_at_point_3(prototype):
    '''данная функция строит график и проводит
     касательную к графику в точке x_0'''
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
        a = np.random.randint(-100, 100)
        y_0 = substituted_eq.subs(x, a)
        prime_value = prime.subs(x, a)
        if ask(Q.integer(prime_value * 10000)) is True and abs(prime_value) < 10000 and prime_value != 0:
            break
    tangent = prime_value * (x - a) + y_0
    substituted_eq_lambdified = lambdify(x, substituted_eq, modules=['numpy'])
    tangent_lambdified = lambdify(x, tangent, modules=['numpy'])
    x_values = np.linspace(a - 100, a + 100, 400)
    y_values = substituted_eq_lambdified(x_values)
    tangent_values = tangent_lambdified(x_values)
    plt.plot(x_values, y_values, label='f(x)')
    plt.plot(x_values, tangent_values, label='Tangent')
    plt.axhline(color='black')
    plt.axvline(color='black')
    plt.xlabel('x')
    plt.ylabel('y')
    plt.title('Graph of f(x) and its tangent')
    plt.legend()
    plt.show()
    text = r'Найдите значение производной заданной функции: \( y= '
    task = text + str(latex(substituted_eq)) + r"\) в точке \(x_0 = " + str(
                a) + "\)"
    answer = float(prime_value)
    return task, answer

def plot_graph_and_draw_tangent_to_graph_at_point_4(prototype):
    '''данная функция строит график и проводит
     касательную к графику в точке x_0'''
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
        a = np.random.randint(-1000, 1000)
        y_0 = substituted_eq.subs(x, a)
        prime_value = prime.subs(x, a)
        # tangent_slope = atan(prime_value)
        # condition = (deg(tangent_slope) > 20) & (deg(tangent_slope) < 160)
        if ask(Q.integer(prime_value * 10000)) is True and tan(pi/6) < abs(prime_value) < 10000 and prime_value != 0:
            break
    tangent = prime_value * (x - a) + y_0
    substituted_eq_lambdified = lambdify(x, substituted_eq, modules=['numpy'])
    tangent_lambdified = lambdify(x, tangent, modules=['numpy'])
    x_values = np.linspace(a - 600, a + 600, 400)
    y_values = substituted_eq_lambdified(x_values)
    tangent_values = tangent_lambdified(x_values)
    fig = plt.figure()
    ax = plt.axes()
    fig.add_axes(ax)
    ax.spines[["left", "bottom"]].set_position('zero')
    ax.spines[["top", "right"]].set_visible(False)
    ax.plot(1, 0, ">k", transform=ax.get_yaxis_transform(), clip_on=False)
    ax.plot(0, 1, "^k", transform=ax.get_xaxis_transform(), clip_on=False)
    arrow_length = 10
    ax.annotate('x', xy=(1, 0), xycoords=('axes fraction', 'data'),
                xytext=(0, arrow_length), textcoords='offset points',
                ha='center', va='bottom')
    ax.annotate('y', xy=(0, 1), xycoords=('data', 'axes fraction'),
                xytext=(arrow_length, 0), textcoords='offset points',
                ha='center', va='bottom')
    plt.plot(x_values, y_values, label='')
    plt.plot(x_values, tangent_values, label='')
    plt.axhline(color='black')
    plt.axvline(color='black')
    plt.grid(True, linewidth=0.5, linestyle='dotted')
    plt.scatter(a, y_0, color='red', label="")
    plt.plot([a, a], [y_0, 0], ':', color='red')
    # plt.annotate(' ^ ', (0, max(y_values)), xytext=(-0.5, max(y_values)), ha='center', arrowprops=dict(
    #     facecolor='black', arrowstyle='->'))
    # plt.annotate(' < ', (max(x_values), 0), xytext=(max(x_values), -0.5), ha='center', arrowprops=dict(
    #     facecolor='black', arrowstyle='->'))
    # b = x_values[np.where(y_values <= tangent_values)[0][-1]]
    # y_1 = substituted_eq.subs(x, b)
    # plt.scatter(b, y_1, color='green', label="Point before x_0")
    grid_x = np.arange(a - 600, a + 600, 1)
    # grid_y = substituted_eq.subs(x, grid_x)
    closest_points_x = [grid_x[np.argmin(np.abs(grid_x - a)) - 300], grid_x[np.argmin(np.abs(grid_x - a)) + 300]]
    closest_points_y = [tangent.subs(x, closest_points_x[0]), tangent.subs(x, closest_points_x[1])]
    # plt.plot(closest_points_x, closest_points_y, color='green', label="Point")
    plt.scatter(closest_points_x, closest_points_y, color='green', label="")
    # plt.xlabel('x')
    # plt.ylabel('y')
    plt.title('')
    # plt.legend()
    plt.show()
    text = r'Найдите значение производной заданной функции: \( y= '
    task = text + str(latex(substituted_eq)) + r"\) в точке \(x_0 = " + str(
                a) + "\)"
    answer = float(prime_value)
    return task, answer

def plot_graph_and_draw_tangent_to_graph_at_point_5(prototype):
    '''данная функция строит график и проводит
     касательную к графику в точке x_0'''
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
        a = np.random.randint(-1000, 1000)
        y_0 = substituted_eq.subs(x, a)
        prime_value = prime.subs(x, a)
        if ask(Q.integer(prime_value * 10000)) is True and tan(pi/6) < abs(prime_value) < 10000 and prime_value != 0:
            break
    tangent = prime_value * (x - a) + y_0
    substituted_eq_lambdified = lambdify(x, substituted_eq, modules=['numpy'])
    tangent_lambdified = lambdify(x, tangent, modules=['numpy'])
    x_values = np.linspace(a - 600, a + 600, 400)
    y_values = substituted_eq_lambdified(x_values)
    tangent_values = tangent_lambdified(x_values)
    fig = plt.figure()
    ax = plt.axes()
    fig.add_axes(ax)
    ax.spines[["left", "bottom"]].set_position('zero')
    ax.spines[["top", "right"]].set_visible(False)
    ax.plot(1, 0, ">k", transform=ax.get_yaxis_transform(), clip_on=False)
    ax.plot(0, 1, "^k", transform=ax.get_xaxis_transform(), clip_on=False)
    arrow_length = 10
    ax.annotate('x', xy=(1, 0), xycoords=('axes fraction', 'data'),
                xytext=(0, arrow_length), textcoords='offset points',
                ha='center', va='bottom')
    ax.annotate('y', xy=(0, 1), xycoords=('data', 'axes fraction'),
                xytext=(arrow_length, 0), textcoords='offset points',
                ha='center', va='bottom')
    plt.plot(x_values, y_values, label='')
    plt.plot(x_values, tangent_values, label='')
    plt.axhline(color='black')
    plt.axvline(color='black')
    plt.grid(True, linewidth=0.5, linestyle='dotted')
    plt.scatter(a, y_0, color='red', label="")
    plt.plot([a, a], [y_0, 0], ':', color='red')
    grid_x = np.arange(a - 600, a + 600, 1)
    closest_points_x = [grid_x[np.argmin(np.abs(grid_x - a)) - 300], grid_x[np.argmin(np.abs(grid_x - a)) + 300]]
    closest_points_y = [tangent.subs(x, closest_points_x[0]), tangent.subs(x, closest_points_x[1])]
    plt.scatter(closest_points_x, closest_points_y, color='green', label="")
    plt.title('')
    plt.show()
    text = r'Найдите значение производной заданной функции: \( y= '
    task = text + str(latex(substituted_eq)) + r"\) в точке \(x_0 = " + str(
                a) + "\)"
    answer = float(prime_value)
    return task, answer

def plot_graph_and_draw_tangent_to_graph_at_point_6(prototype):
    '''данная функция строит график и проводит
     касательную к графику в точке x_0'''
    x, y = symbols('x y')
    while True:
        point1 = (np.random.randint(-100, 100), np.random.randint(-100, 100))
        point2 = (np.random.randint(-100, 100), np.random.randint(-100, 100))
        line_eq = Eq((y - point1[1]) / (y - point2[1]), (x - point1[0]) / (x - point2[0]))
        prime_line = simplify(diff(line_eq, x))
        # if ask(Q.integer(prime_line * 10000)) is True and abs(prime_line) < 10000 and prime_line != 0:
        #     break
    # while True:
        equation = prototype
        pattern = r"C\d+"
        constants = re.findall(pattern, equation)
        constants_values = {}
        for constant in constants:
            constants_values[constant] = random.randint(1, 10)
        symbols_dict = {constant: symbols(constant) for constant in constants}
        substituted_eq = sympify(equation).subs(symbols_dict)
        for constant, value in constants_values.items():
            substituted_eq = substituted_eq.subs(symbols_dict[constant], value)
        prime_curve = substituted_eq.diff(x)
        a = np.random.randint(-1000, 1000)
        y_0 = substituted_eq.subs(x, a)
        prime_line_value = prime_line.subs(x, a)
        prime_curve_value = prime_curve.subs(x, a)
        if ask(Q.integer(prime_line_value * 10000)) is True and abs(prime_line_value) < 10000 and prime_line_value != 0 and prime_line_value == prime_curve_value:
            break
        # if prime_curve_value == prime_line_value:
        #     break
    tangent = prime_curve_value * (x - a) + y_0
    substituted_eq_lambdified = lambdify(x, substituted_eq, modules=['numpy'])
    tangent_lambdified = lambdify(x, tangent, modules=['numpy'])
    x_values = np.linspace(a - 600, a + 600, 400)
    y_values = substituted_eq_lambdified(x_values)
    tangent_values = tangent_lambdified(x_values)
    fig = plt.figure()
    ax = plt.axes()
    fig.add_axes(ax)
    ax.spines[["left", "bottom"]].set_position('zero')
    ax.spines[["top", "right"]].set_visible(False)
    ax.plot(1, 0, ">k", transform=ax.get_yaxis_transform(), clip_on=False)
    ax.plot(0, 1, "^k", transform=ax.get_xaxis_transform(), clip_on=False)
    arrow_length = 10
    ax.annotate('x', xy=(1, 0), xycoords=('axes fraction', 'data'),
                xytext=(0, arrow_length), textcoords='offset points',
                ha='center', va='bottom')
    ax.annotate('y', xy=(0, 1), xycoords=('data', 'axes fraction'),
                xytext=(arrow_length, 0), textcoords='offset points',
                ha='center', va='bottom')
    plt.plot(x_values, y_values, label='Функция')
    plt.plot(x_values, tangent_values, label='')
    plt.axhline(color='black')
    plt.axvline(color='black')
    plt.grid(True, linewidth=0.5, linestyle='dotted')
    plt.scatter(a, y_0, color='red', label="")
    plt.plot([a, a], [y_0, 0], ':', color='red')
    plt.scatter(*point1, color='red', label='Точка 1')
    plt.scatter(*point2, color='blue', label='Точка 2')
    plt.title('')
    plt.show()
    text = r'Найдите значение производной заданной функции: \( y= '
    task = text + str(latex(substituted_eq)) + r"\) в точке \(x_0 = " + str(
                a) + "\)"
    answer = float(prime_line)
    return task, answer




def plot_graph_and_draw_tangent_to_graph_at_point_7():
    '''данная функция строит график и проводит
     касательную к графику в точке x_0'''
    x, y = symbols('x y')
    point1 = (np.random.randint(-100, 100), np.random.randint(-100, 100))
    point2 = (np.random.randint(-100, 100), np.random.randint(-100, 100))
    line_eq = Eq((y - point1[1]) / (y - point2[1]), (x - point1[0]) / (x - point2[0]))
    prime_line = diff(line_eq.rhs, x)
    a = np.random.randint(-100, 100)
    y_0 = line_eq.subs(x, a)
    prime_line_value = prime_line.subs(x, a)
    fig = plt.figure()
    ax = plt.axes()
    fig.add_axes(ax)
    ax.spines[["left", "bottom"]].set_position('zero')
    ax.spines[["top", "right"]].set_visible(False)
    ax.plot(1, 0, ">k", transform=ax.get_yaxis_transform(), clip_on=False)
    ax.plot(0, 1, "^k", transform=ax.get_xaxis_transform(), clip_on=False)
    arrow_length = 10
    ax.annotate('x', xy=(1, 0), xycoords=('axes fraction', 'data'),
                xytext=(0, arrow_length), textcoords='offset points',
                ha='center', va='bottom')
    ax.annotate('y', xy=(0, 1), xycoords=('data', 'axes fraction'),
                xytext=(arrow_length, 0), textcoords='offset points',
                ha='center', va='bottom')
    plt.axhline(color='black')
    plt.axvline(color='black')
    plt.grid(True, linewidth=0.5, linestyle='dotted')
    plt.scatter(a, y_0, color='red', label="")
    plt.plot([a, a], [y_0, 0], ':', color='red')
    plt.scatter(*point1, color='red', label='Точка 1')
    plt.scatter(*point2, color='blue', label='Точка 2')
    plt.title('')
    plt.show()
    answer = float(prime_line_value)
    return answer

def plot_graph_and_draw_tangent_to_graph_at_point_8():
    '''данная функция строит график и проводит
     касательную к графику в точке x_0'''
    x_vals = range(-10, 11)
    y_vals = range(-10, 11)
    point1 = (2, 3)
    point2 = (5, -4)
    fig, ax = plt.subplots()
    ax.grid(True)
    ax.plot(point1[0], point1[1], 'ro', label='Point 1')
    ax.plot(point2[0], point2[1], 'bo', label='Point 2')
    x, y = symbols('x y')
    eq = solve((point2[1] - point1[1])*(x - point1[0]) - (point2[0] - point1[0])*(y - point1[1]), y)
    eq_str = latex(eq[0]).replace("$", "")
    eq_str = eq_str.replace("\left", "").replace("\right", "")
    ax.text(x_vals[-3], y_vals[1], f'y = {eq_str}', fontsize=12)
    ax.legend()
    plt.show()
    return eq

def plot_graph_and_draw_tangent_to_graph_at_point_9():
    '''данная функция строит график и проводит
     касательную к графику в точке x_0'''
    grid_size = 10
    x_vals = np.arange(-grid_size, grid_size + 1)
    y_vals = np.arange(-grid_size, grid_size + 1)
    point1 = (2, 3)
    point2 = (5, -4)
    fig, ax = plt.subplots()
    ax.grid(True)
    ax.plot(point1[0], point1[1], 'ro', label='Point 1')
    ax.plot(point2[0], point2[1], 'bo', label ='Point 2')
    x, y = symbols('x y')
    eq = solve((point2[1] - point1[1])*(x - point1[0]) - (point2[0] - point1[0])*(y - point1[1]), y)
    prime_eq = eq[0].diff(x)
    eq_str = latex(eq[0]).replace("$", "")
    ax.text(x_vals[-3], y_vals[1], f'y = {eq_str}', fontsize=12)
    ax.legend()
    plt.show()
    return eq, prime_eq

def plot_graph_and_draw_tangent_to_graph_at_point_10():
    '''данная функция строит график и проводит
     касательную к графику в точке x_0'''
    grid_size = 100
    x_vals = np.arange(-grid_size, grid_size + 1)
    y_vals = np.arange(-grid_size, grid_size + 1)
    x, y = symbols('x y')
    point1 = (np.random.randint(-100, 100), np.random.randint(-100, 100))
    point2 = (np.random.randint(-100, 100), np.random.randint(-100, 100))
    eq = solve((point2[1] - point1[1]) * (x - point1[0]) - (point2[0] - point1[0]) * (y - point1[1]), y)
    prime_eq = eq[0].diff(x)
    fig, ax = plt.subplots()
    ax.grid(True)
    ax.plot(point1[0], point1[1], 'ro', label='Point 1')
    ax.plot(point2[0], point2[1], 'bo', label='Point 2')
    eq_str = latex(eq[0]).replace("$", "")
    ax.text(x_vals[-3], y_vals[1], f'y = {eq_str}', fontsize=12)
    ax.legend()
    plt.show()
    return prime_eq

def plot_graph_and_draw_tangent_to_graph_at_point_11(prototype):
    '''данная функция строит график и проводит
     касательную к графику в точке x_0'''
    point1 = (np.random.randint(-1000, 1000), np.random.randint(-1000, 1000))
    point2 = (np.random.randint(-1000, 1000), np.random.randint(-1000, 1000))
    x, y = symbols('x y')
    eq = solve((point2[1] - point1[1]) * (x - point1[0]) - (point2[0] - point1[0]) * (y - point1[1]), y)
    prime_eq = eq[0].diff(x)
    equation = prototype
    while True:
        pattern = r"C\d+"
        constants = re.findall(pattern, equation)
        constants_values = {}
        for constant in constants:
            constants_values[constant] = random.randint(0, 1000)
        symbols_dict = {constant: symbols(constant) for constant in constants}
        substituted_eq = sympify(equation).subs(symbols_dict)
        for constant, value in constants_values.items():
            substituted_eq = substituted_eq.subs(symbols_dict[constant], value)
        prime = substituted_eq.diff(x)
        a = np.random.randint(-1000, 1000)
        y_0 = substituted_eq.subs(x, a)
        prime_value = prime.subs(x, a)
        if prime_eq == prime_value:
            break
    tangent = prime_value * (x - a) + y_0
    substituted_eq_lambdified = lambdify(x, substituted_eq, modules=['numpy'])
    tangent_lambdified = lambdify(x, tangent, modules=['numpy'])
    x_values = np.linspace(a - 600, a + 600, 400)
    y_values = substituted_eq_lambdified(x_values)
    tangent_values = tangent_lambdified(x_values)
    fig = plt.figure()
    ax = plt.axes()
    fig.add_axes(ax)
    ax.spines[["left", "bottom"]].set_position('zero')
    ax.spines[["top", "right"]].set_visible(False)
    ax.plot(1, 0, ">k", transform=ax.get_yaxis_transform(), clip_on=False)
    ax.plot(0, 1, "^k", transform=ax.get_xaxis_transform(), clip_on=False)
    arrow_length = 10
    ax.annotate('x', xy=(1, 0), xycoords=('axes fraction', 'data'),
                xytext=(0, arrow_length), textcoords='offset points',
                ha='center', va='bottom')
    ax.annotate('y', xy=(0, 1), xycoords=('data', 'axes fraction'),
                xytext=(arrow_length, 0), textcoords='offset points',
                ha='center', va='bottom')
    plt.plot(x_values, y_values, label='')
    plt.plot(x_values, tangent_values, label='')
    plt.axhline(color='black')
    plt.axvline(color='black')
    plt.grid(True, linewidth=0.5, linestyle='dotted')
    plt.scatter(a, y_0, color='red', label="")
    plt.plot([a, a], [y_0, 0], ':', color='red')
    plt.title('')
    plt.show()
    text = r'Найдите значение производной заданной функции: \( y= '
    task = text + str(latex(substituted_eq)) + r"\) в точке \(x_0 = " + str(
                a) + "\)"
    answer = float(prime_eq)
    return task, answer

def plot_graph_and_draw_tangent_to_graph_at_point_12():
    '''данная функция строит прямую и рисует кривую,
     которая касается прямой в точке x_0'''
    x_coords = np.array([0, 1])
    y_coords = np.array([0, 2])
    plt.grid()
    plt.plot(x_coords, y_coords, 'ro')
    x, y = symbols('x y')
    eq = Eq((y - y_coords[0]) / (y_coords[1] - y_coords[0]), (x - x_coords[0]) / (x_coords[1] - x_coords[0]))
    slope_intercept_eq = solve(eq, y)
    slope_intercept_eq
    t = symbols('t')
    curve_eq = slope_intercept_eq.evalf()[0] * t + Rational(x_coords[0] + x_coords[1], 2) - slope_intercept_eq.evalf()[0] * Rational(x_coords[0] + x_coords[1], 2)
    curve_eq
    t_values = np.arange(x_coords[0], x_coords[1], 0.01)
    x_values = [lambdify(t, curve_eq.subs(x, t)) for x in t_values]
    y_values = [lambdify(t, curve_eq.subs(x, t)) for x in x_values]
    plt.plot(x_values, y_values, 'b-')
    plt.show()
    return curve_eq

def plot_graph_and_draw_tangent_to_graph_at_point_13():
    '''данная функция строит прямую и рисует кривую,
     которая касается прямой в точке x_0'''
    x_coords = np.array([1, 5])
    y_coords = np.array([2, 4])
    plt.grid()
    plt.plot(x_coords, y_coords, 'ro')
    x, y = symbols('x y')
    eq = Eq((y - y_coords[0]) / (y_coords[1] - y_coords[0]), (x - x_coords[0]) / (x_coords[1] - x_coords[0]))
    slope_intercept_eq = solve(eq, y)

    t = symbols('t')
    curve_eq = slope_intercept_eq[0] * t + Rational(x_coords[0] + x_coords[1], 2) - slope_intercept_eq[0] * Rational(x_coords[0] + x_coords[1], 2)

    curve_derivative = diff(curve_eq, t)
    slope = curve_derivative.subs(t, x_coords[0])
    line_eq = slope * (x - x_coords[0]) + curve_eq.subs(x, x_coords[0])
    x_values = np.linspace(x_coords[0], x_coords[1], 100)
    y_line = [line_eq.subs(x, val) for val in x_values]
    y_curve = [curve_eq.subs(x, val) for val in x_values]
    plt.plot(x_values, y_line, 'r-', label='Прямая')
    plt.plot(x_values, y_curve, 'b-', label='Кривая')
    plt.plot(x_coords, y_coords, 'ro')
    plt.legend()
    plt.grid()
    plt.show()
    return curve_derivative

def plot_graph_and_draw_tangent_to_graph_at_point_14():
    '''данная функция строит прямую и рисует кривую,
     которая касается прямой в точке x_0'''
    x = symbols('x')
    point1 = (2, 3)
    point2 = (5, 7)
    # line = Line(point1, point2)
    # midpoint = (point2[0] - point1[0]) / 2
    x1, y1 = point1
    x2, y2 = point2
    m = (y2 - y1) / (x2 - x1)
    c = y1 - m * x1
    curve_tangent = m * x + c
    plt.figure()
    plt.grid(True)
    plt.scatter(point1[0], point1[1], color='red', label='Point 1')
    plt.scatter(point2[0], point2[1], color='blue', label='Point 2')
    plt.plot([point1[0], point2[0]], [point1[1], point2[1]], color='green', label='Line')
    x_vals = np.linspace(-10, 10, 100)
    y_vals_tangent = m * x_vals + c
    plt.plot(x_vals, y_vals_tangent, color='orange', label='Tangent')
    plt.legend()
    plt.show()
    return curve_tangent

def plot_graph_and_draw_tangent_to_graph_at_point_15():
    '''данная функция строит прямую и рисует кривую,
     которая касается прямой в точке x_0'''
    x = symbols('x')
    point1 = (2, 3)
    point2 = (5, 7)
    # line = Line(point1, point2)
    midpoint = ((point2[0] - point1[0]) / 2) + point1[0]
    # x1, y1 = point1
    # x2, y2 = point2
    # m = (y2 - y1) / (x2 - x1)
    # c = y1 - m * x1
    curve = sin(x)
    curve_tangent = diff(curve, x).subs(x, midpoint) * (x - midpoint) + curve.subs(x, midpoint)
    curve_fn = lambdify(x, curve, 'numpy')
    curve_tangent_fn = lambdify(x, curve_tangent, 'numpy')
    x_vals = np.linspace(-10, 10, 100)
    y_vals_curve = curve_fn(x_vals)
    y_vals_tangent = curve_tangent_fn(x_vals)
    plt.figure()
    plt.grid(True)
    plt.scatter(point1[0], point1[1], color='red', label='Point 1')
    plt.scatter(point2[0], point2[1], color='blue', label='Point 2')
    plt.plot([point1[0], point2[0]], [point1[1], point2[1]], color='green', label='Line')
    plt.plot(x_vals, y_vals_curve, color='orange', label='Curve')
    plt.plot(x_vals, y_vals_tangent, color='purple', label='Tangent')
    plt.scatter(midpoint, curve.subs(x, midpoint), color='black', label='Tangent Point')
    plt.legend()
    plt.show()
    return y_vals_curve

def plot_graph_and_draw_tangent_to_graph_at_point_16():
    x = symbols('x')
    point1 = (np.random.randint(-10, 10), np.random.randint(-10, 10))
    point2 = (np.random.randint(point1[0] + 1, 10), np.random.randint(point1[1] + 1, 10))
    midpoint = ((point2[0] - point1[0]) / 2) + point1[0]
    curve = x**2
    curve_tangent = diff(curve, x).subs(x, midpoint) * (x - midpoint) + curve.subs(x, midpoint)
    curve_fn = lambdify(x, curve, 'numpy')
    curve_tangent_fn = lambdify(x, curve_tangent, 'numpy')
    x_vals = np.linspace(-10, 10, 100)
    y_vals_curve = curve_fn(x_vals)
    y_vals_tangent = curve_tangent_fn(x_vals)
    x_left = midpoint - 2
    y_left = curve_tangent.subs(x, x_left)
    x_right = midpoint + 2
    y_right = curve_tangent.subs(x, x_right)
    plt.figure()
    plt.grid(True)
    plt.scatter(x_left, y_left, color='red', label='Point 1')
    plt.scatter(x_right, y_right, color='red', label='Point 2')
    plt.plot(x_vals, y_vals_curve, color='orange', label='Curve')
    plt.plot(x_vals, y_vals_tangent, color='purple', label='Tangent')
    plt.scatter(midpoint, curve.subs(x, midpoint), color='black', label='Tangent Point')
    plt.legend()
    plt.show()
    return y_vals_curve

def plot_graph_and_draw_tangent_to_graph_at_point_17():
    x = symbols('x')
    point1 = (np.random.randint(-10, 10), np.random.randint(-10, 10))
    point2 = (np.random.randint(point1[0] + 1, 10), np.random.randint(point1[1] + 1, 10))
    midpoint = ((point2[0] - point1[0]) / 2) + point1[0]
    curve = (x**2)/15
    prime_curve_value = diff(curve, x).subs(x, midpoint)
    curve_tangent = diff(curve, x).subs(x, midpoint) * (x - midpoint) + curve.subs(x, midpoint)
    curve_fn = lambdify(x, curve, 'numpy')
    curve_tangent_fn = lambdify(x, curve_tangent, 'numpy')
    x_vals = np.linspace(-10, 10, 100)
    y_vals_curve = curve_fn(x_vals)
    y_vals_tangent = curve_tangent_fn(x_vals)
    x_left = midpoint - 2
    y_left = curve_tangent.subs(x, x_left)
    x_right = midpoint + 2
    y_right = curve_tangent.subs(x, x_right)
    fig = plt.figure()
    ax = plt.axes()
    fig.add_axes(ax)
    ax.spines[["left", "bottom"]].set_position('zero')
    ax.spines[["top", "right"]].set_visible(False)
    ax.plot(1, 0, ">k", transform=ax.get_yaxis_transform(), clip_on=False)
    ax.plot(0, 1, "^k", transform=ax.get_xaxis_transform(), clip_on=False)
    arrow_length = 10
    ax.annotate('x', xy=(1, 0), xycoords=('axes fraction', 'data'),
                xytext=(0, arrow_length), textcoords='offset points',
                ha='center', va='bottom')
    ax.annotate('y', xy=(0, 1), xycoords=('data', 'axes fraction'),
                xytext=(arrow_length, 0), textcoords='offset points',
                ha='center', va='bottom')
    plt.axhline(color='black')
    plt.axvline(color='black')
    plt.grid(True, linewidth=0.5, linestyle='dotted')
    plt.scatter(x_left, y_left, color='green', label='Point 1')
    plt.scatter(x_right, y_right, color='green', label='Point 2')
    plt.plot(x_vals, y_vals_curve, color='orange', label='Curve')
    plt.plot(x_vals, y_vals_tangent, color='purple', label='Tangent')
    plt.scatter(midpoint, curve.subs(x, midpoint), color='red', label='Tangent Point')
    plt.plot([midpoint, midpoint], [curve.subs(x, midpoint), 0], ':', color='red')
    plt.title('')
    plt.show()
    answer = prime_curve_value.evalf(5)
    return answer

def plot_graph_and_draw_tangent_to_graph_at_point_18():
    x = symbols('x')
    point1 = (np.random.randint(-10, 10), np.random.randint(-10, 10))
    point2 = (np.random.randint(point1[0] + 1, 10), np.random.randint(point1[1] + 1, 10))
    midpoint = ((point2[0] - point1[0]) / 2) + point1[0]
    curve = (x**2)/16
    prime_curve_value = diff(curve, x).subs(x, midpoint)
    curve_tangent = diff(curve, x).subs(x, midpoint) * (x - midpoint) + curve.subs(x, midpoint)
    curve_fn = lambdify(x, curve, 'numpy')
    curve_tangent_fn = lambdify(x, curve_tangent, 'numpy')
    x_vals = np.linspace(point1[0] - 3, point2[0] + 3, 100)
    y_vals_curve = curve_fn(x_vals)
    y_vals_tangent = curve_tangent_fn(x_vals)
    x_left = point1[0] - 2
    y_left = curve_tangent.subs(x, x_left)
    x_right = point2[0] + 2
    y_right = curve_tangent.subs(x, x_right)
    fig = plt.figure()
    ax = plt.axes()
    fig.add_axes(ax)
    ax.spines[["left", "bottom"]].set_position('zero')
    ax.spines[["top", "right"]].set_visible(False)
    ax.plot(1, 0, ">k", transform=ax.get_yaxis_transform(), clip_on=False)
    ax.plot(0, 1, "^k", transform=ax.get_xaxis_transform(), clip_on=False)
    arrow_length = 10
    ax.annotate('x', xy=(1, 0), xycoords=('axes fraction', 'data'),
                xytext=(0, arrow_length), textcoords='offset points',
                ha='center', va='bottom')
    ax.annotate('y', xy=(0, 1), xycoords=('data', 'axes fraction'),
                xytext=(arrow_length, 0), textcoords='offset points',
                ha='center', va='bottom')
    plt.axhline(color='black')
    plt.axvline(color='black')
    plt.grid(True, linewidth=0.5, linestyle='dotted')
    plt.scatter(x_left, y_left, color='green', label='Point 1')
    plt.scatter(x_right, y_right, color='green', label='Point 2')
    plt.plot(x_vals, y_vals_curve, color='orange', label='Curve')
    plt.plot(x_vals, y_vals_tangent, color='purple', label='Tangent')
    plt.scatter(midpoint, curve.subs(x, midpoint), color='red', label='Tangent Point')
    plt.plot([midpoint, midpoint], [curve.subs(x, midpoint), 0], ':', color='red')
    plt.title('')
    plt.show()
    answer = float(prime_curve_value)
    return answer

def plot_graph_and_draw_tangent_to_graph_at_point_19():
    x = symbols('x')
    curve = (x ** 2) / 8
    x1 = np.random.randint(-10, 10)
    y1 = curve.subs(x, x1)
    x2 = np.random.randint(x1 + 1, 10)
    y2 = curve.subs(x, x2)
    m = (y2 - y1) / (x2 - x1)
    c = y1 - m * x1
    curve_tangent = m * x + c
    midpoint = ((x2 - x1) / 2) + x1
    prime_curve_value = diff(curve, x).subs(x, midpoint)
    y_midpoint_curve = curve.subs(x, midpoint)
    # y_midpoint_curve_tangent = curve_tangent.subs(x, midpoint)
    # prime_curve_tangent_value = diff(curve_tangent, x).subs(x, midpoint)
    # while True:
    #     a = random.uniform(0.0, 10.0)
    #     curve = (x ** 2 + a) / 8
    #     prime_curve_value = diff(curve, x).subs(x, midpoint)
    #     y_midpoint_curve = curve.subs(x, midpoint)
    #     if prime_curve_value == prime_curve_tangent_value and y_midpoint_curve == y_midpoint_curve_tangent:
    #         break
    curve_fn = lambdify(x, curve, 'numpy')
    curve_tangent_fn = lambdify(x, curve_tangent, 'numpy')
    x_vals = np.linspace(x1 - 3, x2 + 3, 100)
    y_vals_curve = curve_fn(x_vals)
    y_vals_tangent = curve_tangent_fn(x_vals)
    fig = plt.figure()
    ax = plt.axes()
    fig.add_axes(ax)
    ax.spines[["left", "bottom"]].set_position('zero')
    ax.spines[["top", "right"]].set_visible(False)
    ax.plot(1, 0, ">k", transform=ax.get_yaxis_transform(), clip_on=False)
    ax.plot(0, 1, "^k", transform=ax.get_xaxis_transform(), clip_on=False)
    arrow_length = 10
    ax.annotate('x', xy=(1, 0), xycoords=('axes fraction', 'data'),
                xytext=(0, arrow_length), textcoords='offset points',
                ha='center', va='bottom')
    ax.annotate('y', xy=(0, 1), xycoords=('data', 'axes fraction'),
                xytext=(arrow_length, 0), textcoords='offset points',
                ha='center', va='bottom')
    plt.axhline(color='black')
    plt.axvline(color='black')
    plt.grid(True, linewidth=0.5, linestyle='dotted')
    plt.scatter(x1, y1, color='green', label='Point 1')
    plt.scatter(x2, y2, color='green', label='Point 2')
    plt.plot(x_vals, y_vals_curve, color='orange', label='Curve')
    plt.plot(x_vals, y_vals_tangent, color='purple', label='Tangent')
    plt.scatter(midpoint, curve.subs(x, midpoint), color='red', label='Tangent Point')
    plt.plot([midpoint, midpoint], [curve.subs(x, midpoint), 0], ':', color='red')
    plt.title('')
    plt.show()
    answer = float(prime_curve_value)
    return answer, curve_tangent, y_midpoint_curve

# x = Symbol('x')
# y = Symbol('y')
# line_equation = Eq((5/4)*x - 3, y)
# parabola_equation = Eq((x**2)/8, y)
# intersection_point = solve((line_equation, parabola_equation), x, y)
# x_value = intersection_point[0][0]
# y_value = intersection_point[0][1]
# shift_amount = y_value

# x = Symbol('x')
# a = Symbol('a')
# line_equation = Eq((5/4) * x - 3, (x**2 + a)/8)
# solution = solve(line_equation, a)
# a_value = solution[0]


# a = Symbol('a')
# line_equation = Eq((15/8)*x - 27/4, (x**2 + a)/8)
# solution = solve(line_equation, a)
# a_value = solution[0]

# x = Symbol('x')
# equation = -(x**2) - 6*x - 8
# result = equation.subs(x, -3)
# result = simplify(result)

def plot_graph_and_draw_tangent_to_graph_at_point_20():
    x = Symbol('x')
    b = Symbol('b')
    curve_start = (x ** 2) / 8
    while True:
        x1 = np.random.randint(-10, 10)
        y1 = curve_start.subs(x, x1)
        x2 = np.random.randint(x1 + 1, 12)
        y2 = curve_start.subs(x, x2)
        m = (y2 - y1) / (x2 - x1)
        c = y1 - m * x1
        curve_tangent = m * x + c
        if ask(Q.integer(y1)) is True and ask(Q.integer(y2)) is True and m != 0:
            break
    midpoint = (x2 - x1)/2 + x1
    curve = (x ** 2 + b) / 8
    line_equation = Eq(curve_tangent, curve)
    solution = solve(line_equation, b)
    b = solution[0]
    a = b.subs(x, midpoint)
    a = simplify(a)
    curve_final = (x ** 2 + a) / 8
    prime_curve_final_value = diff(curve_final, x).subs(x, midpoint)
    curve_final_fn = lambdify(x, curve_final, 'numpy')
    curve_tangent_fn = lambdify(x, curve_tangent, 'numpy')
    x_vals = np.linspace(x1 - 3, x2 + 3, 100)
    y_vals_curve_final = curve_final_fn(x_vals)
    y_vals_tangent = curve_tangent_fn(x_vals)
    fig = plt.figure()
    ax = plt.axes()
    fig.add_axes(ax)
    ax.spines[["left", "bottom"]].set_position('zero')
    ax.spines[["top", "right"]].set_visible(False)
    ax.plot(1, 0, ">k", transform=ax.get_yaxis_transform(), clip_on=False)
    ax.plot(0, 1, "^k", transform=ax.get_xaxis_transform(), clip_on=False)
    arrow_length = 10
    ax.annotate('x', xy=(1, 0), xycoords=('axes fraction', 'data'),
                xytext=(0, arrow_length), textcoords='offset points',
                ha='center', va='bottom')
    ax.annotate('y', xy=(0, 1), xycoords=('data', 'axes fraction'),
                xytext=(arrow_length, 0), textcoords='offset points',
                ha='center', va='bottom')
    plt.axhline(color='black')
    plt.axvline(color='black')
    plt.grid(True, linewidth=0.5, linestyle='dotted')
    # plt.locator_params(axis='x', integer=True)
    # plt.locator_params(axis='y', integer=True)

    # plt.xticks(ticks=[-10, -9, -8, -7, -6, -5, -4, -3, -2, -1, 0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12])
    # plt.yticks(ticks=[-10, -9, -8, -7, -6, -5, -4, -3, -2, -1, 0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12])

    plt.xticks(ticks=list(range(-10, 13)))
    plt.yticks(ticks=list(range(-10, 13)))


    # x_ticks = [1, 2, 3, 4, 5]
    # y_ticks = [1, 2, 3, 4, 5]
    # plt.xticks(x_ticks)
    # plt.yticks(y_ticks)
    plt.scatter(x1, y1, color='green', label='Point 1')
    plt.scatter(x2, y2, color='green', label='Point 2')
    plt.plot(x_vals, y_vals_curve_final, color='orange', label='Curve')
    plt.plot(x_vals, y_vals_tangent, color='purple', label='Tangent')
    plt.scatter(midpoint, curve_final.subs(x, midpoint), color='red', label='Tangent Point')
    plt.plot([midpoint, midpoint], [curve_final.subs(x, midpoint), 0], ':', color='red')
    plt.title('')
    plt.show()
    answer = float(prime_curve_final_value)
    return answer

def plot_graph_and_draw_tangent_to_graph_at_point_21():
    x = Symbol('x')
    b = Symbol('b')
    curve_start = (x ** 2) / 8
    while True:
        x1 = np.random.randint(-10, 10)
        y1 = curve_start.subs(x, x1)
        x2 = np.random.randint(x1 + 1, 12)
        y2 = curve_start.subs(x, x2)
        m = (y2 - y1) / (x2 - x1)
        c = y1 - m * x1
        curve_tangent = m * x + c
        if ask(Q.integer(y1)) is True and ask(Q.integer(y2)) is True and m != 0:
            break
    midpoint = (x2 - x1)/2 + x1
    curve = (x ** 2 + b) / 8
    line_equation = Eq(curve_tangent, curve)
    solution = solve(line_equation, b)
    b = solution[0]
    a = b.subs(x, midpoint)
    a = simplify(a)
    curve_final = (x ** 2 + a) / 8
    prime_curve_final_value = diff(curve_final, x).subs(x, midpoint)
    curve_final_fn = lambdify(x, curve_final, 'numpy')
    curve_tangent_fn = lambdify(x, curve_tangent, 'numpy')
    x_vals = np.linspace(x1 - 3, x2 + 3, 100)
    y_vals_curve_final = curve_final_fn(x_vals)
    y_vals_tangent = curve_tangent_fn(x_vals)
    fig = plt.figure()
    ax = plt.axes()
    fig.add_axes(ax)
    ax.spines[["left", "bottom"]].set_position('zero')
    ax.spines[["top", "right"]].set_visible(False)
    ax.plot(1, 0, ">k", transform=ax.get_yaxis_transform(), clip_on=False)
    ax.plot(0, 1, "^k", transform=ax.get_xaxis_transform(), clip_on=False)
    arrow_length = 10
    ax.annotate('x', xy=(1, 0), xycoords=('axes fraction', 'data'),
                xytext=(0, arrow_length), textcoords='offset points',
                ha='center', va='bottom')
    ax.annotate('y', xy=(0, 1), xycoords=('data', 'axes fraction'),
                xytext=(arrow_length, 0), textcoords='offset points',
                ha='center', va='bottom')
    plt.axhline(color='black')
    plt.axvline(color='black')
    plt.grid(True, linewidth=0.5, linestyle='dotted')
    plt.xticks(ticks=list(range(-10, 13)))
    plt.yticks(ticks=list(range(-10, 13)))
    plt.scatter(x1, y1, color='green', label='Point 1')
    plt.scatter(x2, y2, color='green', label='Point 2')
    plt.plot(x_vals, y_vals_curve_final, color='orange', label='Curve')
    plt.plot(x_vals, y_vals_tangent, color='purple', label='Tangent')
    plt.scatter(midpoint, curve_final.subs(x, midpoint), color='red', label='Tangent Point')
    plt.plot([midpoint, midpoint], [curve_final.subs(x, midpoint), 0], ':', color='red')
    plt.title('')
    plt.show()
    answer = float(prime_curve_final_value)
    return answer

def plot_graph_and_draw_tangent_to_graph_at_point_22():
    x = Symbol('x')
    b = Symbol('b')
    curve_start = (x ** 2) / 8
    while True:
        x1 = np.random.randint(-10, 10)
        y1 = curve_start.subs(x, x1)
        x2 = np.random.randint(x1 + 1, 12)
        y2 = curve_start.subs(x, x2)
        m = (y2 - y1) / (x2 - x1)
        c = y1 - m * x1
        curve_tangent = m * x + c
        if ask(Q.integer(y1)) is True and ask(Q.integer(y2)) is True and m != 0:
            break
    midpoint = (x2 - x1)/2 + x1
    curve = (x ** 2 + b) / 8
    line_equation = Eq(curve_tangent, curve)
    solution = solve(line_equation, b)
    b = solution[0]
    a = b.subs(x, midpoint)
    a = simplify(a)
    curve_final = (x ** 2 + a) / 8
    prime_curve_final_value = diff(curve_final, x).subs(x, midpoint)
    curve_final_fn = lambdify(x, curve_final, 'numpy')
    curve_tangent_fn = lambdify(x, curve_tangent, 'numpy')
    x_vals = np.linspace(x1 - 3, x2 + 3, 100)
    y_vals_curve_final = curve_final_fn(x_vals)
    y_vals_tangent = curve_tangent_fn(x_vals)
    fig = plt.figure()
    ax = plt.axes()
    fig.add_axes(ax)
    ax.spines[["left", "bottom"]].set_position('zero')
    ax.spines[["top", "right"]].set_visible(False)
    ax.plot(1, 0, ">k", transform=ax.get_yaxis_transform(), clip_on=False)
    ax.plot(0, 1, "^k", transform=ax.get_xaxis_transform(), clip_on=False)
    arrow_length = 10
    ax.annotate('x', xy=(1, 0), xycoords=('axes fraction', 'data'),
                xytext=(0, arrow_length), textcoords='offset points',
                ha='center', va='bottom')
    ax.annotate('y', xy=(0, 1), xycoords=('data', 'axes fraction'),
                xytext=(arrow_length, 0), textcoords='offset points',
                ha='center', va='bottom')
    plt.axhline(color='black')
    plt.axvline(color='black')
    plt.grid(True, linewidth=0.5, linestyle='dotted')
    plt.axis('equal')
    plt.xticks(ticks=list(range(-10, 13)))
    plt.yticks(ticks=list(range(-10, 13)))
    plt.xlim(-10, 12)
    plt.ylim(-10, 12)
    plt.scatter(x1, y1, color='green', label='')
    plt.scatter(x2, y2, color='green', label='')
    plt.plot(x_vals, y_vals_curve_final, color='orange', label='y = f(x)')
    plt.plot(x_vals, y_vals_tangent, color='purple', label='')
    plt.scatter(midpoint, curve_final.subs(x, midpoint), color='red', label='')
    plt.plot([midpoint, midpoint], [curve_final.subs(x, midpoint), 0], ':', color='red')
    plt.text(midpoint, 0, "x\u2092", ha='center', va='bottom')
    plt.title('')
    plt.legend()
    plt.show()
    task = r'Найдите значение производной функции f(x) в точке ' + r"\(x_0 \)"
    answer = float(prime_curve_final_value)
    return task, answer

def plot_graph_and_draw_tangent_to_graph_at_point_23():
    x = Symbol('x')
    b = Symbol('b')
    curve_start = (x ** 2) / 8
    while True:
        x1 = np.random.randint(-10, 10)
        y1 = curve_start.subs(x, x1)
        x2 = np.random.randint(x1 + 1, 12)
        y2 = curve_start.subs(x, x2)
        m = (y2 - y1) / (x2 - x1)
        c = y1 - m * x1
        curve_tangent = m * x + c
        if ask(Q.integer(y1)) is True and ask(Q.integer(y2)) is True and m != 0:
            break
    midpoint = (x2 - x1)/2 + x1
    curve = (x ** 2 + b) / 8
    line_equation = Eq(curve_tangent, curve)
    solution = solve(line_equation, b)
    b = solution[0]
    a = b.subs(x, midpoint)
    a = simplify(a)
    curve_final = (x ** 2 + a) / 8
    prime_curve_final_value = diff(curve_final, x).subs(x, midpoint)
    curve_final_fn = lambdify(x, curve_final, 'numpy')
    curve_tangent_fn = lambdify(x, curve_tangent, 'numpy')
    x_vals = np.linspace(x1 - 16, x2 + 16, 100)
    y_vals_curve_final = curve_final_fn(x_vals)
    y_vals_tangent = curve_tangent_fn(x_vals)
    fig = plt.figure()
    ax = plt.axes()
    fig.add_axes(ax)
    ax.spines[["left", "bottom"]].set_position('zero')
    ax.spines[["top", "right"]].set_visible(False)
    ax.plot(1, 0, ">k", transform=ax.get_yaxis_transform(), clip_on=False)
    ax.plot(0, 1, "^k", transform=ax.get_xaxis_transform(), clip_on=False)
    arrow_length = 10
    ax.annotate('x', xy=(1, 0), xycoords=('axes fraction', 'data'),
                xytext=(0, arrow_length), textcoords='offset points',
                ha='center', va='bottom')
    ax.annotate('y', xy=(0, 1), xycoords=('data', 'axes fraction'),
                xytext=(arrow_length, 0), textcoords='offset points',
                ha='center', va='bottom')
    plt.axhline(color='black')
    plt.axvline(color='black')
    plt.grid(True, linewidth=0.5, linestyle='dotted')
    plt.axis('equal')
    plt.xticks(ticks=list(range(-17, 17)))
    plt.yticks(ticks=list(range(-17, 17)))
    plt.xlim(-10, 12)
    plt.ylim(-10, 12)
    plt.scatter(x1, y1, color='green', label='')
    plt.scatter(x2, y2, color='green', label='')
    plt.plot(x_vals, y_vals_curve_final, color='orange', label='y = f(x)')
    plt.plot(x_vals, y_vals_tangent, color='purple', label='')
    plt.scatter(midpoint, curve_final.subs(x, midpoint), color='red', label='')
    plt.plot([midpoint, midpoint], [curve_final.subs(x, midpoint), 0], ':', color='red')
    plt.text(midpoint, 0, "x\u2092", ha='center', va='bottom')
    plt.title('')
    plt.legend()
    plt.show()
    task = r'Найдите значение производной функции f(x) в точке ' + r"\(x_0 \)"
    answer = float(prime_curve_final_value)
    return task, answer

def plot_graph_quadratic_function_and_draw_tangent_to_graph_at_point_1():
    x = Symbol('x')
    x1 = np.random.randint(-10, 10)
    y1 = np.random.randint(-10, 10)
    x2 = np.random.randint(-10, 10)
    while x2 == x1:
        x2 = np.random.randint(-10, 10)
    y2 = np.random.randint(-10, 10)
    while y2 == y1:
        y2 = np.random.randint(-10, 10)
    k = (y2 - y1) / (x2 - x1)
    b = y1 - k * x1
    curve_tangent = k * x + b
    x0 = np.random.uniform(x1, x2)
    while x0 == x1 or x0 == x2:
        x0 = np.random.uniform(x1, x2)
    y0 = curve_tangent.subs(x, x0)
    C1 = np.random.randint(-10, 10)
    while C1 == 0:
        C1 = np.random.randint(-10, 10)
    C2 = k - C1*x0
    C3 = y0 - k*x0 + (C1/2)*(x0**2)
    curve = (C1 / 2) * (x ** 2) + C2 * x + C3
    curve_fn = lambdify(x, curve, 'numpy')
    curve_tangent_fn = lambdify(x, curve_tangent, 'numpy')
    x_vals = np.linspace(-26, 26, 5000)
    y_vals_curve_final = curve_fn(x_vals)
    y_vals_tangent = curve_tangent_fn(x_vals)
    fig = plt.figure()
    ax = plt.axes()
    fig.add_axes(ax)
    ax.spines[["left", "bottom"]].set_position('zero')
    ax.spines[["top", "right"]].set_visible(False)
    ax.plot(1, 0, ">k", transform=ax.get_yaxis_transform(), clip_on=False)
    ax.plot(0, 1, "^k", transform=ax.get_xaxis_transform(), clip_on=False)
    arrow_length = 10
    ax.annotate('x', xy=(1, 0), xycoords=('axes fraction', 'data'),
                xytext=(0, arrow_length), textcoords='offset points',
                ha='center', va='bottom')
    ax.annotate('y', xy=(0, 1), xycoords=('data', 'axes fraction'),
                xytext=(arrow_length, 0), textcoords='offset points',
                ha='center', va='bottom')
    plt.axhline(color='black')
    plt.axvline(color='black')
    plt.grid(True, linewidth=0.5, linestyle='dotted')
    plt.axis('equal')
    plt.xticks(ticks=list(range(-17, 17)))
    plt.yticks(ticks=list(range(-17, 17)))
    plt.xlim(-10, 10)
    plt.ylim(-10, 10)
    plt.scatter(x1, y1, color='green', label='')
    plt.scatter(x2, y2, color='green', label='')
    plt.plot(x_vals, y_vals_curve_final, color='orange', label='y = f(x)')
    plt.plot(x_vals, y_vals_tangent, color='purple', label='')
    plt.scatter(x0, y0, color='red', label='')
    plt.plot([x0, x0], [y0, 0], ':', color='red')
    plt.text(x0, 0, "x\u2092", ha='center', va='bottom')
    plt.title('')
    plt.legend()
    plt.show()
    task = r'Найдите значение производной функции f(x) в точке ' + r"\(x_0 \)"
    answer = round(k, 5)
    return task, answer

def plot_graph_cubic_function_and_draw_tangent_to_graph_at_point_1():
    x = Symbol('x')
    x1 = np.random.randint(-10, 10)
    y1 = np.random.randint(-10, 10)
    x2 = np.random.randint(-10, 10)
    while x2 == x1:
        x2 = np.random.randint(-10, 10)
    y2 = np.random.randint(-10, 10)
    while y2 == y1:
        y2 = np.random.randint(-10, 10)
    k = (y2 - y1) / (x2 - x1)
    b = y1 - k * x1
    curve_tangent = k * x + b
    x0 = np.random.uniform(x1, x2)
    while x0 == x1 or x0 == x2:
        x0 = np.random.uniform(x1, x2)
    y0 = curve_tangent.subs(x, x0)
    C1 = np.random.randint(-10, 10)
    while C1 == 0:
        C1 = np.random.randint(-10, 10)
    C2 = np.random.randint(-10, 10)
    while C2 == 0:
        C2 = np.random.randint(-10, 10)
    C3 = k - C1*(x0**2) - C2*x0
    C4 = y0 - k*x0 + 2*(C1/3)*(x0**3) + (C2/2)*(x0**2)
    curve = (C1 / 3) * (x ** 3) + (C2/2) * (x**2) + C3 * x + C4
    curve_fn = lambdify(x, curve, 'numpy')
    curve_tangent_fn = lambdify(x, curve_tangent, 'numpy')
    x_vals = np.linspace(-26, 26, 5000)
    y_vals_curve_final = curve_fn(x_vals)
    y_vals_tangent = curve_tangent_fn(x_vals)
    fig = plt.figure()
    ax = plt.axes()
    fig.add_axes(ax)
    ax.spines[["left", "bottom"]].set_position('zero')
    ax.spines[["top", "right"]].set_visible(False)
    ax.plot(1, 0, ">k", transform=ax.get_yaxis_transform(), clip_on=False)
    ax.plot(0, 1, "^k", transform=ax.get_xaxis_transform(), clip_on=False)
    arrow_length = 10
    ax.annotate('x', xy=(1, 0), xycoords=('axes fraction', 'data'),
                xytext=(0, arrow_length), textcoords='offset points',
                ha='center', va='bottom')
    ax.annotate('y', xy=(0, 1), xycoords=('data', 'axes fraction'),
                xytext=(arrow_length, 0), textcoords='offset points',
                ha='center', va='bottom')
    plt.axhline(color='black')
    plt.axvline(color='black')
    plt.grid(True, linewidth=0.5, linestyle='dotted')
    plt.axis('equal')
    plt.xticks(ticks=list(range(-17, 17)))
    plt.yticks(ticks=list(range(-17, 17)))
    plt.xlim(-10, 10)
    plt.ylim(-10, 10)
    plt.scatter(x1, y1, color='green', label='')
    plt.scatter(x2, y2, color='green', label='')
    plt.plot(x_vals, y_vals_curve_final, color='orange', label='y = f(x)')
    plt.plot(x_vals, y_vals_tangent, color='purple', label='')
    plt.scatter(x0, y0, color='red', label='')
    plt.plot([x0, x0], [y0, 0], ':', color='red')
    plt.text(x0, 0, "x\u2092", ha='center', va='bottom')
    plt.title('')
    plt.legend()
    plt.show()
    task = r'Найдите значение производной функции f(x) в точке ' + r"\(x_0 \)"
    answer = round(k, 5)
    return task, answer

def plot_graph_function_fourth_degree_and_draw_tangent_to_graph_at_point_1():
    x = Symbol('x')
    x1 = np.random.randint(-10, 10)
    y1 = np.random.randint(-10, 10)
    x2 = np.random.randint(-10, 10)
    while x2 == x1:
        x2 = np.random.randint(-10, 10)
    y2 = np.random.randint(-10, 10)
    while y2 == y1:
        y2 = np.random.randint(-10, 10)
    k = (y2 - y1) / (x2 - x1)
    b = y1 - k * x1
    curve_tangent = k * x + b
    x0 = np.random.uniform(x1, x2)
    while x0 == x1 or x0 == x2:
        x0 = np.random.uniform(x1, x2)
    y0 = curve_tangent.subs(x, x0)
    C1 = np.random.randint(-10, 10)
    while C1 == 0:
        C1 = np.random.randint(-10, 10)
    C2 = np.random.randint(-10, 10)
    while C2 == 0:
        C2 = np.random.randint(-10, 10)
    C3 = np.random.randint(-10, 10)
    while C3 == 0:
        C3 = np.random.randint(-10, 10)
    C4 = k - C1*(x0**3) - C2*(x0**2) - C3*x0
    C5 = y0 - k*x0 + 3*(C1/4)*(x0**4) + 2*(C2/3)*(x0**3) + (C3/2)*(x0**2)
    curve = (C1 / 4) * (x ** 4) + (C2 / 3) * (x ** 3) + (C3/2) * (x ** 2) + C4 * x + C5
    curve_fn = lambdify(x, curve, 'numpy')
    curve_tangent_fn = lambdify(x, curve_tangent, 'numpy')
    x_vals = np.linspace(-26, 26, 5000)
    y_vals_curve_final = curve_fn(x_vals)
    y_vals_tangent = curve_tangent_fn(x_vals)
    fig = plt.figure()
    ax = plt.axes()
    fig.add_axes(ax)
    ax.spines[["left", "bottom"]].set_position('zero')
    ax.spines[["top", "right"]].set_visible(False)
    ax.plot(1, 0, ">k", transform=ax.get_yaxis_transform(), clip_on=False)
    ax.plot(0, 1, "^k", transform=ax.get_xaxis_transform(), clip_on=False)
    arrow_length = 10
    ax.annotate('x', xy=(1, 0), xycoords=('axes fraction', 'data'),
                xytext=(0, arrow_length), textcoords='offset points',
                ha='center', va='bottom')
    ax.annotate('y', xy=(0, 1), xycoords=('data', 'axes fraction'),
                xytext=(arrow_length, 0), textcoords='offset points',
                ha='center', va='bottom')
    plt.axhline(color='black')
    plt.axvline(color='black')
    plt.grid(True, linewidth=0.5, linestyle='dotted')
    plt.axis('equal')
    plt.xticks(ticks=list(range(-17, 17)))
    plt.yticks(ticks=list(range(-17, 17)))
    plt.xlim(-10, 10)
    plt.ylim(-10, 10)
    plt.scatter(x1, y1, color='green', label='')
    plt.scatter(x2, y2, color='green', label='')
    plt.plot(x_vals, y_vals_curve_final, color='orange', label='y = f(x)')
    plt.plot(x_vals, y_vals_tangent, color='purple', label='')
    plt.scatter(x0, y0, color='red', label='')
    plt.plot([x0, x0], [y0, 0], ':', color='red')
    plt.text(x0, 0, "x\u2092", ha='center', va='bottom')
    plt.title('')
    plt.legend()
    plt.show()
    task = r'Найдите значение производной функции f(x) в точке ' + r"\(x_0 \)"
    answer = round(k, 5)
    return task, answer

def plot_graph_function_fifth_degree_and_draw_tangent_to_graph_at_point_1():
    x = Symbol('x')
    x1 = np.random.randint(-10, 10)
    y1 = np.random.randint(-10, 10)
    x2 = np.random.randint(-10, 10)
    while x2 == x1:
        x2 = np.random.randint(-10, 10)
    y2 = np.random.randint(-10, 10)
    while y2 == y1:
        y2 = np.random.randint(-10, 10)
    k = (y2 - y1) / (x2 - x1)
    b = y1 - k * x1
    curve_tangent = k * x + b
    x0 = np.random.uniform(x1, x2)
    while x0 == x1 or x0 == x2:
        x0 = np.random.uniform(x1, x2)
    y0 = curve_tangent.subs(x, x0)
    C1 = np.random.randint(-10, 10)
    while C1 == 0:
        C1 = np.random.randint(-10, 10)
    C2 = np.random.randint(-10, 10)
    while C2 == 0:
        C2 = np.random.randint(-10, 10)
    C3 = np.random.randint(-10, 10)
    while C3 == 0:
        C3 = np.random.randint(-10, 10)
    C4 = np.random.randint(-10, 10)
    while C4 == 0:
        C4 = np.random.randint(-10, 10)
    C5 = k - C1*(x0**4) - C2*(x0**3) - C3*(x0**2) - C4*x0
    C6 = y0 - k*x0 + 4*(C1/5)*(x0**5) + 3*(C2/4)*(x0**4) + 2*(C3/3)*(x0**3) + (C4/2)*(x0**2)
    curve = (C1 / 5) * (x ** 5) + (C2 / 4) * (x ** 4) + (C3/3) * (x ** 3) + (C4/2) * (x**2) + C5 * x + C6
    curve_fn = lambdify(x, curve, 'numpy')
    curve_tangent_fn = lambdify(x, curve_tangent, 'numpy')
    x_vals = np.linspace(-26, 26, 20000)
    y_vals_curve_final = curve_fn(x_vals)
    y_vals_tangent = curve_tangent_fn(x_vals)
    fig = plt.figure()
    ax = plt.axes()
    fig.add_axes(ax)
    ax.spines[["left", "bottom"]].set_position('zero')
    ax.spines[["top", "right"]].set_visible(False)
    ax.plot(1, 0, ">k", transform=ax.get_yaxis_transform(), clip_on=False)
    ax.plot(0, 1, "^k", transform=ax.get_xaxis_transform(), clip_on=False)
    arrow_length = 10
    ax.annotate('x', xy=(1, 0), xycoords=('axes fraction', 'data'),
                xytext=(0, arrow_length), textcoords='offset points',
                ha='center', va='bottom')
    ax.annotate('y', xy=(0, 1), xycoords=('data', 'axes fraction'),
                xytext=(arrow_length, 0), textcoords='offset points',
                ha='center', va='bottom')
    plt.axhline(color='black')
    plt.axvline(color='black')
    plt.grid(True, linewidth=0.5, linestyle='dotted')
    plt.axis('equal')
    plt.xticks(ticks=list(range(-17, 17)))
    plt.yticks(ticks=list(range(-17, 17)))
    plt.xlim(-10, 10)
    plt.ylim(-10, 10)
    plt.scatter(x1, y1, color='green', label='')
    plt.scatter(x2, y2, color='green', label='')
    plt.plot(x_vals, y_vals_curve_final, color='orange', label='y = f(x)')
    plt.plot(x_vals, y_vals_tangent, color='purple', label='')
    plt.scatter(x0, y0, color='red', label='')
    plt.plot([x0, x0], [y0, 0], ':', color='red')
    plt.text(x0, 0, "x\u2092", ha='center', va='bottom')
    plt.title('')
    plt.legend()
    plt.show()
    task = r'Найдите значение производной функции f(x) в точке ' + r"\(x_0 \)"
    answer = round(k, 5)
    return task, answer

def plot_graph_function_sixth_degree_and_draw_tangent_to_graph_at_point_1():
    x = Symbol('x')
    x1 = np.random.randint(-10, 10)
    y1 = np.random.randint(-10, 10)
    x2 = np.random.randint(-10, 10)
    while x2 == x1:
        x2 = np.random.randint(-10, 10)
    y2 = np.random.randint(-10, 10)
    while y2 == y1:
        y2 = np.random.randint(-10, 10)
    k = (y2 - y1) / (x2 - x1)
    b = y1 - k * x1
    curve_tangent = k * x + b
    x0 = np.random.uniform(x1, x2)
    while x0 == x1 or x0 == x2:
        x0 = np.random.uniform(x1, x2)
    y0 = curve_tangent.subs(x, x0)
    C1 = np.random.randint(-10, 10)
    while C1 == 0:
        C1 = np.random.randint(-10, 10)
    C2 = np.random.randint(-10, 10)
    while C2 == 0:
        C2 = np.random.randint(-10, 10)
    C3 = np.random.randint(-10, 10)
    while C3 == 0:
        C3 = np.random.randint(-10, 10)
    C4 = np.random.randint(-10, 10)
    while C4 == 0:
        C4 = np.random.randint(-10, 10)
    C5 = np.random.randint(-10, 10)
    while C5 == 0:
        C5 = np.random.randint(-10, 10)
    C6 = k - C1*(x0**5) - C2*(x0**4) - C3*(x0**3) - C4*(x0**2) - C5*x0
    C7 = y0 - k*x0 + 5*(C1/6)*(x0**6) + 4*(C2/5)*(x0**5) + 3*(C3/4)*(x0**4) + 2*(C4/3)*(x0**3) + (C5/2)*(x0**2)
    curve = (C1 / 6) * (x ** 6) + (C2 / 5) * (x ** 5) + (C3/4) * (x ** 4) + (C4/3) * (x**3) + (C5/2) * (x ** 2) + C6 * x + C7
    curve_fn = lambdify(x, curve, 'numpy')
    curve_tangent_fn = lambdify(x, curve_tangent, 'numpy')
    x_vals = np.linspace(-26, 26, 20000)
    y_vals_curve_final = curve_fn(x_vals)
    y_vals_tangent = curve_tangent_fn(x_vals)
    fig = plt.figure()
    ax = plt.axes()
    fig.add_axes(ax)
    ax.spines[["left", "bottom"]].set_position('zero')
    ax.spines[["top", "right"]].set_visible(False)
    ax.plot(1, 0, ">k", transform=ax.get_yaxis_transform(), clip_on=False)
    ax.plot(0, 1, "^k", transform=ax.get_xaxis_transform(), clip_on=False)
    arrow_length = 10
    ax.annotate('x', xy=(1, 0), xycoords=('axes fraction', 'data'),
                xytext=(0, arrow_length), textcoords='offset points',
                ha='center', va='bottom')
    ax.annotate('y', xy=(0, 1), xycoords=('data', 'axes fraction'),
                xytext=(arrow_length, 0), textcoords='offset points',
                ha='center', va='bottom')
    plt.axhline(color='black')
    plt.axvline(color='black')
    plt.grid(True, linewidth=0.5, linestyle='dotted')
    plt.axis('equal')
    plt.xticks(ticks=list(range(-17, 17)))
    plt.yticks(ticks=list(range(-17, 17)))
    plt.xlim(-10, 10)
    plt.ylim(-10, 10)
    plt.scatter(x1, y1, color='green', label='')
    plt.scatter(x2, y2, color='green', label='')
    plt.plot(x_vals, y_vals_curve_final, color='orange', label='y = f(x)')
    plt.plot(x_vals, y_vals_tangent, color='purple', label='')
    plt.scatter(x0, y0, color='red', label='')
    plt.plot([x0, x0], [y0, 0], ':', color='red')
    plt.text(x0, 0, "x\u2092", ha='center', va='bottom')
    plt.title('')
    plt.legend()
    plt.show()
    task = r'Найдите значение производной функции f(x) в точке ' + r"\(x_0 \)"
    answer = round(k, 5)
    return task, answer

def plot_graph_function_sixth_degree_and_draw_tangent_to_graph_at_point_2():
    x = Symbol('x')
    while True:
        x1 = np.random.randint(-10, 10)
        y1 = np.random.randint(-10, 10)
        x2 = np.random.randint(-10, 10)
        while x2 == x1:
            x2 = np.random.randint(-10, 10)
        y2 = np.random.randint(-10, 10)
        while y2 == y1:
            y2 = np.random.randint(-10, 10)
        frac = Rational(y2 - y1, x2 - x1)
        if frac.is_finite and ask(Q.integer(frac*10000)) is True and abs(frac) < 2.25:
            break
    k = (y2 - y1) / (x2 - x1)
    b = y1 - k * x1
    curve_tangent = k * x + b
    x0 = np.random.uniform(x1, x2)
    while x0 == x1 or x0 == x2:
        x0 = np.random.uniform(x1, x2)
    y0 = curve_tangent.subs(x, x0)
    C1 = np.random.uniform(-0.0001, 0.0001)
    while C1 == 0:
        C1 = np.random.uniform(-0.0001, 0.0001)
    C2 = np.random.uniform(-0.001, 0.001)
    while C2 > -0.0001 and C2 < 0.0001:
        C2 = np.random.uniform(-0.001, 0.001)
    C3 = np.random.uniform(-0.01, 0.01)
    while C3 > -0.001 and C3 < 0.001:
        C3 = np.random.uniform(-0.01, 0.01)
    C4 = np.random.uniform(-0.1, 0.1)
    while C4 > -0.01 and C4 < 0.01:
        C4 = np.random.uniform(-0.1, 0.1)
    C5 = np.random.uniform(-1, 1)
    while C5 > -0.1 and C5 < 0.1:
        C5 = np.random.uniform(-1, 1)
    C6 = k - C1*(x0**5) - C2*(x0**4) - C3*(x0**3) - C4*(x0**2) - C5*x0
    C7 = y0 - k*x0 + 5*(C1/6)*(x0**6) + 4*(C2/5)*(x0**5) + 3*(C3/4)*(x0**4) + 2*(C4/3)*(x0**3) + (C5/2)*(x0**2)
    curve = (C1 / 6) * (x ** 6) + (C2 / 5) * (x ** 5) + (C3/4) * (x ** 4) + (C4/3) * (x**3) + (C5/2) * (x ** 2) + C6 * x + C7
    curve_fn = lambdify(x, curve, 'numpy')
    curve_tangent_fn = lambdify(x, curve_tangent, 'numpy')
    x_vals = np.linspace(-16, 16, 20000)
    y_vals_curve_final = curve_fn(x_vals)
    y_vals_tangent = curve_tangent_fn(x_vals)
    fig = plt.figure()
    ax = plt.axes()
    fig.add_axes(ax)
    ax.spines[["left", "bottom"]].set_position('zero')
    ax.spines[["top", "right"]].set_visible(False)
    ax.plot(1, 0, ">k", transform=ax.get_yaxis_transform(), clip_on=False)
    ax.plot(0, 1, "^k", transform=ax.get_xaxis_transform(), clip_on=False)
    arrow_length = 10
    ax.annotate('x', xy=(1, 0), xycoords=('axes fraction', 'data'),
                xytext=(0, arrow_length), textcoords='offset points',
                ha='center', va='bottom')
    ax.annotate('y', xy=(0, 1), xycoords=('data', 'axes fraction'),
                xytext=(arrow_length, 0), textcoords='offset points',
                ha='center', va='bottom')
    plt.axhline(color='black')
    plt.axvline(color='black')
    plt.grid(True, linewidth=0.5, linestyle='dotted')
    plt.axis('equal')
    ax.set_xticks(range(-17, 17))
    ax.set_yticks(range(-17, 17))
    ax.set_xticklabels([i if i % 2 == 0 else '' for i in range(-17, 17)])
    ax.set_yticklabels([i if i % 2 == 0 else '' for i in range(-17, 17)])
    plt.xlim(-10, 10)
    plt.ylim(-10, 10)
    plt.scatter(x1, y1, color='green', label='')
    plt.scatter(x2, y2, color='green', label='')
    plt.plot(x_vals, y_vals_curve_final, color='orange', label='y = f(x)')
    plt.plot(x_vals, y_vals_tangent, color='purple', label='')
    plt.scatter(x0, y0, color='red', label='')
    plt.plot([x0, x0], [y0, 0], ':', color='red')
    plt.text(x0, 0, "x\u2092", ha='center', va='bottom')
    plt.title('')
    plt.legend()
    plt.show()
    task = r'Найдите значение производной функции f(x) в точке ' + r"\(x_0 \)"
    answer = float(k)
    return task, answer, curve

def plot_graph_function_sixth_degree_and_draw_tangent_to_graph_at_point_3():
    x = Symbol('x')
    while True:
        x1 = np.random.randint(-10, 10)
        y1 = np.random.randint(-10, 10)
        x2 = np.random.randint(-10, 10)
        while x2 == x1:
            x2 = np.random.randint(-10, 10)
        y2 = np.random.randint(-10, 10)
        while y2 == y1:
            y2 = np.random.randint(-10, 10)
        frac = Rational(y2 - y1, x2 - x1)
        if frac.is_finite and ask(Q.integer(frac * 10000)) is True and abs(frac) < 2.25:
            break
    k = (y2 - y1) / (x2 - x1)
    b = y1 - k * x1
    curve_tangent = k * x + b
    while True:
        x0 = np.random.uniform(x1, x2)
        while x0 == x1 or x0 == x2:
            x0 = np.random.uniform(x1, x2)
        y0 = curve_tangent.subs(x, x0)
        C1 = np.random.uniform(-0.0001, 0.0001)
        while C1 == 0:
            C1 = np.random.uniform(-0.0001, 0.0001)
        C2 = np.random.uniform(-0.001, 0.001)
        while C2 > -0.0001 and C2 < 0.0001:
            C2 = np.random.uniform(-0.001, 0.001)
        C3 = np.random.uniform(-0.01, 0.01)
        while C3 > -0.001 and C3 < 0.001:
            C3 = np.random.uniform(-0.01, 0.01)
        C4 = np.random.uniform(-0.1, 0.1)
        while C4 > -0.01 and C4 < 0.01:
            C4 = np.random.uniform(-0.1, 0.1)
        C5 = np.random.uniform(-1, 1)
        while C5 > -0.1 and C5 < 0.1:
            C5 = np.random.uniform(-1, 1)
        C6 = k - C1 * (x0 ** 5) - C2 * (x0 ** 4) - C3 * (x0 ** 3) - C4 * (x0 ** 2) - C5 * x0
        C7 = y0 - k * x0 + 5 * (C1 / 6) * (x0 ** 6) + 4 * (C2 / 5) * (x0 ** 5) + 3 * (C3 / 4) * (x0 ** 4) + 2 * (C4 / 3) * (
                    x0 ** 3) + (C5 / 2) * (x0 ** 2)
        curve = (C1 / 6) * (x ** 6) + (C2 / 5) * (x ** 5) + (C3 / 4) * (x ** 4) + (C4 / 3) * (x ** 3) + (C5 / 2) * (
                    x ** 2) + C6 * x + C7
        values = []
        prime = curve.diff(x)
        eq_diff = Eq(prime, 0)
        critical_points = solve(eq_diff, x)
        for number in critical_points:
            if im(number) == 0:
                values.append(curve.subs(x, number))
        condition = all(abs(point) < 10 for point in values)
        if condition is True:
            break
    curve_fn = lambdify(x, curve, 'numpy')
    curve_tangent_fn = lambdify(x, curve_tangent, 'numpy')
    x_vals = np.linspace(-16, 16, 20000)
    y_vals_curve_final = curve_fn(x_vals)
    y_vals_tangent = curve_tangent_fn(x_vals)
    fig = plt.figure()
    ax = plt.axes()
    fig.add_axes(ax)
    ax.spines[["left", "bottom"]].set_position('zero')
    ax.spines[["top", "right"]].set_visible(False)
    ax.plot(1, 0, ">k", transform=ax.get_yaxis_transform(), clip_on=False)
    ax.plot(0, 1, "^k", transform=ax.get_xaxis_transform(), clip_on=False)
    arrow_length = 10
    ax.annotate('x', xy=(1, 0), xycoords=('axes fraction', 'data'),
                xytext=(0, arrow_length), textcoords='offset points',
                ha='center', va='bottom')
    ax.annotate('y', xy=(0, 1), xycoords=('data', 'axes fraction'),
                xytext=(arrow_length, 0), textcoords='offset points',
                ha='center', va='bottom')
    plt.axhline(color='black')
    plt.axvline(color='black')
    plt.grid(True, linewidth=0.5, linestyle='dotted')
    plt.axis('equal')
    ax.set_xticks(range(-17, 17))
    ax.set_yticks(range(-17, 17))
    ax.set_xticklabels([i if i % 2 == 0 else '' for i in range(-17, 17)])
    ax.set_yticklabels([i if i % 2 == 0 else '' for i in range(-17, 17)])
    plt.xlim(-10, 10)
    plt.ylim(-10, 10)
    plt.scatter(x1, y1, color='green', label='')
    plt.scatter(x2, y2, color='green', label='')
    plt.plot(x_vals, y_vals_curve_final, color='orange', label='y = f(x)')
    plt.plot(x_vals, y_vals_tangent, color='purple', label='')
    plt.scatter(x0, y0, color='red', label='')
    plt.plot([x0, x0], [y0, 0], ':', color='red')
    plt.text(x0, 0, "x\u2092", ha='center', va='bottom')
    plt.title('')
    plt.legend()
    plt.show()
    task = r'Найдите значение производной функции f(x) в точке ' + r"\(x_0 \)"
    answer = float(k)
    return task, answer

def plot_graph_function_sixth_degree_and_draw_tangent_to_graph_at_point_4():
    x = Symbol('x')
    while True:
        x1 = np.random.randint(-10, 10)
        y1 = np.random.randint(-10, 10)
        x2 = np.random.randint(-10, 10)
        while x2 == x1:
            x2 = np.random.randint(-10, 10)
        y2 = np.random.randint(-10, 10)
        while y2 == y1:
            y2 = np.random.randint(-10, 10)
        frac = Rational(y2 - y1, x2 - x1)
        if frac.is_finite and ask(Q.integer(frac * 10000)) is True and abs(frac) < 2.25:
            break
    k = (y2 - y1) / (x2 - x1)
    b = y1 - k * x1
    curve_tangent = k * x + b
    x0 = np.random.uniform(x1, x2)
    while x0 == x1 or x0 == x2:
        x0 = np.random.uniform(x1, x2)
    y0 = curve_tangent.subs(x, x0)
    while True:
        C1 = np.random.uniform(-0.0001, 0.0001)
        while C1 == 0:
            C1 = np.random.uniform(-0.0001, 0.0001)
        C2 = np.random.uniform(-0.001, 0.001)
        while C2 > -0.0001 and C2 < 0.0001:
            C2 = np.random.uniform(-0.001, 0.001)
        C3 = np.random.uniform(-0.01, 0.01)
        while C3 > -0.001 and C3 < 0.001:
            C3 = np.random.uniform(-0.01, 0.01)
        C4 = np.random.uniform(-0.1, 0.1)
        while C4 > -0.01 and C4 < 0.01:
            C4 = np.random.uniform(-0.1, 0.1)
        C5 = np.random.uniform(-1, 1)
        while C5 > -0.1 and C5 < 0.1:
            C5 = np.random.uniform(-1, 1)
        C6 = k - C1 * (x0 ** 5) - C2 * (x0 ** 4) - C3 * (x0 ** 3) - C4 * (x0 ** 2) - C5 * x0
        C7 = y0 - k * x0 + 5 * (C1 / 6) * (x0 ** 6) + 4 * (C2 / 5) * (x0 ** 5) + 3 * (C3 / 4) * (x0 ** 4) + 2 * (C4 / 3) * (x0 ** 3) + (C5 / 2) * (x0 ** 2)
        curve = (C1 / 6) * (x ** 6) + (C2 / 5) * (x ** 5) + (C3 / 4) * (x ** 4) + (C4 / 3) * (x ** 3) + (C5 / 2) * (x ** 2) + C6 * x + C7
        values = []
        prime = curve.diff(x)
        eq_diff = Eq(prime, 0)
        critical_points = solve(eq_diff, x)
        for number in critical_points:
            if im(number) == 0:
                values.append(curve.subs(x, number))
        condition = all(abs(point) < 10 for point in values)
        if condition is True:
            break
    curve_fn = lambdify(x, curve, 'numpy')
    curve_tangent_fn = lambdify(x, curve_tangent, 'numpy')
    x_vals = np.linspace(-16, 16, 20000)
    y_vals_curve_final = curve_fn(x_vals)
    y_vals_tangent = curve_tangent_fn(x_vals)
    fig = plt.figure()
    ax = plt.axes()
    fig.add_axes(ax)
    ax.spines[["left", "bottom"]].set_position('zero')
    ax.spines[["top", "right"]].set_visible(False)
    ax.plot(1, 0, ">k", transform=ax.get_yaxis_transform(), clip_on=False)
    ax.plot(0, 1, "^k", transform=ax.get_xaxis_transform(), clip_on=False)
    arrow_length = 10
    ax.annotate('x', xy=(1, 0), xycoords=('axes fraction', 'data'),
                xytext=(0, arrow_length), textcoords='offset points',
                ha='center', va='bottom')
    ax.annotate('y', xy=(0, 1), xycoords=('data', 'axes fraction'),
                xytext=(arrow_length, 0), textcoords='offset points',
                ha='center', va='bottom')
    plt.axhline(color='black')
    plt.axvline(color='black')
    plt.grid(True, linewidth=0.5, linestyle='dotted')
    plt.axis('equal')
    ax.set_xticks(range(-17, 17))
    ax.set_yticks(range(-17, 17))
    ax.set_xticklabels([i if i % 2 == 0 else '' for i in range(-17, 17)])
    ax.set_yticklabels([i if i % 2 == 0 else '' for i in range(-17, 17)])
    plt.xlim(-10, 10)
    plt.ylim(-10, 10)
    plt.scatter(x1, y1, color='green', label='')
    plt.scatter(x2, y2, color='green', label='')
    plt.plot(x_vals, y_vals_curve_final, color='orange', label='y = f(x)')
    plt.plot(x_vals, y_vals_tangent, color='purple', label='')
    plt.scatter(x0, y0, color='red', label='')
    plt.plot([x0, x0], [y0, 0], ':', color='red')
    plt.text(x0, 0, "x\u2092", ha='center', va='bottom')
    plt.title('')
    plt.legend()
    plt.show()
    task = r'Найдите значение производной функции f(x) в точке ' + r"\(x_0 \)"
    answer = float(k)
    return task, answer






    #     prime = curve.diff(x)
    #     eq_diff = Eq(prime, 0)
    #     critical_points = solve(eq_diff, x)
    #     for number in critical_points:
    #         if Abs(number) < 13:
    #             break
    #
    # while True:
    #     values = []
    #     for i in critical_points:
    #         if Abs(i) < 13:
    #             values.append(curve.subs(x, i))
    #     values.extend([curve.subs(x, -13), curve.subs(x, 13)])
    #     for point in values:
    #         if Abs(point) < 10:
    #             break








