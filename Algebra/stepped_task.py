from sympy import *
import numpy as np
import fractions
from fractions import Fraction
import random

def task_14784():
    '''Задача №14784 с портала https://kuzovkin.info/one_exercise_1/14784'''
    while True:
      a, b, c, d, whole_part = np.random.randint(1, 8, size = 5)
      frac_1 = fractions.Fraction(a, b)
      frac_2 = fractions.Fraction(d, a)
      mixed_fraction = whole_part + frac_2
      x = pow(frac_1, c)
      task = r'Вычислите: \(' + latex(pow(UnevaluatedExpr(frac_1), c)*(UnevaluatedExpr(whole_part))) + latex(UnevaluatedExpr(frac_2)) + '\)'
      answer = float(x * mixed_fraction)
      if d<a and a<b:
        if abs(int(answer*1000) - answer*1000)  < 0.000001:
          break
    return task, answer


def task_14785():
    '''Задача №14785 с портала https://kuzovkin.info/one_exercise_1/14785'''
    while True:
      a = np.random.randint(1, 40)/10
      b = np.random.randint(2, 51)
      c = np.random.randint(2, 5)
      x = pow(a, c)
      task = r'Вычислите: \(' + latex(pow(UnevaluatedExpr(a), c)/b) + '\)'
      answer = x / b
      if abs(answer*1000 - int(answer*1000)) < 0.0001:
         break
    return task, answer


def task_14809():
    '''Задача №14809 с портала https://kuzovkin.info/one_exercise_1/14809 и аналогичные к ней с 14810 по 14813'''
    while True:
      a, b = np.random.randint(2, 10, 2)
      m, n = np.random.randint(2, 6, 2)
      task = r'Вычислите: \(' + latex(a*pow(UnevaluatedExpr(b), m)) + '+' + latex(b*pow(UnevaluatedExpr(a), n)) + '\)'
      answer = a*pow(b, m) + b*pow(a, n)
      if a != b:
         break
    return task, answer


def task_14814():
    '''Задача №14814 с портала https://kuzovkin.info/one_exercise_1/14814'''
    while True:
      a, b = np.random.randint(2, 10, size=2)
      m, n = np.random.randint(2, 5, size=2)
      c = np.random.randint(1, 11)*10
      d = np.random.randint(1, 9)/10
      task = r'Вычислите: \(' + latex(pow(UnevaluatedExpr(a), n)*b+c*pow(UnevaluatedExpr(d), m)) + '\)'
      answer = pow(a, n)*b + c*pow(0.1, m)
      if answer < 2000:
         break
    return task, answer


def task_14815():
    '''Задача №14815 с портала https://kuzovkin.info/one_exercise_1/14815'''
    while True:
      a, b = np.random.randint(1, 10, size=2)
      m, n = np.random.randint(2, 5, size=2)
      c = np.random.randint(1, 10)*1000
      d = np.random.randint(2, 30)
      k = np.random.randint(1, 9)/10
      frac = fractions.Fraction(a, b)
      task = r'Вычислите: \(' + latex(d*pow(UnevaluatedExpr(frac), n)) + '+' + latex(pow(UnevaluatedExpr(k), m)*c) + '\)'
      answer = pow(frac, n)*d + pow(0.1, m)*c
      summand = pow(frac, n)*d
      if a<b:
        if abs(int(summand*1000) - summand*1000) < 0.000001:
          break
    return task, round(answer, 5)


def task_14816():
    '''Задача №14816 с портала https://kuzovkin.info/one_exercise_1/14816'''
    while True:
      a = np.random.randint(10, 101)
      b = np.random.randint(2, 11)
      m, n = np.random.randint(1, 11, size=2)
      d = np.random.randint(2, 500)
      c, k = np.random.randint(2, 5, size=2)
      frac = fractions.Fraction(m, n)
      task = r'Вычислите: \(' + latex(UnevaluatedExpr(a)) + ':' + latex(pow(UnevaluatedExpr(b), UnevaluatedExpr(k))) + '-' + latex(pow(UnevaluatedExpr(frac), c)*d) + '\)'
      answer = a/pow(b, k) - pow(frac, c)*d
      summand_1 = a/pow(b, k)
      summand_2 = pow(frac, c)*d
      if m<n:
        if abs(int(summand_2*1000) - summand_2*1000) < 0.000001:
          if abs(int(summand_1*1000) - summand_1*1000) < 0.000001:
            break
    return task, round(answer, 5)


def task_14817():
    '''Задача №14817 с портала https://kuzovkin.info/one_exercise_1/14817 и аналогичная 14818'''
    while True:
      a, b, c = np.random.randint(1, 7, size=3)
      m, n = np.random.randint(2, 5, size=2)
      whole_part_1, whole_part_2 = np.random.randint(1, 11, size=2)
      frac_1 = fractions.Fraction(a, b)
      frac_2 = fractions.Fraction(c, b)
      mix_frac_1 = whole_part_1 + frac_1
      mix_frac_2 = whole_part_2 + frac_2
      show_1 = pow(UnevaluatedExpr(mix_frac_1), m)
      show_2 = f"{whole_part_2}" + latex(UnevaluatedExpr(frac_2))
      # latex(pow(UnevaluatedExpr(whole_part_2)*UnevaluatedExpr(frac_2), n))
      task = r'Вычислите: \(' + latex(show_1) + '-' + show_2*n + '\)'
      result = pow(mix_frac_1, m) - pow(mix_frac_2, n)
      answer = float(result)
      if a<b and c<b:
        if abs(int(result*1000) - result*1000) < 0.000001:
          break
    return task, round(answer, 5)


def task_14819():
    '''Задача №14819 с портала https://kuzovkin.info/one_exercise_1/14819 и аналогичные 14820, 14821, 14822'''
    while True:
      a, b, c, d = np.random.randint(2, 10, size=4)
      m, n = np.random.randint(2, 5, size=2)
      task = r'Вычислите: \(' + latex(pow(UnevaluatedExpr(-a), m)/b) + '-' + latex(pow(UnevaluatedExpr(c), n)/d) + '\)'
      answer = - (fractions.Fraction(pow(-a, m), b)) - fractions.Fraction(pow(c, n), d)
      if m == n:
        break
    return task, answer


def task_14836():
    '''Задача №14836 с портала https://kuzovkin.info/one_exercise_1/14836 и аналогичные 14837, 14838'''
    while True:
      a, b, c = np.random.randint(-1, 2, size=3)
      m, n, k = np.random.randint(2, 70, size=3)
      task = r'Вычислите: \(' +latex(pow(UnevaluatedExpr(a), m))+ '+' +latex(pow(UnevaluatedExpr(b), n))+ '+' +latex(pow(UnevaluatedExpr(c), k))+ '\)'
      answer = pow(a, m) + pow(b, n) + pow(c, k)
      if a!=b or a!=c or c!=b:
        break
    return task, answer


def task_14839():
    '''Задача №14839 с портала https://kuzovkin.info/one_exercise_1/14839 и аналогичная 14840'''
    while True:
      a, b, c, d = np.random.randint(-1, 2, size=4)
      m, n, k, f = np.random.randint(2, 503, size=4)
      task = r'Вычислите: \(' +latex(pow(UnevaluatedExpr(a), m))+ '-' +latex(pow(UnevaluatedExpr(b), n))+ '+' +latex(pow(UnevaluatedExpr(c), k))+ '+' +latex(pow(UnevaluatedExpr(d), f)) + '\)'
      answer = pow(a, m) - pow(b, n) + pow(c, k) + pow(d, f)
      if a!=b or a!=c or c!=b:
        break
    return task, answer


def task_14841():
    '''Задача №14841 с портала https://kuzovkin.info/one_exercise_1/14841'''
    while True:
      a = -1
      m, n, k, f = np.random.randint(2, 10, size=4)
      task = r'Вычислите: \(' + latex(pow(UnevaluatedExpr(a), m)-pow(UnevaluatedExpr(a), n)-pow(UnevaluatedExpr(a), k)-pow(UnevaluatedExpr(a), f)) + '\)'
      answer = pow(a, m) - pow(a, n) - pow(a, k) - pow(a, f)
      if m!=n and m!=k and m!=f:
        if n!=k and n!=f:
          if k!=f:
            break
    return task, answer


def task_14842():
    '''Задача №14842 с портала https://kuzovkin.info/one_exercise_1/14842'''
    while True:
      a, b, c, d, e = np.random.randint(-1, 1, size=5)
      m, n, k, x, y = np.random.randint(2, 30, size=5)
      task = r'Вычислите: \(' +latex(pow(UnevaluatedExpr(a), m)+pow(UnevaluatedExpr(b), n)-(pow(UnevaluatedExpr(c), k))-(pow(UnevaluatedExpr(d), x))*(pow(UnevaluatedExpr(e), y)))+ '\)'
      answer = pow(a, m) + pow(b, n) - pow(c, k) - pow(d, x)*pow(e, y)
      if d!=e:
        break
    return task, answer


def task_15021():
    '''Задача №15021 с портала https://kuzovkin.info/one_exercise_1/15021 и аналогичные 15022, 15023'''
    while True:
      a = np.random.randint(2, 20)
      m, n, k = np.random.randint(1, 15, size=3)
      task = r'Вычислите: \( \frac{'+latex(pow(UnevaluatedExpr(a), UnevaluatedExpr(m))*pow(UnevaluatedExpr(a), UnevaluatedExpr(n)))+'}{'+latex(pow(UnevaluatedExpr(a), UnevaluatedExpr(k)))+'} \)'
      answer = pow(a, m)*pow(a, n)/pow(a, k)
      if abs(int(answer*1000) - answer*1000) < 0.000001:
        if answer < 1000:
          break
    return task, answer


def task_15024():
    '''Задача №15021 с портала https://kuzovkin.info/one_exercise_1/15024'''
    while True:
      a = np.random.randint(10, 50)
      m, n, k = np.random.randint(1, 15, size=3)
      task = r'Вычислите: \( \frac{'+latex(pow(UnevaluatedExpr(a), UnevaluatedExpr(m)))+'}{'+latex(pow(UnevaluatedExpr(a), UnevaluatedExpr(n))*(pow(UnevaluatedExpr(a), UnevaluatedExpr(k))))+'} \)'
      answer = pow(a, m)/(pow(a, n)*pow(a, k))
      if m>(n+k):
        if answer < 1000:
          break
    return task, round(answer)


def task_15025():
    '''Задача №15025 с портала https://kuzovkin.info/one_exercise_1/15025 и аналогичные 15027'''
    while True:
      a = np.random.randint(1, 9)/10
      m, n, k = np.random.randint(1, 15, size=3)
      task = r'Вычислите: \( \frac{'+latex(pow(UnevaluatedExpr(a), UnevaluatedExpr(m))*pow(UnevaluatedExpr(a), UnevaluatedExpr(n)))+'}{'+latex(pow(UnevaluatedExpr(a), UnevaluatedExpr(k)))+'} \)'
      answer = pow(a, m)*pow(a, n)/pow(a, k)
      if m+n-k < 4:
        if abs(int(answer*1000) - answer*1000) < 0.000001:
          break
    return task, round(answer, 5)


def task_15026():
    '''Задача №15026 с портала https://kuzovkin.info/one_exercise_1/15026 и аналогичные 15028'''
    while True:
      a, b = np.random.randint(1, 9, size=2)
      m, n, k = np.random.randint(1, 15, size=3)
      frac = fractions.Fraction(a, b)
      task = r'Вычислите: \( \frac{'+latex(pow(UnevaluatedExpr(frac), UnevaluatedExpr(m))*pow(UnevaluatedExpr(frac), UnevaluatedExpr(n)))+'}{'+latex(pow(UnevaluatedExpr(frac), UnevaluatedExpr(k)))+'} \)'
      answer = pow(frac, m)*pow(frac, n)/pow(frac, k)
      if a<b:
        if m+n > k:
          if abs(int(answer*1000) - answer*1000) < 0.000001:
            break
    return task, float(answer)


def task_15046():
    '''Задача №15046 с портала https://kuzovkin.info/one_exercise_1/15046 и аналогичные 15047, 15048, 15049'''
    while True:
      a = np.random.randint(2, 10)
      m, n= np.random.randint(2, 5, size=2)
      x_1 = pow(UnevaluatedExpr(a), UnevaluatedExpr(m))
      x_2 = pow(UnevaluatedExpr(x_1), UnevaluatedExpr(n))
      task = r'Вычислите: \(' +latex(x_2)+ '\)'
      answer = pow(pow(a, m), n)
      if answer < 1500:
        break
    return task, answer
