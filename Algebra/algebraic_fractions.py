from Tools.scripts.dutree import display
from sympy import *
import numpy as np
import fractions
from fractions import Fraction
import random
import math
import decimal


def task_1554():
    """Задача №1554 с портала https://kuzovkin.info/one_exercise_1/1554"""
    while True:
        a, b = np.random.randint(2, 20, size=2)
        m, n = np.random.randint(2, 5, size=2)
        if m != n and a > b:
            x, y = symbols('x y')
            task = r'Найдите значение алгебраической дроби: \( \frac{'+latex(pow(UnevaluatedExpr(x), m))+('+')+latex(pow(y, m))+'}{'+latex(pow(UnevaluatedExpr(x), n))+('-')+latex(pow(y, n))+'} \) при \(' +latex(x)+str('=')+latex(UnevaluatedExpr(a))+str(',')+latex(y)+str('=')+latex(UnevaluatedExpr(b))+ '\)'
            answer = (a ** m + b ** m) / (a ** n - b ** n)
            if len(str(answer % 1)) < 6:
                if answer % 1 == 0:
                    answer = int(answer)
                break
    return {
      "condition": task,
      "answer": answer
    }


def task_1555():
    """Задача №1555 с портала https://kuzovkin.info/one_exercise_1/1555"""
    while True:
        a, b = np.random.randint(-10, 10, size=2)
        if a > b and a * b != 0 and abs(a) != abs(b):
            m, n = symbols("m n")
            task = (
                r"Найдите значение алгебраической дроби: \( \frac{" + latex(pow(m, 4)) + r"-" + latex(pow(n, 4)) + "}{"
                + latex(pow(m, 3) * n) + r"-" + latex(m * pow(n, 3)) + r"} \) при \(" + latex(m) + str("=")
                + latex(UnevaluatedExpr(a)) + str(",") + latex(n) + str("=") + latex(UnevaluatedExpr(b)) + r"\)"
            )
            answer = (a ** 4 - b ** 4) / (a ** 3 * b - a * b ** 3)
            if len(str(answer % 1)) < 6:
                if answer % 1 == 0:
                    answer = int(answer)
                break
    return {
        "condition": task,
        "answer": answer
    }


def task_1581():
    """Задача №1581 с портала https://kuzovkin.info/one_exercise_1/1581"""
    while True:
        k = np.random.randint(2, 10)
        a, b = symbols("a b")
        task = (
            r"Зная, что \( \frac{" + latex(a) + "}{" + latex(b) + "} {" + str("=") + latex(UnevaluatedExpr(k))
            + "} \), найдите значение выражения: \( \\frac{" + latex(b) + "}{" + latex(a) + "} \)"
        )
        answer = (
            r"\( \frac{" + latex(UnevaluatedExpr(1)) + "}{" + latex(UnevaluatedExpr(k)) + "}" + "\)"
        )
        if k:
            break
    return {
        "condition": task,
        "answer": answer
    }


def task_1583():
    """Задача №1583 с портала https://kuzovkin.info/one_exercise_1/1583 и аналогичная 1"""
    while True:
        k = np.random.randint(2, 10)
        a, b = symbols('a b')
        task = r'Зная, что \( \frac{'+latex(a)+'}{'+latex(b)+'} {'+str('=')+latex(UnevaluatedExpr(k))+'} \), найдите значение выражения: \( \\frac{'+latex(b+UnevaluatedExpr(2*a))+'}{'+latex(a)+'} \)'
        whole_path = 2
        answer = r'\( {'+latex(UnevaluatedExpr(whole_path))+'} \\frac{'+latex(UnevaluatedExpr(1))+'}{'+latex(UnevaluatedExpr(k))+'} \)'
        if k:
            break
    return {
      "condition": task,
      "answer": answer
    }


def task_1584():
    """Задача №1584 с портала https://kuzovkin.info/one_exercise_1/1584"""
    while True:
        a, b = np.random.randint(2, 10, size=2)
        if a < b and a % b != 0:
            x, y = symbols("x y")
            task = (
                r"Зная, что \( \frac{" + latex(x) + "}{" + latex(y) + "} {" + str("=") + "} \\frac{"
                + latex(UnevaluatedExpr(a)) + "}{" + latex(UnevaluatedExpr(b))
                + "} \), найдите значение выражения: \( \\frac{" + latex(x) + "}{" + latex(2 * y) + "} \)"
            )
            result = fractions.Fraction(a, 2 * b)
            fraction = Fraction(result).limit_denominator()
            break
    answer = (
        r"\(\frac{" + f"{fraction.numerator}" + r"}{" + f"{fraction.denominator}" + r"}\)"
    )
    return {
        "condition": task,
        "answer": answer
    }


def task_1588():
    """Задача №1588 с портала https://kuzovkin.info/one_exercise_1/1588"""
    while True:
        k = np.random.randint(1, 26)/10
        if pow(k, -1) == int(pow(k, -1)):
            x, y = symbols('x y')
            task = r'Надйите значение дроби \( \frac{'+latex(x+y)+'}{'+latex(x)+'} \), если \( \\frac{'+latex(x)+'}{'+latex(y)+'}{'+str('=')+'}{'+latex(UnevaluatedExpr(k))+'} \)'
            answer = int(1+pow(k, -1))
            break
    return {
      "condition": task,
      "answer": answer
    }


def task_1591():
    """Задача №1591 с портала https://kuzovkin.info/one_exercise_1/1591"""
    while True:
        k = np.random.randint(2, 20)
        a, b = symbols('a b')
        task = r'Зная, что \( \frac{'+latex(a+UnevaluatedExpr(2*b))+'}{'+latex(b)+'} {'+str('=')+'} {'+latex(UnevaluatedExpr(k))+'} \), найдите значение выражения: \( \\frac{'+latex(2*a-b)+'}{'+latex(2*b)+'} \)'
        answer = k-2.5
        if k:
            break
    return {
      "condition": task,
      "answer": answer
    }


def task_1596():
    """Задача №1596 с портала https://kuzovkin.info/one_exercise_1/1596"""
    while True:
        k = np.random.randint(2, 20)
        x, y = symbols('x y')
        task = r'Зная, что \( \frac{'+latex(x-UnevaluatedExpr(3*y))+'}{'+latex(y)+'} {'+str('=')+'} {'+latex(UnevaluatedExpr(k))+'} \), найдите значение выражения: \( \\frac{'+latex(y)+'}{'+latex(x)+'} \)'
        result = fractions.Fraction(1, k+3)
        fraction = Fraction(result).limit_denominator()
        if k:
            break
    answer = (
            r"\(\frac{"
            + f"{fraction.numerator}"
            + r"}{"
            + f"{fraction.denominator}"
            + r"}\)"
    )
    return {
      "condition": task,
      "answer": answer
    }


def task_1785():
    """Задача №1785 с портала https://kuzovkin.info/one_exercise_1/1785"""
    while True:
        a, b, c, d = np.random.randint(1, 10, size=4)
        k = np.random.randint(2, 40)/10
        if k % 1 == 0:
            k = int(k)
        x = symbols('x')
        task = r'Упростите выражение и найдите его значение: \( \frac{'+latex(UnevaluatedExpr(c))+('+')+latex(UnevaluatedExpr(a*x))+'}{'+latex((UnevaluatedExpr(a)+x)*(UnevaluatedExpr(b)-UnevaluatedExpr(x)))+'} {'+str('+')+'} \\frac{'+latex(UnevaluatedExpr(d)+x)+'}{'+latex((x+UnevaluatedExpr(a))*(x-UnevaluatedExpr(b)))+'}\) при \(' +latex(UnevaluatedExpr(x))+str('=')+latex(UnevaluatedExpr(k))+ '\)'
        if a != b and b != k and (c-d)/(a-1) == a > 1:
            answer = (c-d)/(a-1)/a/(b-k)
            if len(str(answer % 1)) < 6:
                if answer % 1 == 0:
                    answer = int(answer)
                break
    return {
      "condition": task,
      "answer": answer
    }


def task_1883():
    """Задача №1883 с портала https://kuzovkin.info/one_exercise_1/1883"""
    while True:
        a, b, m, n, f, h = np.random.randint(2, 10, size=6)
        c = symbols('c')
        check = b*h-a*f
        task = r'Упростите выражение: \( \frac{'+latex(c)+('-')+latex(UnevaluatedExpr(b))+'}{'+latex(UnevaluatedExpr(b*m*c))+('+')+latex(UnevaluatedExpr(b*n))+'} {'+str('-')+'} \\frac{'+latex(UnevaluatedExpr(c))+('-')+latex(UnevaluatedExpr(h))+'}{'+latex(UnevaluatedExpr(a*m*c))+('+')+latex(UnevaluatedExpr(a*n))+'} \)'
        answer = 1/(a*b)
        if check == n:
            if len(str(answer % 1)) < 6:
                if answer % 1 == 0:
                    answer = int(answer)
                break
    return {
      "condition": task,
      "answer": answer
    }


def task_1947():
    """Задача №1947 с портала https://kuzovkin.info/one_exercise_1/1947"""
    while True:
        a, b, n, k = np.random.randint(1, 25, size=4)
        if k % b == 0 and a % n == 0:
            c, d = symbols('c d')
            task = r'Упростите выражение: \( \frac{'+latex(UnevaluatedExpr(b*c))+'}{'+latex(UnevaluatedExpr(a*d))+'} {'+str(':')+'} ( {'+str('-')+'} \\frac{'+latex(UnevaluatedExpr(k*c))+'}{'+latex(UnevaluatedExpr(n*d))+'}) \)'
            answer = int(-(b*n)*(k*a))
            if len(str(answer % 1)) < 6 and -1000 <= answer <= 1000:
                if answer % 1 == 0:
                    answer = int(answer)
                break
    return {
      "condition": task,
      "answer": answer
    }


def task_1967():
    """Задача №1967 с портала https://kuzovkin.info/one_exercise_1/1967"""
    while True:
        a, b, n, k = np.random.randint(8, 100, size=4)
        if n % k == 0 and n != k and a != b:
            c, r, s = symbols('c r s')
            task = r'Упростите выражение: \( \frac{'+latex(UnevaluatedExpr(a*r))+('-')+latex(UnevaluatedExpr(b*s))+'}{'+latex(UnevaluatedExpr(k*c))+'} {'+str('\cdot')+'} \\frac{'+latex(UnevaluatedExpr(n*c))+'}{'+latex(UnevaluatedExpr(b*s))+('-')+latex(UnevaluatedExpr(a*r))+'} \)'
            answer = float(-(n/k))
            if len(str(answer % 1)) < 6:
                if answer % 1 == 0:
                    answer = int(answer)
                break
    return {
      "condition": task,
      "answer": answer
    }


def task_5492():
    """Задача №5492 с портала https://kuzovkin.info/one_exercise_1/5492"""
    while True:
        m, n, k, c = np.random.randint(1, 10, size=4)
        f = np.random.randint(1, 7)/10
        a, b = symbols('a b')
        task = r'Найдите значение дроби: \( \frac{'+latex(UnevaluatedExpr(k*c*a))+('+')+latex(UnevaluatedExpr(k*n*b))+'}{'+latex(UnevaluatedExpr(f*pow(c, 2))*UnevaluatedExpr(pow(a, 2)))+('-')+latex(UnevaluatedExpr(f*pow(n, 2))*UnevaluatedExpr(pow(b, 2)))+'} \), если \(' +latex(a-2*b)+str('=')+latex(UnevaluatedExpr(m))+str(',')+latex(a+2*b)+str('\u2260')+latex(UnevaluatedExpr(0))+ '\)'
        answer = float(k/(f*m))
        check = k % f
        if c != n and f*pow(c, 2) != int(f*pow(c, 2)) and f*pow(n, 2) != int(f*pow(n, 2)):
            if check == int(check) and answer != 0 and len(str(answer).split('.')[1]) <= 6:
                if answer % 1 == 0:
                    answer = int(answer)
                break
    return {
      "condition": task,
      "answer": answer
    }


def task_5493():
    """Задача №5493 с портала https://kuzovkin.info/one_exercise_1/5493"""
    while True:
        a, b, m, n = np.random.randint(1, 10, size=4)
        if a != b and m != n:
            c = np.random.randint(1, 10)/10
            d = np.random.randint(1, 100)/100
            x, y = symbols('x y')
            task = r'Найдите значение дроби: \( \frac{'+latex(UnevaluatedExpr(a*m*pow(x, 2)))+('-')+latex(UnevaluatedExpr(a*n*x*y))+'}{'+latex(UnevaluatedExpr(b*m*x*y))+('-')+latex(UnevaluatedExpr(b*n*pow(y, 2)))+'} \) при \(' +latex(x)+str('=')+latex(UnevaluatedExpr(c))+str(',')+latex(y)+str('=')+latex(UnevaluatedExpr(d))+ '\)'
            answer = float((a*c)/(b*d))
            if len(str(answer).split('.')[1]) <= 6:
                if answer % 1 == 0:
                    answer = int(answer)
                break
    return {
      "condition": task,
      "answer": answer
    }


def task_5494():
    """Задача №5494 с портала https://kuzovkin.info/one_exercise_1/5494"""
    while True:
        m, n, k, f = np.random.randint(1, 7, size=4)
        x = -np.random.randint(11, 30)/10
        y = np.random.randint(1, 10)/10
        a, b = symbols('a b')
        task = r'Найдите значение дроби: \( \frac{'+latex(UnevaluatedExpr(f*pow(m, 2))*UnevaluatedExpr(pow(a, 3)))+('-')+latex(UnevaluatedExpr(f*pow(n, 2)*a*pow(b, 2)))+'}{'+latex(UnevaluatedExpr(k*n*pow(b, 2)))+('-')+latex(UnevaluatedExpr(k*m*a*b))+'} \), при \(' +latex(a)+str('=')+latex(UnevaluatedExpr(x))+str(',')+latex(b)+str('=')+latex(UnevaluatedExpr(y))+ '\)'
        answer = float(-(x*f*(m*x+n*y))/(k*y))
        if m != n and k != f and len(str(answer).split('.')[1]) <= 6:
            if answer % 1 == 0:
                answer = int(answer)
            break
    return {
      "condition": task,
      "answer": answer
    }


def task_5475():
    """Задача №5475 с портала https://kuzovkin.info/one_exercise_1/5475"""
    while True:
        a, b, c, m, n, k = np.random.randint(2, 10, size=6)
        if a != b != k and m != n != k:
            x, y = symbols('x y')
            task = r'Пусть \( \frac{'+latex(x)+'}{'+latex(y)+'}{'+str('=')+'}{'+latex(UnevaluatedExpr(k))+'} \). Найдите значение дроби: \( \\frac{'+latex(UnevaluatedExpr(a)*UnevaluatedExpr(pow(x, 2)))+('-')+latex(UnevaluatedExpr(b)*UnevaluatedExpr(x*y))+('+')+latex(UnevaluatedExpr(c)*UnevaluatedExpr(pow(y, 2)))+'}{'+latex(UnevaluatedExpr(m)*UnevaluatedExpr(pow(x, 2)))+('+')+latex(UnevaluatedExpr(n)*UnevaluatedExpr(pow(y, 2)))+'} \)'
            num = a*pow(k, 2)-b*k+c
            den = m*pow(k, 2)+n
            answer = num/den
            if answer % 1 == 0 and answer != 0:
                if answer % 1 == 0:
                    answer = int(answer)
                break
    return {
      "condition": task,
      "answer": answer
    }


def task_5459():
    """Задача №5459 с портала https://kuzovkin.info/one_exercise_1/5459"""
    while True:
        k, n, m = np.random.randint(1, 15, size=3)
        if k < n and m != 1 and n % k != 0:
            x, y = symbols('x y')
            task = r'Зная, что \( \frac{'+latex(x)+'}{'+latex(y)+'} {'+str('=')+'} \\frac{'+latex(UnevaluatedExpr(k))+'}{'+latex(UnevaluatedExpr(n))+'} \), найдите значение выражения: \( \\frac{'+latex(y)+'}{'+latex(UnevaluatedExpr(m)*UnevaluatedExpr(x))+'} \)'
            answer = float(n/(m*k))
            if len(str(answer).split('.')[1]) <= 6:
                if answer % 1 == 0:
                    answer = int(answer)
                break
    return {
      "condition": task,
      "answer": answer
    }


def task_5460():
    """Задача №5460 с портала https://kuzovkin.info/one_exercise_1/5460"""
    while True:
        k, n = np.random.randint(1, 15, size=2)
        if k < n:
            x, y = symbols('x y')
            task = r'Зная, что \( \frac{'+latex(x)+'}{'+latex(y)+'} {'+str('=')+'} \\frac{'+latex(UnevaluatedExpr(k))+'}{'+latex(UnevaluatedExpr(n))+'} \), найдите значение выражения: \( \\frac{'+latex(x-y)+'}{'+latex(y)+'} \)'
            answer = float(k/n-1)
            if len(str(answer).split('.')[1]) <= 6:
                if answer % 1 == 0:
                    answer = int(answer)
                break
    return {
      "condition": task,
      "answer": answer
    }


def task_5462():
    """Задача №5462 с портала https://kuzovkin.info/one_exercise_1/5462"""
    while True:
        a, b = np.random.randint(2, 10, size=2)
        if a != b:
            k = np.random.randint(1, 10)/10
            x, y = symbols('x y')
            task = r'Найдите значение дроби: \( \frac{'+latex(UnevaluatedExpr(a)*UnevaluatedExpr(x))+('-')+latex(UnevaluatedExpr(b)*UnevaluatedExpr(y))+'}{'+latex(y)+'}\), если \( \\frac{'+latex(x)+'}{'+latex(y)+'}{'+str('=')+'}{'+latex(UnevaluatedExpr(k))+'} \)'
            answer = float(a*k-b)
            if len(str(answer).split('.')[1]) <= 6:
                if answer % 1 == 0:
                    answer = int(answer)
                break
    return {
      "condition": task,
      "answer": answer
    }


def task_5465():
    """Задача №5465 с портала https://kuzovkin.info/one_exercise_1/5465"""
    while True:
        k, m, c, d = np.random.randint(2, 10, size=4)
        if k != m and c != d:
            a, b = symbols('a b')
            task = r'Зная, что \( \frac{'+latex(a)+('+')+latex(UnevaluatedExpr(m*b))+'}{'+latex(b)+'} {'+str('=')+'} {'+latex(UnevaluatedExpr(k))+'} \), найдите значение выражения: \( \\frac{'+latex(UnevaluatedExpr(c*a))+('+')+latex(UnevaluatedExpr(d*b))+'}{'+latex(b)+'} \)'
            answer = float(c*(k-m)+d)
            if answer != 0 and len(str(answer).split('.')[1]) <= 6:
                if answer % 1 == 0:
                    answer = int(answer)
                break
    return {
      "condition": task,
      "answer": answer
    }


def task_5449():
    """Задача №5449 с портала https://kuzovkin.info/one_exercise_1/5449"""
    while True:
        a, b, m, k = np.random.randint(1, 10, size=4)
        if m % k == 0 and a != b and k != m:
            x, y = symbols('x y')
            task = r'Зная, что \( \{'+latex(UnevaluatedExpr(k*a*x))+('-')+latex(UnevaluatedExpr(k*b*y))+'} {'+str('=')+'} {'+latex(UnevaluatedExpr(m))+'} \), найдите значение выражения: \( \{'+latex(UnevaluatedExpr(a*x))+('-')+latex(UnevaluatedExpr(b*y))+'} \)'
            answer = float(m/k)
            if len(str(answer).split('.')[1]) <= 6:
                if answer % 1 == 0:
                    answer = int(answer)
                break
    return {
      "condition": task,
      "answer": answer
    }


def task_5450():
    """Задача №5450 с портала https://kuzovkin.info/one_exercise_1/5450 и аналогичная 5451"""
    while True:
        a, b, m, k, f = np.random.randint(1, 10, size=5)
        if a != b and k != m:
            x, y = symbols('x y')
            task = r'Зная, что \( {'+latex(UnevaluatedExpr(k*a*x))+('-')+latex(UnevaluatedExpr(k*b*y))+'} {'+str('=')+'} {'+latex(UnevaluatedExpr(m))+'} \), найдите значение выражения: \( \\frac{'+latex(UnevaluatedExpr(f))+'}{'+latex(UnevaluatedExpr(a*x))+('-')+latex(UnevaluatedExpr(b*y))+'} \)'
            answer = float((f*k)/m)
            if len(str(answer).split('.')[1]) <= 6:
                if answer % 1 == 0:
                    answer = int(answer)
                break
    return {
      "condition": task,
      "answer": answer
    }


def task_5452():
    """Задача №5452 с портала https://kuzovkin.info/one_exercise_1/5452"""
    while True:
        a, b, m, k, f = np.random.randint(1, 8, size=5)
        if m % k == 0 and a != b and k != m:
            x, y = symbols('x y')
            task = r'Зная, что \( {'+latex(UnevaluatedExpr(k*a*x))+('-')+latex(UnevaluatedExpr(k*b*y))+'} {'+str('=')+'} {'+latex(UnevaluatedExpr(m))+'} \), найдите значение выражения: \( ({'+latex(UnevaluatedExpr(pow(b, 2)*pow(y, 2)))+('-')+latex(UnevaluatedExpr(2*a*b*x*y))+('+')+latex(UnevaluatedExpr(pow(a, 2)*pow(b, 2)))+'}){'+str('\cdot')+'}{'+latex(UnevaluatedExpr(f))+'} \)'
            answer = float(pow(m/k, 2)*f)
            if len(str(answer).split('.')[1]) <= 6:
                if answer % 1 == 0:
                    answer = int(answer)
                break
    return {
      "condition": task,
      "answer": answer
    }


def task_5496():
    """Задача №5496 с портала https://kuzovkin.info/one_exercise_1/5496"""
    while True:
        a, b, c, d, m, n = np.random.randint(2, 10, size=6)
        if a != b and m % c == 0 and n % d == 0:
            k, l = symbols('k l')
            task = r'Найдите значение дроби: \( \frac{'+latex(UnevaluatedExpr(m*a)*UnevaluatedExpr(k*l))+('-')+latex(UnevaluatedExpr(m*b)*UnevaluatedExpr(pow(k, 2)))+'}{'+latex(UnevaluatedExpr(n*b)*UnevaluatedExpr(k*l))+('-')+latex(UnevaluatedExpr(n*a)*UnevaluatedExpr(pow(l, 2)))+'}\), при \( {'+latex(k)+'}{'+str('=')+'}\\frac{'+latex(UnevaluatedExpr(1))+'}{'+latex(UnevaluatedExpr(c))+'}{'+str(';')+'}{'+latex(l)+'}{'+str('=')+'}\\frac{'+latex(UnevaluatedExpr(1))+'}{'+latex(UnevaluatedExpr(d))+'} \)'
            answer = float(-(m*d)/(c*n))
            if len(str(answer).split('.')[1]) <= 6:
                if answer % 1 == 0:
                    answer = int(answer)
                break
    return {
      "condition": task,
      "answer": answer
    }


def task_5838():
    """Задача №5838 с портала https://kuzovkin.info/one_exercise_1/5838"""
    while True:
        a, b, k = np.random.randint(2, 10, size=3)
        if k < b:
            m, n, c = symbols('m n c')
            task = r'Упростите выражение: \( \frac{'+latex(UnevaluatedExpr(a*m))+('-')+latex(n)+'}{'+latex(UnevaluatedExpr(b*c))+'} {'+str('\cdot')+'} \\frac{'+latex(UnevaluatedExpr(k*c))+'}{'+latex(n)+('-')+latex(UnevaluatedExpr(a*m))+'} \)'
            answer = r'\( -\frac{'+latex(UnevaluatedExpr(k))+'}{'+latex(UnevaluatedExpr(b))+'} \)'
            break
    return {
      "condition": task,
      "answer": answer
    }


def task_5853():
    """Задача №5853 с портала https://kuzovkin.info/one_exercise_1/5853"""
    while True:
        a, b, k = np.random.randint(2, 10, size=3)
        if a != b:
            x, y, p = symbols('x y p')
            task = r'Упростите выражение: \( \frac{'+latex(UnevaluatedExpr(a*p))+('-')+latex(pow(p, 2))+'}{'+latex(y)+('-')+latex(x)+'} {'+str(':')+'} \\frac{'+latex(UnevaluatedExpr(a*k*p))+('-')+latex(UnevaluatedExpr(b*k*pow(p, 2)))+'}{'+latex(x-y)+'} \)'
            answer = float(-1/k)
            if len(str(answer).split('.')[1]) <= 6:
                if answer % 1 == 0:
                    answer = int(answer)
                break
    return {
      "condition": task,
      "answer": answer
    }


def task_5854():
    """Задача №5854 с портала https://kuzovkin.info/one_exercise_1/5854"""
    while True:
        x, y, k = np.random.randint(2, 10, size=3)
        if x != y:
            a, b, q = symbols('a b q')
            task = r'Упростите выражение: \( \frac{'+latex(a)+('-')+latex(b)+'}{'+latex(UnevaluatedExpr(x*q))+('-')+latex(pow(q, 2))+'} {'+str('\cdot')+'} \\frac{'+latex(UnevaluatedExpr(k*x*q))+('-')+latex(UnevaluatedExpr(k*y*pow(q, 2)))+'}{'+latex(b)+('-')+latex(a)+'} \)'
            answer = float(-k)
            if len(str(answer).split('.')[1]) <= 6:
                if answer % 1 == 0:
                    answer = int(answer)
                break
    return {
      "condition": task,
      "answer": answer
    }


def task_11915():
    """Задача №11915 с портала https://kuzovkin.info/one_exercise_1/11915"""
    while True:
        a, b, k = np.random.randint(1, 10, size=3)
        if k != a != b:
            p = symbols('p')
            task = r'Выполните сложение алгебраических дробей: \( \frac{'+latex(UnevaluatedExpr(k*a))+'}{'+latex(UnevaluatedExpr(a))+('+')+latex(UnevaluatedExpr(b*p))+'} {'+str('+')+'} \\frac{'+latex(UnevaluatedExpr(k*b*p))+'}{'+latex(UnevaluatedExpr(a))+('+')+latex(UnevaluatedExpr(b*p))+'} \)'
            answer = float(k)
            if len(str(answer).split('.')[1]) <= 6:
                if answer % 1 == 0:
                    answer = int(answer)
                break
    return {
        "condition": task,
        "answer": answer
    }


def task_11947():
    """Задача №11947 с портала https://kuzovkin.info/one_exercise_1/11947"""
    while True:
        a, x, y = np.random.randint(1, 10, size=3)
        m_ = np.random.randint(-50, 50)/10
        if a != x != y and m_ != int(m_) and m_ != 0 and pow(x, 2)+y == pow(a, 2) and 2*x-1 == a:
            m = symbols('m')
            task = r'Упростите и найдите значение выражения: \( \frac{'+latex(UnevaluatedExpr(pow(m-x, 2)))+'}{'+latex(pow(m, 3))+('+')+latex(UnevaluatedExpr(pow(a, 3)))+'} {'+str('+')+'} \\frac{'+latex(UnevaluatedExpr(y))+('-')+latex(m)+'}{'+latex(pow(m, 3))+('+')+latex(UnevaluatedExpr(pow(a, 3)))+'} \), при \( {'+latex(m)+('=')+latex(UnevaluatedExpr(m_))+'} \)'
            answer = float(1/(m_+a))
            if len(str(answer).split('.')[1]) <= 6:
                if answer % 1 == 0:
                    answer = int(answer)
                break
    return {
      "condition": task,
      "answer": answer
    }


def task_11997():
    """Задача №11997 с портала https://kuzovkin.info/one_exercise_1/11997"""
    while True:
        a, b, k, n = np.random.randint(1, 10, size=4)
        if k != 1 and n != 1 and a % k == 0 and b % n == 0:
            c = 3*a
            x, y = symbols('x y')
            task = r'Упростите выражение и найдите его значение: \( \frac{'+latex(UnevaluatedExpr(c*x))+('+')+latex(UnevaluatedExpr(b*y))+'}{'+latex(UnevaluatedExpr(a*pow(x, 2)*y))+'} {'+str('-')+'} \\frac{'+latex(UnevaluatedExpr(b*y))+('-')+latex(UnevaluatedExpr(a*x))+'}{'+latex(UnevaluatedExpr(b*x*pow(y, 2)))+'} \), при \( {'+latex(x)+'}{'+str('=')+'}\\frac{'+latex(UnevaluatedExpr(1))+'}{'+latex(UnevaluatedExpr(k))+'}{'+str(';')+'}{'+latex(y)+'}{'+str('=')+'}\\frac{'+latex(UnevaluatedExpr(1))+'}{'+latex(UnevaluatedExpr(n))+'} \)'
            answer = float(pow(a*(1/k+b*(1/n)) ,2))/(a*b*(pow(1/k, 2))*(pow(1/n, 2)))
            if a != x != y and len(str(answer).split('.')[1]) <= 6:
                if answer % 1 == 0:
                    answer = int(answer)
                break
    return {
      "condition": task,
      "answer": answer
    }


def task_16072():
    """Задача №16072 с портала https://kuzovkin.info/one_exercise_1/16072"""
    while True:
        x, y, z = np.random.randint(2, 15, size=3)
        if x != y != z and pow(y + z - x, 2) != 0:
            a, b, c = symbols('a b c')
            task = r'Упростите выражение и найдите его значение: \( ((\frac{'+latex(UnevaluatedExpr(1))+'}{'+latex(a)+'} {'+str('+')+'} \\frac{'+latex(UnevaluatedExpr(1))+'}{'+latex(b+c)+'}) {'+str(':')+'} (\\frac{'+latex(UnevaluatedExpr(1))+'}{'+latex(a)+'} {'+str('-')+'} \\frac{'+latex(UnevaluatedExpr(1))+'}{'+latex(b+c)+'})) {'+str(':')+'} ({'+latex(UnevaluatedExpr(1))+'}{'+str('+')+'} \\frac{'+latex(pow(b, 2))+('+')+latex(pow(c, 2))+('-')+latex(pow(a, 2))+'}{'+latex(2*b*c)+'}) \), при \( {'+latex(a)+'}{'+str('=')+'} {'+latex(UnevaluatedExpr(x))+'}{'+str(';')+'}{'+latex(b)+'}{'+str('=')+'}{'+latex(UnevaluatedExpr(y))+'}{'+str(';')+'}{'+latex(c)+'}{'+str('=')+'}{'+latex(UnevaluatedExpr(z))+'} \)'
            answer = float((2*y*z)/pow(y+z-x, 2))
            if len(str(answer).split('.')[1]) <= 6:
                if answer % 1 == 0:
                    answer = int(answer)
                break
    return {
      "condition": task,
      "answer": answer
    }


def task_16075():
    """Задача №16075 с портала https://kuzovkin.info/one_exercise_1/16075"""
    while True:
        a, b, c, d = np.random.randint(1, 15, size=4)
        if c > a and c > b and c > d:
            x_ = np.random.randint(1, 15)/10
            x = symbols('x')
            task = r'Упростите выражение и найдите его значение: \( ({'+latex(pow(x, 2))+('+')+latex(UnevaluatedExpr(a*x))+('-')+'} \\frac{'+latex(UnevaluatedExpr(c*x))+('-')+latex(UnevaluatedExpr(a))+'}{'+latex(UnevaluatedExpr(b*x))+('+')+latex(UnevaluatedExpr(d))+'}) {'+str(':')+'} ({'+latex(x)+('+')+latex(UnevaluatedExpr(d))+('-')+'} \\frac{'+latex(UnevaluatedExpr(a*pow(x, 2)))+('+')+latex(x)+('+')+latex(UnevaluatedExpr(a))+'}{'+latex(UnevaluatedExpr(b*x))+('+')+latex(UnevaluatedExpr(d))+'}) \), при \( {'+latex(x)+'}{'+str('=')+'}{'+latex(UnevaluatedExpr(x_))+'} \)'
            answer = float(b*x_-a)
            if len(str(answer).split('.')[1]) <= 6:
                if answer % 1 == 0:
                    answer = int(answer)
                break
    return {
      "condition": task,
      "answer": answer
    }


def task_16080():
    """Задача №16080 с портала https://kuzovkin.info/one_exercise_1/16080"""
    while True:
        a, m, k = np.random.randint(2, 15, size=3)
        if a != m and a < 10:
            b = a+1
            c = b+1
            n = m+1
            f = 4*b
            t = symbols('t')
            task = r'Упростите выражение: \( {(\frac{'+latex(UnevaluatedExpr(1))+'}{'+latex(pow(t, 2))+('+')+latex(UnevaluatedExpr(b*t))+('+')+latex(UnevaluatedExpr(a))+'} {'+str('+')+'} \\frac{'+latex(UnevaluatedExpr(2*t))+'}{'+latex(pow(t, 2))+('+')+latex(UnevaluatedExpr(c*t))+('+')+latex(UnevaluatedExpr(b))+'} {'+str('+')+'} \\frac{'+latex(UnevaluatedExpr(1))+'}{'+latex(pow(t, 2))+('+')+latex(UnevaluatedExpr(m*t))+('+')+latex(UnevaluatedExpr(n))+'})}^{'+latex(UnevaluatedExpr(2))+'} {'+str('\cdot')+'} \\frac{'+latex(pow(UnevaluatedExpr(t-b), 2))+('+')+latex(UnevaluatedExpr(f*t))+'}{'+latex(UnevaluatedExpr(k))+'} \)'
            answer = float(k)
            if len(str(answer).split('.')[1]) <= 6:
                if answer % 1 == 0:
                    answer = int(answer)
                break
    return {
      "condition": task,
      "answer": answer
    }


from functools import wraps
from string import Template
import random
import re as r
import math
import numpy as np
from decimal import Decimal

from sympy import *

from random import sample

def task(target, known):
    x_100 = random.randint(1,99)
    answer = x_100/100
    numb_1, numb_2 = '', 2
    segment_q = lambda x: latex(UnevaluatedExpr(S.One*pi*(math.floor(x*2/pi))/2)) + " < \\alpha < " + latex(UnevaluatedExpr(S.One*pi*(math.floor(x*2/pi)+1)/2))
    radian = random.randint(-10,10)
    if radian == 0:
        radian = 0.01
    segment = segment_q(radian)
    if x_100 != 10 or x_100 != (-10):

        if known == 'sin':
            sign_x = (sin(radian) / abs(sin(radian)))
            if target == 'sin':
                d = latex(sign_x * (sqrt(100 + x_100) - sqrt(100 - x_100)) / 20)
            if target == 'cos':
                d = latex(sign_x * sqrt(100 - x_100) / sqrt(200))
            if target == 'tg':
                d = latex(sign_x * (x_100) / (sqrt(2 * (10000 + x_100 ** 2 + sqrt(10000 + (x_100 ** 2)) * 100))))
            if target == 'ctg':
                d = latex(sign_x * 100 / (sqrt(2 * (10000 + x_100 ** 2 + (sqrt(10000 + x_100 ** 2)) * x_100))))

        if known == 'cos':
            sign_x = cos(2*radian)/abs(cos(2*radian))
            if target == 'sin':
                d = latex(sign_x * (sqrt(100+x_100)+sqrt(100-x_100))/20)
            if target == 'cos':
                d = latex(sign_x * (sqrt(100+x_100)/sqrt(2))/10)
            if target == 'tg':
                d = latex(sign_x * (sqrt(10000 + x_100**2 + 100*sqrt(10000 + x_100**2)))/(sqrt(20000 + 2* (x_100**2))))
            if target == 'ctg':
                d = latex(sign_x * (sqrt(10000 + x_100**2 + x_100 * sqrt(10000 + x_100**2)))/(sqrt(20000 + 2*(x_100**2))))

        if known == 'tg':
            sign_x = tan(2*radian)/abs(tan(2*radian))
            if target == 'sin':
                d = latex(sign_x * (sqrt(100+x_100)-sqrt(100-x_100))/((sqrt(100+x_100)+sqrt(100-x_100))))
            if target == 'cos':
                d = latex(sign_x * sqrt(100-x_100)/sqrt(100+x_100))
            if target == 'tg':
                d = latex(sign_x * x_100/(100 + sqrt(10000 + x_100**2)))
            if target == 'ctg':
                d = latex(sign_x * 100/(x_100 + sqrt(10000 + x_100**2)))

        if known == 'ctg':
            sign_x = tan(2*radian)/abs(tan(2*radian))
            if target == 'sin':
                d = latex(sign_x * (sqrt(100+x_100)+sqrt(100-x_100))/((sqrt(100+x_100)-sqrt(100-x_100))))
            if target == 'cos':
                d = latex(sign_x * sqrt(100+x_100)/sqrt(100-x_100))
            if target == 'tg':
                d = latex(sign_x * (100 + sqrt(10000 + x_100**2))/x_100)
            if target == 'ctg':
                d = latex(sign_x * (x_100 + sqrt(10000 + x_100**2))/100)

        if known == 'sin_2':
            sign_x = sin(radian)/abs(sin(radian))
            numb_1, numb_2 = 2, ''
            known = known[:-2]
            if target == 'sin' or target == 'cos':
                d = latex(sign_x * (x_100 * (sqrt(10000 - x_100**2)) /5000))
            if target == 'tg' or target == 'ctg':
                d = "\\frac{"+str((sign_x * 200 * x_100)/(math.gcd((200 * x_100), (10000 + x_100**2))))+"}{"+str((10000 + x_100**2)/(math.gcd((200 * x_100), (10000 + x_100**2))))+"}"

        if known == 'cos_2':
            sign_x = cos(radian)/abs(cos(radian))
            numb_1, numb_2 = 2, ''
            known = known[:-2]
            if target == 'sin':
                d = "\\frac{"+str(int(sign_x * (5000 - x_100**2)/(math.gcd((5000 - x_100**2),5000))))+"}{"+str(int((5000)/(math.gcd((5000 - x_100**2),5000))))+"}"
            if target == 'cos':
                d = "\\frac{"+str(int(sign_x * (x_100**2 - 5000)/(math.gcd((x_100**2 - 5000),5000))))+"}{"+str(int((5000)/(math.gcd((x_100**2 - 5000),5000))))+"}}"
            if target == 'tg':
                d = "\\frac{"+str(int(sign_x * (10000 - x_100**2)/(math.gcd((10000 - x_100**2), (10000 + x_100**2)))))+"}{"+str(int((10000 + x_100**2)/(math.gcd((10000 - x_100**2), (10000 + x_100**2)))))+"}"
            if target == 'ctg':
                d = "\\frac{"+str(int(sign_x * (x_100**2 - 10000)/(math.gcd((x_100**2 - 10000), (10000 + x_100**2)))))+"}{"+str(int((10000 + x_100**2)/(math.gcd((x_100**2 - 10000), (10000 + x_100**2)))))+"}"

        if known == 'tg_2':
            sign_x = tan(radian)/abs(tan(radian))
            numb_1, numb_2 = 2, ''
            known = known[:-2]
            if target == 'sin':
                d = latex(sign_x * (x_100 * (sqrt(10000 - x_100**2))) /(5000 - x_100**2))
            if target == 'cos':
                d = latex(sign_x * (x_100 * (sqrt(10000 - x_100**2))) /(x_100**2 - 5000))
            if target == 'tg':
                d = "\\frac{"+str(int(sign_x * (200 * x_100)/(math.gcd((200 * x_100), (10000 - x_100**2)))))+"}{"+str(int((10000 - x_100**2)/(math.gcd((200 * x_100), (10000 - x_100**2)))))+"}"
            if target == 'ctg':
                d = "\\frac{"+str(int(sign_x * (200 * x_100)/(math.gcd((200 * x_100), (x_100**2 - 10000)))))+"}{"+str(int((x_100**2 - 10000)/(math.gcd((200 * x_100), (x_100**2 - 10000)))))+"}"

        if known == 'ctg_2':
            sign_x = tan(radian)/abs(tan(radian))
            numb_1, numb_2 = 2, ''
            known = known[:-2]
            if target == 'sin':
                d = latex(sign_x * (5000 - x_100**2)/(x_100 * (sqrt(10000 - x_100**2))))
            if target == 'cos':
                d = latex(sign_x * (x_100**2 - 5000)/(x_100 * (sqrt(10000 - x_100**2))))
            if target == 'tg':
                d = "\\frac{"+str(int(sign_x * (10000 - x_100**2)/(math.gcd((10000 - x_100**2), (200 * x_100)))))+"}{"+str(int((200 * x_100)/(math.gcd((10000 - x_100**2), (200 * x_100)))))+"}"
            if target == 'ctg':
                d = "\\frac{"+str(int(sign_x * (x_100**2 - 10000)/(math.gcd((x_100**2 - 10000), (200 * x_100)))))+"}{"+str(int((200 * x_100)/(math.gcd((x_100**2 - 10000), (200 * x_100)))))+"}"

        if sign_x == 1:
            answer = answer
        else:
            answer = -answer

    task = "Зная, что $\\"+str(known)+"("+str(numb_1)+"\\alpha)="+""+str(d)+"$ и $"+str(segment)+"$, найдите: $ \\"+str(target)+"("+str(numb_2)+"\\alpha)$"

    return task, answer
def trig_identity(target_known='sin-sin'):
    target, known = target_known.split("-")
    t, a = task(target, known)
    return {
        'condition': t,
        'answer': a
        }


