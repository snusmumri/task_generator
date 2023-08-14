import random
import fractions
import math
from sympy import *


'''Задача № 13274 c портала https://kuzovkin.info/one_exercise_1/13274
 Выписать производную в заданной точке (точках) x0:
f(x) = (1 + tg^2(2x))**3, x0 = π/8'''
def task_13274():
    answer = 1.234
    x = Symbol('x')
    while ask(Q.complex(answer)) is True:
        k = random.randint(1, 10)
        expr = (1 + (tan(2*x))**2)**3
        prime = expr.diff(x)
        result = simplify(prime)
        answer = result.subs(x, pi/k)
        task = r'Вычислите значение производной заданной функции: \( y= ' + str(
             latex(expr)) + r"\) в точке \(x_0 = \frac{\pi}{" + str(k) + "}\)"
        if ask(Q.integer(answer)) is True:
            break
    return answer, task

'''Задача № 3034 c портала https://kuzovkin.info/one_exercise_1/3034
 Найти критические точки функции: y = x**2 + 4x + 5'''
def task_3034():
    answer = 1.234
    x = Symbol('x')
    while ask(Q.complex(answer)) is True:
        k = random.randint(1, 10)
        m = random.randint(1, 10)
        n = random.randint(1, 10)
        expr = k*(x**2) + (m*x) + n
        prime = expr.diff(x)
        result = solveset(Eq(prime, 0), x)
        for i in result:
            if ask(Q.integer(i)) is True:
                answer = i
        task = r'Вычислите критические точки функции: \( y= ' + str(
             latex(expr)) + '\)'
        if ask(Q.integer(answer)) is True:
            break
    return answer, task

'''Задача № 42911 c портала https://kuzovkin.info/one_exercise_1/42911
 Найдите значение производной заданной функции в точке x0: y = sqrt(x), x0 = 4'''
def task_42911():
    answer = 1.234
    x = Symbol('x')
    while ask(Q.complex(answer)) is True:
        a = random.randint(1, 10)
        k = random.randint(1, 10)
        expr = k*(sqrt(x))
        prime = expr.diff(x)
        answer = prime.subs(x, a)
        task = r'Найдите значение производной заданной функции: \( y= '+str(
            latex(expr))+ r"\) в точке \(x_0 = \{" + str(a) +"}\)"
        if ask(Q.integer(answer)) is True:
            break
    return answer, task

'''Задача № 42912 c портала https://kuzovkin.info/one_exercise_1/42912
 Найдите значение производной заданной функции в точке x0: y = x**2, x0 = −7'''
def task_42912():
    answer = 1.234
    x = Symbol('x')
    while ask(Q.complex(answer)) is True:
        a = random.randint(1, 10)
        k = random.randint(1, 3)
        m = random.randint(1, 3)
        expr = m*(x**k)
        prime = expr.diff(x)
        answer = prime.subs(x, a)
        task = r'Найдите значение производной заданной функции: \( y= ' + str(
            latex(expr)) + r"\) в точке \(x_0 = \{" + str(a) + "}\)"
        if ask(Q.integer(answer)) is True:
            break
    return answer, task

'''Задача № 42913 c портала https://kuzovkin.info/one_exercise_1/42913
 Найдите значение производной заданной функции в точке x0: y = −3x − 11, x0 = −3'''
def task_42913():
    answer = 1.234
    x = Symbol('x')
    while ask(Q.complex(answer)) is True:
        a = random.randint(-10, -1)
        k = random.randint(-10, -1)
        m = random.randint(1, 10)
        expr = k*x - m
        prime = expr.diff(x)
        answer = prime.subs(x, a)
        task = r'Найдите значение производной заданной функции: \( y= ' + str(
            latex(expr)) + r"\) в точке \(x_0 = \{" + str(a) + "}\)"
        if ask(Q.integer(answer)) is True:
            break
    return answer, task

'''Задача № 42914 c портала https://kuzovkin.info/one_exercise_1/42914
 Найдите значение производной заданной функции в точке x0: y = 1/x, x0 = 0.5'''
def task_42914():
    answer = 1.234
    x = Symbol('x')
    while ask(Q.complex(answer)) is True:
        a = random.randint(1, 10)
        k = random.randint(1, 10)
        expr = k/x
        prime = expr.diff(x)
        answer = prime.subs(x, a)
        task = r'Найдите значение производной заданной функции: \( y= ' + str(
            latex(expr)) + r"\) в точке \(x_0 = \{" + str(a) + "}\)"
        if ask(Q.integer(answer)) is True:
            break
    return answer, task

'''Задача № 42916 c портала https://kuzovkin.info/one_exercise_1/42916
 Найдите значение производной заданной функции в точке x0: y = cosx, x0 = π/6'''
def task_42916():
    answer = 1.234
    x = Symbol('x')
    while ask(Q.complex(answer)) is True:
        a = random.randint(1, 10)
        k = random.randint(1, 10)
        m = random.randint(1, 10)
        expr = k*cos(m*x)
        prime = expr.diff(x)
        result = simplify(prime)
        answer = result.subs(x, pi/a)
        task = r'Вычислите значение производной заданной функции: \( y= ' + str(
            latex(expr)) + r"\) в точке \(x_0 = \frac{\pi}{" + str(a) + "}\)"
        if ask(Q.integer(answer)) is True:
            break
    return answer, task

task_1 = task_13274()
task_2 = task_3034()
task_3 = task_42911()
task_4 = task_42912()
task_5 = task_42913()
task_6 = task_42914()
task_7 = task_42915()
task_8 = task_42916()

stack_of_functions = [task_1, task_2, task_3, task_4, task_5, task_6, task_7, task_8]

def derivative_tasks_generator():
    answer = random.choice(stack_of_functions)
    return answer


if __name__ == "__main__":
    ...





