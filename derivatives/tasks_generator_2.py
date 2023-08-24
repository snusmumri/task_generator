import random
import fractions
import math
import numpy as np
from sympy import *


'''Задача № 13274 c портала https://kuzovkin.info/one_exercise_1/13274
 Выписать производную в заданной точке (точках) x0:
f(x) = (1 + tg^2(2x))**3, x0 = π/8'''
def task_13274():
    answer = 1.234
    x = Symbol('x')
    while ask(Q.complex(answer*1000)) is True:
        a = random.randint(1, 10)
        expr = (1 + (tan(2*x))**2)**3
        prime = expr.diff(x)
        result = simplify(prime)
        answer = result.subs(x, pi/a)
        task = r'Вычислите значение производной заданной функции: \( y= ' + str(
            latex(expr)) + r"\) в точке \(x_0 = " + str(latex(pi/a) + r"\)")
        if ask(Q.integer(answer*1000)) is True:
            break
    return answer, task

'''Задача № 3034 c портала https://kuzovkin.info/one_exercise_1/3034
 Найти критические точки функции: y = x**2 + 4x + 5'''
def task_3034():
    answer = 1.234
    x = Symbol('x')
    while ask(Q.complex(answer*1000)) is True:
        k, m, n = np.random.randint(1, 10, size=3)
        expr = k*(x**2) + (m*x) + n
        prime = expr.diff(x)
        result = solveset(Eq(prime, 0), x)
        for i in result:
            if ask(Q.integer(i)) is True:
                answer = i
        task = r'Вычислите критические точки функции: \( y= ' + str(
             latex(expr)) + '\)'
        if ask(Q.integer(answer*1000)) is True:
            break
    answer_float = float(answer)
    return answer_float, task

'''Задача № 42911 c портала https://kuzovkin.info/one_exercise_1/42911
 Найдите значение производной заданной функции в точке x0: y = sqrt(x), x0 = 4'''
def task_42911():
    answer = 1.234
    x = Symbol('x')
    while ask(Q.complex(answer*1000)) is True:
        a, k = np.random.randint(1, 10, size=2)
        expr = k*(sqrt(x))
        prime = expr.diff(x)
        answer = prime.subs(x, a)
        task = r'Найдите значение производной заданной функции: \( y= '+str(
            latex(expr))+ r"\) в точке \(x_0 = \{" + str(a) +"}\)"
        if ask(Q.integer(answer*1000)) is True:
            break
    answer_float = float(answer)
    return answer_float, task

'''Задача № 42912 c портала https://kuzovkin.info/one_exercise_1/42912
 Найдите значение производной заданной функции в точке x0: y = x**2, x0 = −7'''
def task_42912():
    answer = 1.234
    x = Symbol('x')
    while ask(Q.complex(answer*1000)) is True:
        a, m = np.random.randint(1, 10, size=2)
        k = random.randint(1, 3)
        expr = m*(x**k)
        prime = expr.diff(x)
        answer = prime.subs(x, a)
        task = r'Найдите значение производной заданной функции: \( y= ' + str(
            latex(expr)) + r"\) в точке \(x_0 = \{" + str(a) + "}\)"
        if ask(Q.integer(answer*1000)) is True:
            break
    answer_float = float(answer)
    return answer_float, task

'''Задача № 42913 c портала https://kuzovkin.info/one_exercise_1/42913
 Найдите значение производной заданной функции в точке x0: y = −3x − 11, x0 = −3'''
def task_42913():
    answer = 1.234
    x = Symbol('x')
    while ask(Q.complex(answer*1000)) is True:
        a, k, m = np.random.randint(1, 10, size=3)
        expr = -k*x - m
        prime = expr.diff(x)
        answer = prime.subs(x, -a)
        task = r'Найдите значение производной заданной функции: \( y= ' + str(
            latex(expr)) + r"\) в точке \(x_0 = \{" + str(-a) + "}\)"
        if ask(Q.integer(answer*1000)) is True:
            break
    answer_float = float(answer)
    return answer_float, task

'''Задача № 42914 c портала https://kuzovkin.info/one_exercise_1/42914
 Найдите значение производной заданной функции в точке x0: y = 1/x, x0 = 0.5'''
def task_42914():
    answer = 1.234
    x = Symbol('x')
    while ask(Q.complex(answer*1000)) is True:
        a, k = np.random.randint(1, 10, size=2)
        expr = k/x
        prime = expr.diff(x)
        answer = prime.subs(x, a)
        task = r'Найдите значение производной заданной функции: \( y= ' + str(
            latex(expr)) + r"\) в точке \(x_0 = \{" + str(a) + "}\)"
        if ask(Q.integer(answer*1000)) is True:
            break
    answer_float = float(answer)
    return answer_float, task

'''Задача № 42915 c портала https://kuzovkin.info/one_exercise_1/42915
 Найдите значение производной заданной функции в точке x0: y = sinx, x0 = −π/2'''
def task_42915():
    answer = 1.234
    x = Symbol('x')
    while ask(Q.complex(answer*1000)) is True:
        a, k, m = np.random.randint(1, 10, size=3)
        expr = k*sin(m*x)
        prime = expr.diff(x)
        result = simplify(prime)
        answer = result.subs(x, -pi/a)
        task = r'Вычислите значение производной заданной функции: \( y= ' + str(
            latex(expr)) + r"\) в точке \(x_0 = " + str(latex(-pi/a) + r"\)")
        if ask(Q.integer(answer*1000)) is True:
            break
    answer_float = float(answer)
    return answer_float, task

'''Задача № 42916 c портала https://kuzovkin.info/one_exercise_1/42916
 Найдите значение производной заданной функции в точке x0: y = cosx, x0 = π/6'''
def task_42916():
    answer = 1.234
    x = Symbol('x')
    while ask(Q.complex(answer*1000)) is True:
        a = random.randint(1, 100)
        k, m = np.random.randint(1, 10, size=2)
        expr = k*cos(m*x)
        prime = expr.diff(x)
        result = simplify(prime)
        answer = result.subs(x, pi/a)
        task = r'Вычислите значение производной заданной функции: \( y= ' + str(
            latex(expr)) + r"\) в точке \(x_0 = " + str(latex(pi/a) + r"\)")
        if ask(Q.integer(answer*1000)) is True:
            break
    answer_float = float(answer)
    return answer_float, task

'''Задача № 42918 c портала https://kuzovkin.info/one_exercise_1/42918
 Найдите значение производной заданной функции в точке x0: y = sinx, x0 = 0'''
def task_42918():
    answer = 1.234
    x = Symbol('x')
    while ask(Q.complex(answer*1000)) is True:
        a = random.randint(0, 100)
        k, m = np.random.randint(1, 10, size=2)
        expr = k*sin(m*x)
        prime = expr.diff(x)
        result = simplify(prime)
        answer = result.subs(x, a*pi)
        task = r'Вычислите значение производной заданной функции: \( y= ' + str(
            latex(expr)) + r"\) в точке \(x_0 = " + str(latex(a*pi) + r"\)")
        if ask(Q.integer(answer*1000)) is True:
            break
    answer_float = float(answer)
    return answer_float, task

'''Задача № 42919 c портала https://kuzovkin.info/one_exercise_1/42919
 Найдите значение производной заданной функции в точке x0: y = 6x − 9, x0 = 3'''
def task_42919():
    answer = 1.234
    x = Symbol('x')
    while ask(Q.complex(answer*1000)) is True:
        a, k, m = np.random.randint(1, 10, size=3)
        expr = k*x - m
        prime = expr.diff(x)
        answer = prime.subs(x, a)
        task = r'Найдите значение производной заданной функции: \( y= ' + str(
            latex(expr)) + r"\) в точке \(x_0 = \{" + str(a) + "}\)"
        if ask(Q.integer(answer*1000)) is True:
            break
    answer_float = float(answer)
    return answer_float, task

'''Задача № 42920 c портала https://kuzovkin.info/one_exercise_1/42920
 Найдите значение производной заданной функции в точке x0: y = x^3 − 3x + 2, x0 = 1'''
def task_42920():
    answer = 1.234
    x = Symbol('x')
    while ask(Q.complex(answer*1000)) is True:
        a, k, m, n = np.random.randint(1, 10, size=4)
        expr = k*(x**3) - (m*x) + n
        prime = expr.diff(x)
        answer = prime.subs(x, a)
        task = r'Найдите значение производной заданной функции: \( y= ' + str(
            latex(expr)) + r"\) в точке \(x_0 = \{" + str(a) + "}\)"
        if ask(Q.integer(answer*1000)) is True:
            break
    answer_float = float(answer)
    return answer_float, task

'''Задача № 42921 c портала https://kuzovkin.info/one_exercise_1/42921
 Найдите значение производной заданной функции в точке x0: y = 5x − 8, x0 = 2'''
def task_42921():
    answer = 1.234
    x = Symbol('x')
    while ask(Q.complex(answer*1000)) is True:
        a, k, m = np.random.randint(1, 10, size=3)
        expr = (k*x) - m
        prime = expr.diff(x)
        answer = prime.subs(x, a)
        task = r'Найдите значение производной заданной функции: \( y= ' + str(
            latex(expr)) + r"\) в точке \(x_0 = \{" + str(a) + "}\)"
        if ask(Q.integer(answer*1000)) is True:
            break
    answer_float = float(answer)
    return answer_float, task

'''Задача № 42922 c портала https://kuzovkin.info/one_exercise_1/42922
 Найдите значение производной заданной функции в точке x0: y = x^2 + 3x − 4, x0 = 1'''
def task_42922():
    answer = 1.234
    x = Symbol('x')
    while ask(Q.complex(answer*1000)) is True:
        a, k, m, n = np.random.randint(1, 10, size=4)
        expr = k*(x**2) + (m*x) - n
        prime = expr.diff(x)
        answer = prime.subs(x, a)
        task = r'Найдите значение производной заданной функции: \( y= ' + str(
            latex(expr)) + r"\) в точке \(x_0 = \{" + str(a) + "}\)"
        if ask(Q.integer(answer*1000)) is True:
            break
    answer_float = float(answer)
    return answer_float, task

'''Задача № 42923 c портала https://kuzovkin.info/one_exercise_1/42923
 Найдите значение производной заданной функции в точке x0: y = (2/x) − (x/2), x0 = 3'''
def task_42923():
    answer = 1.234
    x = Symbol('x')
    while ask(Q.complex(answer*1000)) is True:
        a, k, m = np.random.randint(1, 10, size=3)
        expr = k/x - x/m
        prime = expr.diff(x)
        answer = prime.subs(x, a)
        task = r'Найдите значение производной заданной функции: \( y= ' + str(
            latex(expr)) + r"\) в точке \(x_0 = \{" + str(a) + "}\)"
        if ask(Q.integer(answer*1000)) is True:
            break
    answer_float = float(answer)
    return answer_float, task

'''Задача № 42924 c портала https://kuzovkin.info/one_exercise_1/42924
 Найдите значение производной заданной функции в точке x0: y = sqrt(x) + 4, x0 = 9'''
def task_42924():
    answer = 1.234
    x = Symbol('x')
    while ask(Q.complex(answer*1000)) is True:
        a, k, m = np.random.randint(1, 10, size=3)
        expr = k*(sqrt(x)) + m
        prime = expr.diff(x)
        answer = prime.subs(x, a)
        task = r'Найдите значение производной заданной функции: \( y= '+str(
            latex(expr))+ r"\) в точке \(x_0 = \{" + str(a) +"}\)"
        if ask(Q.integer(answer*1000)) is True:
            break
    answer_float = float(answer)
    return answer_float, task

'''Задача № 42925 c портала https://kuzovkin.info/one_exercise_1/42925
 Найдите значение производной заданной функции в точке x0: y = (8/x) − ((x^3)/3), x0 = 1'''
def task_42925():
    answer = 1.234
    x = Symbol('x')
    while ask(Q.complex(answer*1000)) is True:
        a, k, m = np.random.randint(1, 10, size=3)
        expr = k/x - (x**3)/m
        prime = expr.diff(x)
        answer = prime.subs(x, a)
        task = r'Найдите значение производной заданной функции: \( y= ' + str(
            latex(expr)) + r"\) в точке \(x_0 = \{" + str(a) + "}\)"
        if ask(Q.integer(answer*1000)) is True:
            break
    answer_float = float(answer)
    return answer_float, task

'''Задача № 42926 c портала https://kuzovkin.info/one_exercise_1/42926
 Найдите значение производной заданной функции в точке x0: y = sqrt(x) + 5x, x0 = 4'''
def task_42926():
    answer = 1.234
    x = Symbol('x')
    while ask(Q.complex(answer*1000)) is True:
        a, k, m = np.random.randint(1, 10, size=3)
        expr = k*(sqrt(x)) + m*x
        prime = expr.diff(x)
        answer = prime.subs(x, a)
        task = r'Найдите значение производной заданной функции: \( y= '+str(
            latex(expr))+ r"\) в точке \(x_0 = \{" + str(a) +"}\)"
        if ask(Q.integer(answer*1000)) is True:
            break
    answer_float = float(answer)
    return answer_float, task

'''Задача № 42927 c портала https://kuzovkin.info/one_exercise_1/42927
 Найдите значение производной заданной функции в точке x0: y = 2sinx − 13cosx, x0 = π/2'''
def task_42927():
    answer = 1.234
    x = Symbol('x')
    while ask(Q.complex(answer*1000)) is True:
        a = random.randint(1, 100)
        k, m, n, v = np.random.randint(1, 10, size=4)
        expr = k*sin(m*x) - n*cos(v*x)
        prime = expr.diff(x)
        result = simplify(prime)
        answer = result.subs(x, pi/a)
        task = r'Вычислите значение производной заданной функции: \( y= ' + str(
            latex(expr)) + r"\) в точке \(x_0 = " + str(latex(pi/a) + r"\)")
        if ask(Q.integer(answer*1000)) is True:
            break
    answer_float = float(answer)
    return answer_float, task

'''Задача № 42928 c портала https://kuzovkin.info/one_exercise_1/42928
 Найдите значение производной заданной функции в точке x0: y = −cosx + (1/π)*(x**2), x0 = π/6'''
def task_42928():
    answer = 1.234
    x = Symbol('x')
    while ask(Q.complex(answer*1000)) is True:
        a = random.randint(1, 100)
        k, m, n = np.random.randint(1, 10, size=3)
        expr = (-k)*cos(m*x) - (n/pi)*(x**2)
        prime = expr.diff(x)
        result = simplify(prime)
        answer = result.subs(x, pi/a)
        task = r'Вычислите значение производной заданной функции: \( y= ' + str(
            latex(expr)) + r"\) в точке \(x_0 = " + str(latex(pi/a) + r"\)")
        if ask(Q.integer(answer*1000)) is True:
            break
    answer_float = float(answer)
    return answer_float, task

'''Задача № 42929 c портала https://kuzovkin.info/one_exercise_1/42929
 Найдите значение производной заданной функции в точке x0: y = −sinx − 3, x0 = π/3'''
def task_42929():
    answer = 1.234
    x = Symbol('x')
    while ask(Q.complex(answer*1000)) is True:
        a = random.randint(1, 100)
        k, m, n = np.random.randint(1, 10, size=3)
        expr = (-k)*sin(m*x) - n
        prime = expr.diff(x)
        result = simplify(prime)
        answer = result.subs(x, pi/a)
        task = r'Вычислите значение производной заданной функции: \( y= ' + str(
            latex(expr)) + r"\) в точке \(x_0 = " + str(latex(pi/a) + r"\)")
        if ask(Q.integer(answer*1000)) is True:
            break
    answer_float = float(answer)
    return answer_float, task

'''Задача № 42930 c портала https://kuzovkin.info/one_exercise_1/42930
 Найдите значение производной заданной функции в точке x0: y = 4cosx + xsqrt(2), x0 = π/4'''
def task_42930():
    answer = 1.234
    x = Symbol('x')
    while ask(Q.complex(answer*1000)) is True:
        a, k, m, n = np.random.randint(1, 10, size=4)
        expr = k*cos(m*x) + sqrt(n)*x
        prime = expr.diff(x)
        result = simplify(prime)
        answer = result.subs(x, pi/a)
        task = r'Вычислите значение производной заданной функции: \( y= ' + str(
            latex(expr)) + r"\) в точке \(x_0 = " + str(latex(pi/a) + r"\)")
        if ask(Q.integer(answer*1000)) is True:
            break
    answer_float = float(answer)
    return answer_float, task

'''Задача № 42931 c портала https://kuzovkin.info/one_exercise_1/42931
 Найдите значение производной заданной функции в точке x0: y = tgx + x*sqrt(π)*sqrt(x), x0 = π/4'''
def task_42931():
    answer = 1.234
    x = Symbol('x')
    while ask(Q.complex(answer*1000)) is True:
        a, k = np.random.randint(1, 10, size=2)
        expr = k*(tan(x)) + x*(sqrt(pi))*(sqrt(x))
        prime = expr.diff(x)
        result = simplify(prime)
        answer = result.subs(x, pi/a)
        task = r'Вычислите значение производной заданной функции: \( y= ' + str(
            latex(expr)) + r"\) в точке \(x_0 = " + str(latex(pi/a) + r"\)")
        if ask(Q.integer(answer*1000)) is True:
            break
    return answer, task

'''Задача № 42932 c портала https://kuzovkin.info/one_exercise_1/42932
 Найдите значение производной заданной функции в точке x0: y = 2ctgx − 3tgx, x0 = π/3'''
def task_42932():
    answer = 1.234
    x = Symbol('x')
    while ask(Q.complex(answer*1000)) is True:
        a, k, m, n, v = np.random.randint(1, 10, size=5)
        expr = k*(cot(m*x)) - n*(tan(v*x))
        prime = expr.diff(x)
        result = simplify(prime)
        answer = result.subs(x, pi/a)
        task = r'Вычислите значение производной заданной функции: \( y= ' + str(
            latex(expr)) + r"\) в точке \(x_0 = " + str(latex(pi/a) + r"\)")
        if ask(Q.integer(answer*1000)) is True:
            break
    return answer, task

'''Задача № 42934 c портала https://kuzovkin.info/one_exercise_1/42934
 Найдите значение производной заданной функции в точке x0: y = (2x + 3)^2 − 4tgx, x0 = 0'''
def task_42934():
    answer = 1.234
    x = Symbol('x')
    while ask(Q.complex(answer*1000)) is True:
        a, k, m, n, v = np.random.randint(1, 10, size=5)
        expr = (k*x + m)**2 - n*(tan(v*x))
        prime = expr.diff(x)
        result = simplify(prime)
        answer = result.subs(x, pi/a)
        task = r'Вычислите значение производной заданной функции: \( y= ' + str(
            latex(expr)) + r"\) в точке \(x_0 = " + str(latex(pi/a) + r"\)")
        if ask(Q.integer(answer*1000)) is True:
            break
    return answer, task

'''Задача № 42936 c портала https://kuzovkin.info/one_exercise_1/42936
 Найдите значение производной заданной функции в точке x0: y = (x+1)/(x−1), x0 = 2'''
def task_42936():
    answer = 1.234
    x = Symbol('x')
    while ask(Q.complex(answer*1000)) is True:
        a, k, m, n, v = np.random.randint(1, 10, size=5)
        expr = (k*x + m)/(n*x + v)
        prime = expr.diff(x)
        result = simplify(prime)
        answer = result.subs(x, a)
        task = r'Найдите значение производной заданной функции: \( y= ' + str(
            latex(expr)) + r"\) в точке \(x_0 = \{" + str(a) + "}\)"
        if ask(Q.integer(answer*1000)) is True:
            break
    answer_float = float(answer)
    return answer_float, task

