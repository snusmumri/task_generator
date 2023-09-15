from sympy import *
import numpy as np
import fractions
from fractions import Fraction
import random
import math
import decimal

def task_2908():
    '''Задача №2908 с портала https://kuzovkin.info/one_exercise_1/2908 и аналогичная 6780'''
    while True:
      a, b, c = np.random.randint(2, 15, size=3)
      task = r'Возвести корень в степень: \(' + latex(pow(sqrt(a+b*sqrt(c))-sqrt(a-b*sqrt(c)), 2)) + '\)'
      answer = pow(pow(a+b*pow(c, 1/2), 1/2)-pow(a-b*pow(c, 1/2), 1/2), 2)
      if b%2==0 and a==pow(b/2, 2)+c:
        if b/2<c:
          break
    return task, round(answer, 5)

def task_2922():
    '''Задача №2922 с портала https://kuzovkin.info/one_exercise_1/2922 и аналогичные 2924, 6798'''
    while True:
      a = np.random.randint(2, 20)
      n = np.random.randint(2, 15)
      b = pow(a, n)
      task = r'Извлечь корень: \( \sqrt['+str(n)+']{'+str(b)+'} \)'
      answer = pow(b, 1/n)
      if b<=10000:
        break
    return task, int(answer)

def task_2963():
    '''Задача №2963 с портала https://kuzovkin.info/one_exercise_1/2963'''
    while True:
      a, b, c = np.random.randint(1, 10, size=3)
      num_ = pow(b, 2)*c
      task = r'Вычислить: \( \frac{'+latex(sqrt(UnevaluatedExpr(num_)))+'}{'+latex((UnevaluatedExpr(a)+sqrt(UnevaluatedExpr(b)))*(sqrt(UnevaluatedExpr(b*c))-sqrt(UnevaluatedExpr(c))))+'} \)'
      answer = (pow(num_, 1/2))/((a+pow(b, 1/2))*(pow(b*c, 1/2)-pow(c, 1/2)))
      if a!=b!=c:
        if b!=1 and c!=1:
          if abs(int(answer*1000) - answer*1000) < 0.000001:
            break
    return task, answer

def task_2967():
    '''Задача №2967 с портала https://kuzovkin.info/one_exercise_1/2967'''
    while True:
      b = np.random.randint(1, 9)
      a = random.randint(2, 9)
      while sqrt(a) == int(a):
        a = random.randint(2, 9)
      task = r'Вычислить: \( \frac{'+latex(sqrt(UnevaluatedExpr(a))-UnevaluatedExpr(b))+'}{'+latex(sqrt(UnevaluatedExpr(a))+UnevaluatedExpr(b))+'}+\\frac{'+latex(sqrt(UnevaluatedExpr(a))+UnevaluatedExpr(b))+'}{'+latex(sqrt(UnevaluatedExpr(a))-UnevaluatedExpr(b))+'} \)'
      answer = (pow(a, 1/2)-b)/(pow(a, 1/2)+b) + (pow(a, 1/2)+b)/(pow(a, 1/2)-b)
      if a!=b:
        if abs(int(answer*1000) - answer*1000) < 0.000001:
          break
    return task, int(answer)

def task_3012():
    '''Задача №3012 с портала https://kuzovkin.info/one_exercise_1/3012'''
    while True:
      a = np.random.randint(2, 5)
      m, n = np.random.randint(2, 5, size=2)
      b = pow(a, n)
      task = r'Вычислить: \(' + latex(pow(UnevaluatedExpr(b), -UnevaluatedExpr(m)/UnevaluatedExpr(n))) + '\)'
      c = 1/b
      answer = pow(c, m/n)
      if m>n and m%n==1:
        break
    return task, round(answer, 5)

def task_3013():
    '''Задача №3013 с портала https://kuzovkin.info/one_exercise_1/3013'''
    while True:
      a = np.random.randint(2, 10)
      m, n = np.random.randint(2, 5, size=2)
      b = pow(a, n)
      task = r'Вычислить: \(' + latex(pow(UnevaluatedExpr(-b), UnevaluatedExpr(m)/UnevaluatedExpr(n))) + '\)'
      result = pow(-a, m)
      answer = Fraction(result).limit_denominator()
      if m<n and n%m==1:
        break
    return task, answer

def task_6500():
    '''Задача №6500 с портала https://kuzovkin.info/one_exercise_1/6500'''
    while True:
      a, b = np.random.randint(2, 6, size=2)
      n = np.random.randint(2, 6)
      a_ = pow(a, n)
      b_ = pow(b, n)
      task = r'Извлечь корень: \( \sqrt['+str(n)+']{'+str(a_)+str('\cdot')+str(b_)+'} \)'
      answer = pow(a_*b_, 1/n)
      task_1 = r'Извлечь корень: \( \sqrt{'+str(a_)+str('\cdot')+str(b_)+'} \)'
      if n == 2:
          task = task_1
      if a!=b:
        break
    return task, int(answer)

def task_6509():
    '''Задача №6509 с портала https://kuzovkin.info/one_exercise_1/6509'''
    while True:
      a = np.random.randint(2, 6)
      n = np.random.randint(2, 6)
      a_ = pow(a, n)
      task = r'Извлечь корень: \( \sqrt['+str(-n)+']{-\\frac{1}{'+latex(UnevaluatedExpr(a_))+'}} \)'
      answer = pow(a_, 1/n)
      if n%2==1:
        break
    return task, int(answer)

def task_6696():
    '''Задача №6696 с портала https://kuzovkin.info/one_exercise_1/6696'''
    while True:
      a = np.random.randint(2, 6)
      n, m, k, p = np.random.randint(2, 6, size=4)
      a_ = pow(a, p)
      b_ = pow(a, n)
      c_ = pow(a, k)
      task = r'Извлечь корень: \( \frac{1}{'+latex(UnevaluatedExpr(a))+'}\sqrt['+str(m)+']{'+str(b_)+'} {'+str('\cdot')+'} \\frac{1}{'+latex(UnevaluatedExpr(a_))+'}\sqrt['+str(m)+']{'+str(c_)+'} \)'
      task_1 = r'Извлечь корень: \( \frac{1}{'+latex(UnevaluatedExpr(a))+'}\sqrt{'+str(b_)+'} {'+str('\cdot')+'} \\frac{1}{'+latex(UnevaluatedExpr(a_))+'}\sqrt{'+str(c_)+'} \)'
      step = -1+n/m-p+k/m
      result = pow(a, step)
      if m == 2:
          task = task_1
      answer = Fraction(result).limit_denominator()
      if m!=n!=k!=p:
        if (n+k)%m==0:
          break
    return task, answer

def task_6729():
    '''Задача №6729 с портала https://kuzovkin.info/one_exercise_1/6729 и аналогичная '''
    while True:
      a, b = np.random.randint(2, 100, size=2)
      task = r'Извлечь корень: \( \sqrt{'+str(a)+'} {'+str(':')+'} \sqrt{'+str(b)+'} \)'
      answer = pow(a/b, 1/2)
      if a%b==0 and a!=b:
        if abs(int(answer*1000) - answer*1000) < 0.000001:
          break
    return task, int(answer)

def task_6700():
    '''Задача №6700 с портала https://kuzovkin.info/one_exercise_1/6700'''
    while True:
      a, b, c, d, p, q = np.random.randint(2, 9, size=6)
      n = np.random.randint(2, 6)
      b_ = pow(b, n)
      c_ = pow(c, n)
      task = r'Произвести действия с корнями: \( (\sqrt['+str(n)+']{'+str(a)+'} {'+str('-')+str(p)+'} \sqrt['+str(n)+']{'+str(b_*a)+'} {'+str('+')+str(q)+'} \sqrt['+str(n)+']{'+str(c_*a)+'}){'+str('\cdot')+'}{'+str(d)+'}\sqrt['+str(n)+']{\\frac{1}{'+latex(UnevaluatedExpr(a))+'}} \)'
      task_1 = r'Произвести действия с корнями: \( (\sqrt{'+str(a)+'} {'+str('-')+str(p)+'} \sqrt{'+str(b_*a)+'} {'+str('+')+str(q)+'} \sqrt{'+str(c_*a)+'}){'+str('\cdot')+'}{'+str(d)+'}\sqrt{\\frac{1}{'+latex(UnevaluatedExpr(a))+'}} \)'
      if n == 2:
          task = task_1
      answer = (1-p*b+q*c)*d
      if a!=b!=c:
        if p!=q!=d:
          break
    return task, answer

def task_6730():
    '''Задача №6730 с портала https://kuzovkin.info/one_exercise_1/6730'''
    while True:
      a, b, c = np.random.randint(2, 100, size=3)
      n = np.random.randint(2, 6)
      a_ = pow(a, n)
      task = r'Извлечь корень: \( \sqrt['+str(n)+']{'+str(b)+'} {'+str(':')+'} \sqrt['+str(n)+']{'+str(c)+'} \)'
      task_1 = r'Извлечь корень: \( \sqrt{'+str(b)+'} {'+str(':')+'} \sqrt{'+str(c)+'} \)'
      if n == 2:
        task = task_1
      answer = a
      if b/c==pow(a, n):
        break
    return task, int(answer)

def task_6884():
    '''Задача №6884 с портала https://kuzovkin.info/one_exercise_1/6884 и аналогичная 13135'''
    while True:
      a, n, m = np.random.randint(1, 6, size=3)
      b = pow(a, n)
      frac = fractions.Fraction(m, n)
      task = r'Вычислить: \('+ latex(pow(UnevaluatedExpr(b), UnevaluatedExpr(frac))) +'\)'
      answer = pow(a, m)
      if m<n and a!=1:
        break
    return task, answer

def task_6887():
    '''Задача №6887 с портала https://kuzovkin.info/one_exercise_1/6887'''
    while True:
      a, b = np.random.randint(2, 6, size=2)
      n = np.random.randint(2, 5)
      a_ = pow(a, n)
      b_ = pow(b, n)
      frac = fractions.Fraction(a_, b_)
      frac_pow = fractions.Fraction(1, n)
      task = r'Вычислить: \('+ latex(pow(UnevaluatedExpr(frac), -UnevaluatedExpr(frac_pow))) +'\)'
      answer = b/a
      if a!=b:
        if abs(int(answer*1000) - answer*1000) < 0.000001:
          break
    return task, round(answer, 5)

def task_6827():
    '''Задача №6827 с портала https://kuzovkin.info/one_exercise_1/6827'''
    while True:
      a, b = np.random.randint(2, 6, size=2)
      while sqrt(b) == int(b):
        b = random.randint(2, 6)
      c = pow(a, 2)
      d = pow(b, 2)
      e = a*b
      f = c+b+e
      task = r'Вычислить: \('+ latex(sqrt(UnevaluatedExpr(f)+UnevaluatedExpr(e)*sqrt(UnevaluatedExpr(d)+sqrt(UnevaluatedExpr(c)+UnevaluatedExpr(2*b)*sqrt(UnevaluatedExpr(b))))))+latex(-sqrt(UnevaluatedExpr(b)))+'\)'
      answer = a
      if a!=b:
        break
    return task, answer

def task_6888():
    '''Задача №6888 с портала https://kuzovkin.info/one_exercise_1/6888'''
    while True:
      a, b = np.random.randint(2, 6, size=2)
      m, n = np.random.randint(2, 4, size=2)
      a_ = pow(a, n)
      b_ = pow(b, n)
      whole_part = b_//a_
      num = b_%a_
      frac = fractions.Fraction(num, a_)
      frac_pow = fractions.Fraction(m, n)
      task = r'Вычислить: \( ({'+str('-')+'}{'+str(whole_part)+'}{'+latex(UnevaluatedExpr(frac))+'})^{{'+str('-')+'}\\frac{'+latex(UnevaluatedExpr(m))+'}{'+latex(UnevaluatedExpr(n))+'}} \)'
      answer = pow(a/b, m)
      if a<b and m<n:
        if abs(int(answer*1000) - answer*1000) < 0.000001:
          break
    return task, round(answer, 5)

def task_12799():
    '''Задача №12799 с портала https://kuzovkin.info/one_exercise_1/12799 '''
    while True:
      a, b = np.random.randint(2, 10, size=2)
      n = np.random.randint(2, 5)
      task = r'Извлечь корень: \( \sqrt'+ ('['+str(n)+']{' if n > 2 else '{') + latex(UnevaluatedExpr(pow(a, n))*pow(UnevaluatedExpr(b), n))+'} \)'
      answer = a*b
      if a!=b:
        break
    return task, int(answer)

def task_13134():
    '''Задача №13134 с портала https://kuzovkin.info/one_exercise_1/13134 '''
    while True:
      m, k, n, l = np.random.randint(2, 12, size=4)
      a = pow(m, 2) - k
      b = k-l
      c = pow(n, 2) - l
      while sqrt(k) == int(k) or sqrt(l) == int(l):
        k, l = random.randint(2, 14, size=2)
      task = r'Вычислить: \( \frac{'+latex(UnevaluatedExpr(a))+'}{'+latex(m)+latex(-sqrt(k))+'}{'+str('-')+'}\\frac{'+latex(UnevaluatedExpr(b))+'}{'+latex(sqrt(k))+latex(-sqrt(l))+'}{'+str('-')+'}\\frac{'+latex(UnevaluatedExpr(c))+'}{'+latex(UnevaluatedExpr(n)+sqrt(UnevaluatedExpr(l)))+'}\)'
      answer = m-n
      if k-l!=0 and a>0 and b>0 and c>0:
        break
    return task, answer

def task_13135():
    '''Задача №13135 с портала https://kuzovkin.info/one_exercise_1/13135 '''
    while True:
      a, b, c = np.random.randint(2, 12, size=3)
      d = np.random.randint(1, 40)
      check = pow(c, 2) - pow(b, 2)*a
      while sqrt(a) == int(a):
        a = random.randint(2, 12)
      task = r'Вычислить: \( \frac{'+latex(UnevaluatedExpr(d))+'}{'+latex(UnevaluatedExpr(c)+UnevaluatedExpr(b))+latex(sqrt(UnevaluatedExpr(a)))+'}{'+str('+')+'}\\frac{'+latex(UnevaluatedExpr(d))+'}{'+latex(UnevaluatedExpr(c))+latex(-UnevaluatedExpr(b)*sqrt(UnevaluatedExpr(a)))+'} \)'
      answer = 2*c*d
      if check == 1:
        break
    return task, answer

def task_13191():
    '''Задача №13191 с портала https://kuzovkin.info/one_exercise_1/13191'''
    while True:
      a = np.random.randint(1, 10)/10
      b = pow(a, 2)
      task = r'Вычислить: \('+ latex(pow(UnevaluatedExpr(b), UnevaluatedExpr(0.5))) +'\)'
      answer = a
      if answer:
        break
    return task, answer

def task_13192():
    '''Задача №13192 с портала https://kuzovkin.info/one_exercise_1/13192'''
    while True:
      a = np.random.randint(2, 6)
      m, n = np.random.randint(2, 6, size=2)
      b = pow(a, n)
      frac = fractions.Fraction(m, n)
      task = r'Вычислить: \('+ latex(pow(UnevaluatedExpr(b), -m/n)) +'\)'
      result = fractions.Fraction(1, pow(a, m))
      answer = Fraction(result).limit_denominator()
      if m<n:
        if abs(frac*1000 - int(frac*1000)) < 0.000001:
          break
    return task, answer

def task_13193():
    '''Задача №13193 с портала https://kuzovkin.info/one_exercise_1/13193'''
    while True:
      a, b, c = np.random.randint(2, 5, size=3)
      m, n, k, p = np.random.randint(1, 5, size=4)
      a_ = pow(a, n)
      b_ = pow(b, k)
      c_ = pow(c, p)
      frac_1 = fractions.Fraction(m, n)
      frac_2 = fractions.Fraction(1, k)
      frac_3 = fractions.Fraction(1, p)
      task = r'Вычислить: \('+ latex(pow(UnevaluatedExpr(a_), UnevaluatedExpr(frac_1))-pow(UnevaluatedExpr(b_), UnevaluatedExpr(frac_2))+pow(UnevaluatedExpr(c_), UnevaluatedExpr(frac_3))) +'\)'
      answer = pow(a, m)-b+c
      if m<n and k!=1 and p!=1 and n!=1:
        break
    return task, answer

def task_13194():
    '''Задача №13194 с портала https://kuzovkin.info/one_exercise_1/13194'''
    while True:
      a, b, c = np.random.randint(2, 5, size=3)
      m, n, k, p = np.random.randint(2, 5, size=4)
      a_ = pow(a, k)
      b_ = fractions.Fraction(1, pow(b, n))
      c_ = fractions.Fraction(1, c)
      frac_1 = fractions.Fraction(1, k)
      frac_2 = fractions.Fraction(m, n)
      task = r'Вычислить: \('+latex(pow(UnevaluatedExpr(a_), 1/k)+(pow(UnevaluatedExpr(b_), -m/n))-pow(UnevaluatedExpr(c_), -p))+'\)'
      answer = a+pow(b, m)-pow(c, p)
      if m<n:
        if abs(frac_1*1000 - int(frac_1*1000)) < 0.000001 and abs(frac_2*1000 - int(frac_2*1000)) < 0.000001:
          break
    return task, answer

def task_16768():
    '''Задача №16768 с портала https://kuzovkin.info/one_exercise_1/16768 '''
    while True:
      a, b = np.random.randint(2, 14, size=2)
      c = a+b
      d = a*b
      while sqrt(a) == int(a) and sqrt(b) == int(b):
        a, b = random.randint(2, 14, size=2)
      task = r'Вычислить: \( \frac{'+latex(sqrt(UnevaluatedExpr(c)-b*sqrt(UnevaluatedExpr(d))))+'}{(\sqrt['+str(4)+']{'+str(a)+'}+\sqrt['+str(4)+']{'+str(b)+'})(\sqrt['+str(4)+']{'+str(a)+'}-\sqrt['+str(4)+']{'+str(b)+'})} \)'
      answer = 1
      if a>b:
        break
    return task, answer

def task_16885():
    '''Задача №16885 с портала https://kuzovkin.info/one_exercise_1/16885 '''
    while True:
      a, b = np.random.randint(2, 6, size=2)
      while sqrt(b) == int(b):
        b = random.randint(2, 6, size=2)
      task = r'Вычислить: \('+ latex(sqrt(UnevaluatedExpr(a)+sqrt(UnevaluatedExpr(b))))+latex(sqrt(UnevaluatedExpr(a)+sqrt(UnevaluatedExpr(a)+sqrt(UnevaluatedExpr(b)))))+latex(sqrt(a+sqrt(UnevaluatedExpr(a)+sqrt(UnevaluatedExpr(a)+sqrt(UnevaluatedExpr(b))))))+latex(sqrt(a-sqrt(UnevaluatedExpr(a)+sqrt(UnevaluatedExpr(a)+sqrt(UnevaluatedExpr(b))))))+'\)'
      answer = sqrt(pow(a, 2)-b)
      if answer == int(answer):
        if answer!=0:
          break
    return task, answer

def task_16902():
    '''Задача №16902 с портала https://kuzovkin.info/one_exercise_1/16902 '''
    while True:
      a, b, c = np.random.randint(1, 30, size=3)
      x = symbols('x')
      eq_show = Eq(sqrt(a-pow(x, 2)) - sqrt(b-pow(x, 2)), c)
      task = r'Чему равна сумма \('+ latex(sqrt(UnevaluatedExpr(a)-UnevaluatedExpr(pow(x, 2)))+sqrt(UnevaluatedExpr(b)-UnevaluatedExpr(pow(x, 2))))+'\) , если известно, что разность \('+ latex(eq_show) +'\)'
      answer = (a-b)/c
      if answer>0:
        if answer == int(answer):
          break
    return task, int(answer)

def task_16907():
    '''Задача №16907 с портала https://kuzovkin.info/one_exercise_1/16907 '''
    while True:
      a, b, c = np.random.randint(2, 19, size=3)
      x = symbols('x')
      eq_show = Eq(sqrt(a-x) + sqrt(b+x), c)
      task = r'Если \('+latex(eq_show)+'\) ,то чему равен \('+ latex(sqrt((UnevaluatedExpr(a)-UnevaluatedExpr(x))*(UnevaluatedExpr(b)+UnevaluatedExpr(x)))) +'\)'
      answer = (pow(c, 2)-(a+b))/2
      if answer>0 and a!=b:
        if answer == int(answer):
          break
    return task, int(answer)

def task_16906():
    '''Задача №16906 с портала https://kuzovkin.info/one_exercise_1/16906 '''
    while True:
      a, b, c = np.random.randint(2, 19, size=3)
      y = symbols('y')
      task = r'Сделать указанную подстановку и упростить результат: \( \frac{'+latex((1-y)*(y+2))+'}{'+latex(pow(y, 2)*pow(y+1, 2))+'}{'+str(';')+'}{'+latex(y)+'}{'+str('=')+'}{'+latex((sqrt(UnevaluatedExpr(a))-UnevaluatedExpr(1))/c)+'} \)'
      num = (pow(c+b, 2)-a)/pow(c, 2)
      dec = pow((a-b)/c, 2)
      answer = num/dec
      if answer>0 and a>b:
        if answer == int(answer):
          break
    return task, int(answer)

def task_16949():
    '''Задача №16949 с портала https://kuzovkin.info/one_exercise_1/16949 '''
    while True:
      y = np.random.randint(1, 6)
      x = pow(y, 2)
      a = symbols('a')
      b = symbols('b')
      c = symbols('c')
      task = r'Упростить выражение: \( {(\frac{'+latex(UnevaluatedExpr(x))+'}{'+latex(UnevaluatedExpr(a)+UnevaluatedExpr(1/(b+(1/c))))+'}{'+str(':')+'} \\frac{'+latex(1)+'}{'+latex(UnevaluatedExpr(a)+UnevaluatedExpr(1/b))+'}{'+str('-')+'}\\frac{'+latex(UnevaluatedExpr(x))+'}{'+latex(b*(a*b*c+a+c))+'})}^{'+latex(-UnevaluatedExpr(1)/2)+'}\)'
      answer = 1/y
      if math.isfinite(answer) and y!=3:
        break
    return task, float(answer)

def task_16905():
    '''Задача №16905 с портала https://kuzovkin.info/one_exercise_1/16905 '''
    while True:
      b, c, d = np.random.randint(2, 7, size=3)
      x = pow(d, 2)*b
      y = pow(b, 2)*c
      z = (pow(d, 2)*b)/c
      task = r'Упростить выражение: \( \frac{'+latex(UnevaluatedExpr(b)*sqrt(UnevaluatedExpr(x)))+'}{'+latex(sqrt(UnevaluatedExpr(y)))+latex(-UnevaluatedExpr(pow(d, 2))*sqrt(UnevaluatedExpr(b)))+'}{'+str('+')+'}{'+latex(UnevaluatedExpr(c)*sqrt(UnevaluatedExpr(z)))+'}({'+latex(sqrt(UnevaluatedExpr(b*c))+UnevaluatedExpr(b))+'}) \)'
      answer = b*d
      if abs(z*1000 - int(z*1000)) < 0.000001:
        if answer == int(answer):
          break
    return task, int(answer)

def task_16990():
    '''Задача №16990 с портала https://kuzovkin.info/one_exercise_1/16990 '''
    while True:
      a, b, n, m = np.random.randint(2, 6, size=4)
      c, e = np.random.randint(2, 20, size=2)
      d = pow(b, 2)*a
      f = pow(a, m+n)
      i = pow(a, m+1)
      t = pow(b, m)*a
      k = pow(a, n-1)
      j = pow(b, n-1)
      task = r'Упростить выражение: \(  \frac{\sqrt['+str(m)+']{{'+latex(UnevaluatedExpr(c))+'}\\sqrt['+str(n)+']{'+latex(UnevaluatedExpr(d))+'}{'+str('+')+'}{'+latex(UnevaluatedExpr(e))+'}\\sqrt['+str(n)+']{'+latex(UnevaluatedExpr(f))+'}}}{\\sqrt['+str(n)+']{{'+latex(UnevaluatedExpr(k))+'}\\sqrt['+str(m)+']{'+latex(UnevaluatedExpr(i))+'}} {'+str('+')+'} \\sqrt['+str(n)+']{{'+latex(UnevaluatedExpr(j))+'}\\sqrt['+str(m)+']{'+latex(UnevaluatedExpr(t))+'}}} \)'
      answer = b/(a+b)
      if m!=n and pow(b, m)==c*b+e*a and m!=2 and n!=2:
        if abs(answer*1000 - int(answer*1000)) < 0.000001:
          break
    return task, float(answer)

def task_16887():
    '''Задача №16887 с портала https://kuzovkin.info/one_exercise_1/16887 '''
    while True:
      a, b = np.random.randint(2, 4, size=2)
      n = np.random.randint(2, 9)
      m = int(n/2)
      b_ = pow(b, 2)
      c = pow(b, m)*pow(a, n-m)
      task = r'Упростить выражение и вычислить: \( \frac{\sqrt{( \frac{{'+latex(UnevaluatedExpr(b_))+'}{'+latex(-UnevaluatedExpr(a)*UnevaluatedExpr(sqrt(b)))+'}}{{'+latex(sqrt(UnevaluatedExpr(b)))+'}{'+str('-')+'}\\sqrt['+str(m)+']{'+latex(UnevaluatedExpr(a))+'}} {'+str('+')+'}{'+latex(UnevaluatedExpr(b))+'}\\sqrt['+str(m)+']{'+latex(UnevaluatedExpr(a))+'}){'+latex(sqrt(UnevaluatedExpr(b)))+'}}}{{'+latex(UnevaluatedExpr(b))+'}{'+str('+')+'}\\sqrt['+str(n)+']{'+latex(UnevaluatedExpr(c))+'}} \)'
      answer = 1
      if n%2==0 and a!=b:
        break
    return task, answer
