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
        trig_functions = ['sin', 'cos', 'tan', 'cot']
        pattern_1 = "|".join(trig_functions)
        if re.search(pattern_1, equation):
            result = simplify(prime)
            answer = result.subs(x, pi/a)
            task = r'Вычислите значение производной заданной функции: \( y= ' + str(
                latex(substituted_eq)) + r"\) в точке \(x_0 = " + str(latex(pi/a) + r"\)")
            if ask(Q.integer(answer*10000)) is True:
                break
        else:
            answer = prime.subs(x, a)
            task = r'Найдите значение производной заданной функции: \( y= ' + str(
            latex(substituted_eq)) + r"\) в точке \(x_0 = \{" + str(a) + "}\)"
            if ask(Q.integer(answer*10000)) is True:
                break
    answer_float = float(answer)
    return answer_float, task

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

prototype_42914 = "k*(x**p) + m*x + n"

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

prototype_42928 = "(-k)*cos(m*x) - (n/pi)*(x**2)"

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

