import random
import fractions
import numpy as np
from sympy import *

def task_16515():
  '''задача 16515 с портала https://kuzovkin.info/one_exercise_1/16515 Решите уравнение: 10⋅x2−(2⋅x−3)⋅(5⋅x−1)=31'''
  while True:
    x_int_1, x_int_2, int_1, int_2  = np.random.randint(1, 30, size=4)
    eq_ans = random.randint(1, 300)
    x = symbols('x')
    eq = Eq(x_int_1 * x_int_2 * x**2 - (x_int_1 * x - int_1) * (x_int_2 * x - int_2), eq_ans)
    task = r'Решите уравнение: \(' +latex(eq)+'\)'
    answer = solve(eq, x)
    if len(answer) > 0:
      if abs(int(answer[0]) - answer[0]) < 0.000001:
        break
  return task, round(answer[0])

def task_16616():
  '''задача 16616 (и аналогичные) с портала https://kuzovkin.info/one_exercise_1/16616 Решите уравнение: (x−2)⋅(x−3)=(x+2)⋅(x−5)'''
  while True:
    x_int_1, x_int_2, = [random.randrange(1, 10) for i in range(1, 3)]
    int_1, int_2, int_3, int_4 = [random.randrange(-20, 20) for i in range(1, 5)]
    while int_1 * int_2 * int_3 * int_4 == 0:
      int_1, int_2, int_3, int_4 = [random.randrange(-20, 20) for i in range(1, 5)]
    x = symbols('x')
    eq = Eq((x_int_1*x + int_1) * (x_int_2 * x + int_2), (x_int_1 * x_int_2 * x + int_3) * (x + int_4))
    task = r'Решите уравнение: \(' +latex(eq)+'\)'
    answer = solve(eq, x)
    if len(answer) > 0:
      if abs(int(answer[0]) - answer[0]) < 0.000001:
        break
  return task, round(answer[0])

def task_16641():
  '''задача 16641, 16689, 16690, 16691 с портала https://kuzovkin.info/one_exercise_1/16641 Решите уравнение: (2⋅x−3)/3+(7⋅x−13)/6+(5−2⋅x)/2=x−1'''
  while True:
    del_1, del_2 = [random.randrange(1, 30) for i in range(1, 3)]
    x_int_1, x_int_2, x_int_3, int_1, int_2, int_3, int_4 = [random.randrange(-20, 20) for i in range(1, 8)]
    while int_1 * int_2 * int_3 * int_4 * x_int_1 * x_int_2 * x_int_3 == 0:
      x_int_1, x_int_2, x_int_3, int_1, int_2, int_3, int_4 = [random.randrange(-20, 20) for i in range(1, 8)]
    x = symbols('x')
    eq_show = Eq(UnevaluatedExpr(x_int_1 * x + int_1)*Pow(del_1, -1) + UnevaluatedExpr(x_int_2 * x + int_2)*Pow(del_1 * del_2, -1) + UnevaluatedExpr(int_3 + x_int_3 * x) * Pow(del_2, -1), x + int_4)
    eq = Eq(((x_int_1 * x + int_1)/del_1) + ((x_int_2 * x + int_2)/(del_1 * del_2)) + ((int_3 + x_int_3 * x)/del_2), x + int_4)
    task = r'Решите уравнение: \(' +latex(eq_show)+'\)'
    answer = solve(eq, x)
    if len(answer) > 0:
      if abs(int(answer[0]) - answer[0]) < 0.000001:
        break
  return task, round(answer[0])

def task_16651():
  '''задача 16651 с портала https://kuzovkin.info/one_exercise_1/16651 Решите уравнение: (2⋅x+1)/5=1'''
  while True:
    del_1, x_int = [random.randrange(1, 30) for i in range(1, 3)]
    int_1, int_2 = [random.randrange(-20, 20) for i in range(1, 3)]
    while int_1 * int_2 == 0:
      int_1, int_2 = [random.randrange(-20, 20) for i in range(1, 3)]
    x = symbols('x')
    eq_show = Eq(UnevaluatedExpr(x_int * x + int_1)*Pow(del_1, -1), int_2)
    eq = Eq((x_int * x + int_1)/del_1, int_2)
    task = r'Решите уравнение: \(' +latex(eq_show)+'\)'
    answer = solve(eq, x)
    if len(answer) > 0:
      if abs(int(answer[0]) - answer[0]) < 0.000001:
        break
  return task, round(answer[0])

def task_16653():
  '''задача 16653 с портала https://kuzovkin.info/one_exercise_1/16653 Решите уравнение: (11−3⋅x)/4=1/2'''
  while True:
    n = random.randint(1, 20)
    m = random.randint(n+1, n+30)
    fract = fractions.Fraction(n, m)
    del_1, int_1 = [random.randrange(1, 30) for i in range(1, 3)]
    x_int = random.randrange(-20, 20)
    while x_int == 0:
      x_int = random.randrange(-20, 20)
    x = symbols('x')
    eq_show = Eq(UnevaluatedExpr(int_1 + x_int * x)*Pow(del_1, -1), n * Pow(m, -1))
    eq = Eq((int_1 + x_int * x)/del_1, fract)
    task = r'Решите уравнение: \(' +latex(eq_show)+'\)'
    answer = solve(eq, x)
    if len(answer) > 0:
      if abs(int(answer[0]) - answer[0]) < 0.000001:
        break
  return task, round(answer[0])

def task_16654():
  '''задача 16654 с портала https://kuzovkin.info/one_exercise_1/16654 Решите уравнение: (3⋅x+7)/5=(6⋅x+4)/5'''
  while True:
    x_int_1, x_int_2 = [random.randrange(1, 30) for i in range(1, 3)]
    int_1, int_2 = [random.randrange(-20, 20) for i in range(1, 3)]
    while int_1 * int_2 == 0:
      int_1, int_2 = [random.randrange(-20, 20) for i in range(1, 3)]
    del_1 = random.randrange(2, 30)
    x = symbols('x')
    eq_show = Eq(UnevaluatedExpr(x_int_1 * x + int_1)*Pow(del_1, -1), UnevaluatedExpr(x_int_2 * x + int_2)*Pow(del_1, -1))
    eq = Eq((x_int_1 * x + int_1)/del_1, (x_int_2 * x + int_2)/del_1)
    task = r'Решите уравнение: \(' +latex(eq_show)+'\)'
    answer = solve(eq, x)
    if len(answer) > 0:
      if abs(int(answer[0]) - answer[0]) < 0.000001:
        break
  return task, round(answer[0])

def task_16655():
  '''задача 16655, 16657 с портала https://kuzovkin.info/one_exercise_1/16655 Решите уравнение: 3⋅x−(2⋅x−1)/5=(3⋅x−19)/5'''
  while True:
    x_int_1, x_int_2, x_int_3 = [random.randrange(1, 30) for i in range(1, 4)]
    int_1, int_2 = [random.randrange(-20, 20) for i in range(1, 3)]
    while int_1 * int_2 == 0:
      int_1, int_2 = [random.randrange(-20, 20) for i in range(1, 3)]
    del_1 = random.randrange(2, 30)
    x = symbols('x')
    eq_show = Eq(x_int_1 * x - UnevaluatedExpr(x_int_2 * x + int_1)*Pow(del_1, -1), UnevaluatedExpr(x_int_3 * x + int_2)*Pow(del_1, -1))
    eq = Eq(x_int_1 * x - (x_int_2 * x + int_1)/del_1, (x_int_3 * x + int_2)/del_1)
    task = r'Решите уравнение: \(' +latex(eq_show)+'\)'
    answer = solve(eq, x)
    if len(answer) > 0:
      if abs(int(answer[0]) - answer[0]) < 0.000001:
        break
  return task, round(answer[0])

def task_16656():
  '''задача 16656, 16658 с портала https://kuzovkin.info/one_exercise_1/16656 Решите уравнение: (8⋅x−3)/7−(3⋅x+1)/10=2'''
  while True:
    x_int_1, x_int_2, del_1, del_2 = [random.randrange(1, 30) for i in range(1, 5)]
    int_1, int_2, int_3 = [random.randrange(-20, 20) for i in range(1, 4)]
    while int_1 * int_2 == 0:
      int_1, int_2 = [random.randrange(-20, 20) for i in range(1, 3)]
    x = symbols('x')
    eq_show = Eq(UnevaluatedExpr(x_int_1 * x + int_1)*Pow(del_1, -1) - UnevaluatedExpr(x_int_2 * x + int_2)*Pow(del_2, -1), int_3)
    eq = Eq(((x_int_1 * x + int_1)/del_1) - ((x_int_2 * x + int_2)/del_2), int_3)
    task = r'Решите уравнение: \(' +latex(eq_show)+'\)'
    answer = solve(eq, x)
    if len(answer) > 0:
      if abs(int(answer[0]) - answer[0]) < 0.000001:
        break
  return task, round(answer[0])

def task_16659():
  '''задача 16659 с портала https://kuzovkin.info/one_exercise_1/16659 Решите уравнение: 6⋅x⋅(x+2)−0,5⋅(12⋅x2−7⋅x)−31=0'''
  while True:
    x_sq = random.randrange(1, 20)
    deci_1 = random.randrange(0, 1000, 5) / 1000
    x_int, int_1, int_2 = [random.randrange(-30, 30) for i in range(1, 4)]
    while x_int * int_1 * int_2 == 0:
      x_int, int_1, int_2 = [random.randrange(-30, 30) for i in range(1, 4)]
    x = symbols('x')
    eq_show = Eq(UnevaluatedExpr(x_sq * deci_1 * x * (x + int_1)) - UnevaluatedExpr(deci_1) * (UnevaluatedExpr(x_sq * x**2) + UnevaluatedExpr(x_int * x)) + int_2, 0)
    eq = Eq((x_sq * deci_1 * x * (x + int_1)) - deci_1 * (x_sq * x**2 + x_int * x) + int_2, 0)
    task = r'Решите уравнение: \(' +latex(eq_show)+'\)'
    answer = solve(eq, x)
    if len(answer) > 0:
      if abs(int(answer[0]) - answer[0]) < 0.000001:
        break
  return task, round(answer[0])

def task_16660():
  '''задача 16660 с портала https://kuzovkin.info/one_exercise_1/16660 Решите уравнение: 2⋅x3−x⋅(x2−6)−3⋅(2⋅x−1)−30=0'''
  while True:
    x_cub = random.randrange(1, 20)
    x_sq = x_cub - 1
    x_int, int_1 = [random.randrange(1, 20) for i in range(1, 3)]
    int_2, int_3 = [random.randrange(-30, 30) for i in range(1, 3)]
    while int_2 * int_3 == 0:
      int_2, int_3 = [random.randrange(-30, 30) for i in range(1, 3)]
    x = symbols('x')
    eq_show = Eq(x_cub * x**3 - x * (x_sq * x**2 - int_1 * x_int) - int_1 * (UnevaluatedExpr(x_int * x + int_2)) + int_3, 0)
    eq = Eq(x_cub * x**3 - x * (x_sq * x**2 - int_1 * x_int) - int_1 * (x_int * x + int_2) + int_3, 0)
    task = r'Решите уравнение: \(' +latex(eq_show)+'\)'
    answer = solve(eq, x)
    if len(answer) > 0 and im(solve(eq, x)[0])==0:
      if abs(int(answer[0]) - answer[0]) < 0.000001:
        break
  return task, round(answer[0])

def task_16661():
  '''задача 16661 с портала https://kuzovkin.info/one_exercise_1/16661 Решите уравнение: 12⋅x⋅(x−8)−4⋅x⋅(3⋅x−5)=10−26⋅x'''
  while True:
    x_int_1, x_int_2 = [random.randrange(1, 20) for i in range(1, 3)]
    int_1, int_2, int_3, x_int_3 = [random.randrange(-30, 30) for i in range(1, 5)]
    while int_1 * int_2 * int_3 * x_int_3 == 0:
      int_1, int_2, int_3, x_int_3 = [random.randrange(-30, 30) for i in range(1, 5)]
    x = symbols('x')
    eq = Eq(x_int_1 * x_int_2 * x * (x + int_1) - x_int_1 * x * (x_int_2 * x + int_2), int_3 + x_int_3 * x)
    task = r'Решите уравнение: \(' +latex(eq)+'\)'
    answer = solve(eq, x)
    if len(answer) > 0:
      if abs(int(answer[0]) - answer[0]) < 0.000001:
        break
  return task, round(answer[0])

def task_16662():
  '''задача 16662 с портала https://kuzovkin.info/one_exercise_1/16662 Решите уравнение: 8⋅(x2−5)−5⋅x⋅(x+2)+10⋅(x+4)=0'''
  while True:
    x_int = random.randrange(1, 20)
    int_1, int_2, int_3, int_4 = [random.randrange(-30, 30) for i in range(1, 5)]
    while int_1 * int_2 * int_3 * int_4 == 0:
      int_1, int_2, int_3, int_4 = [random.randrange(-30, 30) for i in range(1, 5)]
    x = symbols('x')
    eq_show = Eq(int_1 * UnevaluatedExpr(x**2 + int_2) - x_int * x * (x + int_3) + x_int * int_3 * UnevaluatedExpr(x + int_4), 0)
    eq = Eq(int_1 * (x**2 + int_2) - x_int * x * (x + int_3) + x_int * int_3 * (x + int_4), 0)
    task = r'Решите уравнение: \(' +latex(eq_show)+'\)'
    answer = solve(eq, x)
    if len(answer) > 0 and im(solve(eq, x)[0])==0:
      if abs(int(answer[0]) - answer[0]) < 0.000001:
        break
  return task, round(answer[0])

def task_16664():
  '''задача 16664 с портала https://kuzovkin.info/one_exercise_1/16664 Решите уравнение:   x−3⋅x⋅(1−12⋅x)=11−(5−6⋅x)⋅(6⋅x+5)'''
  while True:
    x_int_1, x_int_2, x_int_3, x_int_4, int_1, int_2, int_3, int_4 = [random.randrange(1, 20) for i in range(1, 9)]
    while x_int_1 * x_int_2 != x_int_3 * x_int_4:
      x_int_1, x_int_2, x_int_3, x_int_4 = [random.randrange(1, 20) for i in range(1, 5)]
    x = symbols('x')
    eq = Eq(x - x_int_1 * x * (int_1 - x_int_2 * x), int_2 - (int_3 - x_int_3 * x) * (x_int_4 * x + int_4))
    task = r'Решите уравнение: \(' +latex(eq)+'\)'
    answer = solve(eq, x)
    if len(answer) > 0 and im(solve(eq, x)[0])==0:
      if abs(int(answer[0]) - answer[0]) < 0.000001:
        break
  return task, round(answer[0])

def task_16665():
  '''задача 16665 с портала https://kuzovkin.info/one_exercise_1/16665 Решите уравнение: (6⋅x−1)⋅(6⋅x+1)−4⋅x⋅(9⋅x+2)=−1'''
  while True:
    x_int_1, x_int_2, x_int_3, x_int_4 = [random.randrange(1, 20) for i in range(1, 5)]
    while x_int_1 * x_int_2 != x_int_3 * x_int_4:
      x_int_1, x_int_2, x_int_3, x_int_4 = [random.randrange(1, 20) for i in range(1, 5)]
    int_1, int_2, int_3, int_4 = [random.randrange(-10, 10) for i in range(1, 5)]
    while int_1 * int_2 * int_3 * int_4 == 0:
      int_1, int_2, int_3, int_4 = [random.randrange(-10, 10) for i in range(1, 5)]
    x = symbols('x')
    eq = Eq((x_int_1 * x + int_1) * (x_int_2 * x + int_2) - x_int_3 * x * (x_int_4 * x + int_3), int_4)
    task = r'Решите уравнение: \(' +latex(eq)+'\)'
    answer = solve(eq, x)
    if len(answer) > 0:
      if abs(int(answer[0]) - answer[0]) < 0.000001:
        break
  return task, round(answer[0])

def task_16667():
  '''задача 16667, 16670 с портала https://kuzovkin.info/one_exercise_1/16667 Решите уравнение: (x−6)ˆ2−x⋅(x+8)=2'''
  while True:
    x_int_1, x_int_2, x_int_3 = [random.randrange(1, 10) for i in range(1, 4)]
    while x_int_1**2 != x_int_2 * x_int_3:
      x_int_1, x_int_2, x_int_3 = [random.randrange(1, 10) for i in range(1, 4)]
    int_1, int_2, int_3 = [random.randrange(-10, 10) for i in range(1, 4)]
    while int_1 * int_2 == 0:
      int_1, int_2 = [random.randrange(-10, 10) for i in range(1, 3)]
    x = symbols('x')
    eq = Eq((x_int_1 * x + int_1)**2 - x_int_2 * x * (x_int_3 * x + int_2), int_3)
    task = r'Решите уравнение: \(' +latex(eq)+'\)'
    answer = solve(eq, x)
    if len(answer) > 0:
      if abs(int(answer[0]) - answer[0]) < 0.000001:
        break
  return task, round(answer[0])

def task_16672():
  '''задача 16672 с портала https://kuzovkin.info/one_exercise_1/16672 Решите уравнение: : x+(5⋅x+2)**2=25⋅(1+x**2)'''
  while True:
    x_int_1, int_1, int_2 = [random.randrange(-10, 10) for i in range(1, 4)]
    while x_int_1 * int_1 * int_2 == 0:
      x_int_1, int_1, int_2 = [random.randrange(-10, 10) for i in range(1, 4)]
    int_3, x_sq = [random.randrange(1, 20) for i in range(1, 3)]
    x = symbols('x')
    eq_show = Eq(x_int_1 * x + (int_3 * x_sq * x + int_1)**2, int_3 * UnevaluatedExpr(int_2 + x_sq * x**2))
    eq = Eq(x_int_1 * x + (int_3 * x_sq * x + int_1)**2, int_3 * (int_2 + x_sq * x**2))
    task = r'Решите уравнение: \(' +latex(eq_show)+'\)'
    answer = solve(eq, x)
    if len(answer) > 0 and im(solve(eq, x)[0])==0:
      if abs(int(answer[0]) - answer[0]) < 0.000001:
        break
  return task, round(answer[0])

def task_16676():
  '''задача 16676, 16678 с портала https://kuzovkin.info/one_exercise_1/16676 Решите уравнение: (2⋅x+3)**2−4⋅(x−1)⋅(x−1)=49'''
  while True:
    x_int_1, x_int_2, x_int_3, int_1 = [random.randrange(1, 10) for i in range(1, 5)]
    while x_int_1**2 != int_1 * x_int_2 * x_int_3:
      x_int_1, x_int_2, x_int_3, int_1 = [random.randrange(1, 10) for i in range(1, 5)]
    int_2, int_3, int_4 = [random.randrange(-10, 10) for i in range(1, 4)]
    while int_2 * int_3 * int_4 == 0:
      int_2, int_3, int_4 = [random.randrange(-10, 10) for i in range(1, 4)]
    answ_int = random.randrange(-100, 100)
    x = symbols('x')
    eq_show = Eq((x_int_1 * x + int_2)**2 - UnevaluatedExpr(int_1) * (x_int_2 * x + int_3) * (x_int_3 * x + int_4), answ_int)
    eq = Eq((x_int_1 * x + int_2)**2 - int_1 * (x_int_2 * x + int_3) * (x_int_3 * x + int_4), answ_int)
    task = r'Решите уравнение: \(' +latex(eq_show)+'\)'
    answer = solve(eq, x)
    if len(answer) > 0:
      if abs(int(answer[0]) - answer[0]) < 0.000001:
        break
  return task, round(answer[0])

def task_16679():
  '''задача 16679, 16680, 16681, 16682 с портала https://kuzovkin.info/one_exercise_1/16679 Решите уравнение: (x−1)⋅(x**2+x+1)=0'''
  while True:
    int_1, x_int_1 = [random.randrange(-5, 5) for i in range(1, 3)]
    while int_1 * x_int_1 == 0:
      int_1, x_int_1 = [random.randrange(-5, 5) for i in range(1, 3)]
    answ_int = random.randrange(-50, 50)
    x = symbols('x')
    eq = Eq((x + int_1) * (x**2 + x_int_1 * x - int_1 * x_int_1), 0)
    task = r'Решите уравнение: \(' +latex(eq)+'\)'
    answer = solve(eq, x)
    if len(answer) > 0:
      if abs(int(answer[0]) - answer[0]) < 0.000001:
        break
  return task, round(answer[0])

def task_16684():
  '''задача 16684, 16686 с портала https://kuzovkin.info/one_exercise_1/16684 Решите уравнение: (x**2−3)⋅(x+2)+(x**2+3)⋅(x−2)=4'''
  while True:
    int_1, int_2 = [random.randrange(-10, 10) for i in range(1, 3)]
    while int_1 * int_2 == 0:
      int_1, int_2 = [random.randrange(-10, 10) for i in range(1, 3)]
    answ_int = random.randrange(-30, 30)
    x = symbols('x')
    eq = Eq((x**2 + int_1) * (x + int_2) + (x**2 - int_1) * (x - int_2), answ_int)
    task = r'Решите уравнение: \(' +latex(eq)+'\)'
    answer = solve(eq, x)
    if len(answer) > 0 and im(solve(eq, x)[0])==0:
      if abs(int(answer[0]) - answer[0]) < 0.000001:
        break
  return task, round(answer[0])

def task_16687():
  '''задача 16687 с портала https://kuzovkin.info/one_exercise_1/16687 Решите уравнение: 12⋅x**2−(4⋅x−3)⋅(3⋅x+1)=−2'''
  while True:
    x_int_1, x_int_2, int_1, int_2 = [random.randrange(-10, 10) for i in range(1, 5)]
    while x_int_1 * x_int_2 == 0:
      x_int_1, x_int_2, int_1, int_2 = [random.randrange(-10, 10) for i in range(1, 5)]
    answ_int = random.randrange(-30, 30)
    x = symbols('x')
    eq = Eq(x_int_1 * x_int_2 * x**2 - (x_int_1 * x + int_1) * (x_int_2 * x + int_2), answ_int)
    task = r'Решите уравнение: \(' +latex(eq)+'\)'
    answer = solve(eq, x)
    if len(answer) > 0:
      if abs(int(answer[0]) - answer[0]) < 0.000001:
        break
  return task, round(answer[0])

def task_16692():
  '''задача 16692 с портала https://kuzovkin.info/one_exercise_1/16692 Решите уравнение: 2⋅x+x⋅(3−(x+1))=x⋅(2−x)+12'''
  while True:
    int_1, int_2, int_3 = [random.randrange(-20, 20) for i in range(1, 4)]
    while int_1 * int_2 * int_3 == 0:
       int_1, int_2, int_3 = [random.randrange(-20, 20) for i in range(1, 4)]
    x_int_1, x_int_2 = [random.randrange(-10, 10) for i in range(1, 3)]
    while x_int_1 * x_int_2  == 0:
      x_int_1, x_int_2 = [random.randrange(-10, 10) for i in range(1, 3)]
    x = symbols('x')
    eq = Eq(x_int_1 * x + x * (int_1 + x_int_2 * (x + int_2)), x * (x_int_1 + x_int_2 * x) + int_3)
    eq_show = Eq(x_int_1 * x + x * (int_1 + x_int_2 * UnevaluatedExpr(x + int_2)), x * (x_int_1 + x_int_2 * x) + int_3)
    task = r'Решите уравнение: \(' +latex(eq_show)+'\)'
    answer = solve(eq, x)
    if len(answer) > 0:
      if abs(int(answer[0]) - answer[0]) < 0.000001:
        break
  return task, round(answer[0])

def task_16693():
  '''задача 16693 с портала https://kuzovkin.info/one_exercise_1/16693 Решите уравнение: x**2⋅(5⋅x+3)−6⋅x⋅(x**2−4)=3⋅x⋅(8+x)'''
  while True:
    x_int_1, int_1, x_int_2, int_2 = [random.randrange(-20, 20) for i in range(1, 5)]
    while x_int_1 * int_1 * x_int_2 * int_2 == 0 or x_int_1 * int_1 != x_int_2 * int_2:
       x_int_1, int_1, x_int_2, int_2 = [random.randrange(-20, 20) for i in range(1, 5)]
    x = symbols('x')
    eq = Eq(x**2 * ((-1) * (1 + x_int_1) * x + x_int_2) + x_int_1 * x * (x**2 + int_1), x_int_2 * x * (int_2 + x))
    task = r'Решите уравнение: \(' +latex(eq)+'\)'
    answer = solve(eq, x)
    if len(answer) > 0:
      if abs(int(answer[0]) - answer[0]) < 0.000001:
        break
  return task, round(answer[0])

def task_16696():
  '''задача 16696, 16697 с портала https://kuzovkin.info/one_exercise_1/16696 Решите уравнение: (5⋅x−3)+(7⋅x−4)=8−(15−11⋅x)
  осталась нерешенная проблема с раскрытием скобок и урощением выводимого выражения
  '''
  while True:
    x_int_1, x_int_2, x_int_3, int_1, int_2, int_3, int_4 = [random.randrange(-20, 20) for i in range(1, 8)]
    while x_int_1 * x_int_2 * x_int_3 * int_1 * int_2 * int_3 * int_4 == 0:
       x_int_1, x_int_2, x_int_3, int_1, int_2, int_3, int_4 = [random.randrange(-20, 20) for i in range(1, 8)]
    x = symbols('x')
    eq = Eq((x_int_1 * x + int_1) + (x_int_2 * x + int_2), int_3 - (int_4 + x_int_3 * x))
    eq_show = Eq(Add((UnevaluatedExpr(x_int_1 * x) + UnevaluatedExpr(int_1)),  (UnevaluatedExpr(x_int_2 * x) - UnevaluatedExpr(int_2))), int_3 - (int_4 + UnevaluatedExpr(x_int_3 * x)))
    task = r'Решите уравнение: \(' +latex(eq_show)+'\)'
    answer = solve(eq, x)
    if len(answer) > 0:
      if abs(int(answer[0]) - answer[0]) < 0.000001:
        break
  return task, round(answer[0])

def task_16699():
  '''задача 16699 с портала https://kuzovkin.info/one_exercise_1/16699 Решите уравнение: (2⋅x+3)+(3⋅x+4)+(5⋅x+5)=12−7⋅x
  осталась нерешенная проблема с раскрытием скобок и урощением выводимого выражения
  '''
  while True:
    x_int_1, x_int_2, x_int_3, x_int_4, int_1, int_2, int_3, int_4 = [random.randrange(-20, 20) for i in range(1, 9)]
    while x_int_1 * x_int_2 * x_int_3 * x_int_4 * int_1 * int_2 * int_3 * int_4 == 0:
       x_int_1, x_int_2, x_int_3, x_int_4, int_1, int_2, int_3, int_4 = [random.randrange(-20, 20) for i in range(1, 9)]
    x = symbols('x')
    eq = Eq((x_int_1 * x + int_1) + (x_int_2 * x + int_2) + (x_int_3 * x + int_3), int_4 + x_int_4 * x)
    eq_show = Eq((UnevaluatedExpr(x_int_1 * x) + UnevaluatedExpr(int_1)) + (UnevaluatedExpr(x_int_2 * x) + UnevaluatedExpr(int_2)) + (UnevaluatedExpr(x_int_3 * x) + UnevaluatedExpr(int_3)), int_4 + x_int_4 * x)
    task = r'Решите уравнение: \(' +latex(eq_show)+'\)'
    answer = solve(eq, x)
    if len(answer) > 0:
      if abs(int(answer[0]) - answer[0]) < 0.000001:
        break
  return task, round(answer[0])

def task_16702():
  '''задача 16702 с портала https://kuzovkin.info/one_exercise_1/16702 Решите уравнение: 3/8*x−(1/3*x−2,4)=−0,4
  осталась нерешенная проблема с раскрытием скобок и урощением выводимого выражения
  '''
  while True:
    x_int_1, x_int_2 = [random.randrange(1, 10) for i in range(1, 3)]
    del_1 = random.randrange(x_int_1 + 1, x_int_1 + 20)
    del_2 = random.randrange(x_int_2 + 1, x_int_2 + 20)
    deci_1, deci_2 = [random.randrange(-1000, 1000, 5) / 100 for i in range(1, 3)]
    x = symbols('x')
    eq = Eq((x_int_1/del_1) * x - ((x_int_2/del_2) * x + deci_1), deci_2)
    eq_show = Eq(UnevaluatedExpr(x_int_1*Pow(del_1, -1) * x) - (UnevaluatedExpr(UnevaluatedExpr(x_int_2*Pow(del_2, -1) * x) + deci_1)), deci_2)
    task = r'Решите уравнение: \(' +latex(eq_show)+'\)'
    answer = solve(eq, x)
    if len(answer) > 0:
      if abs(int(answer[0]) - answer[0]) < 0.000001:
        break
  return task, round(answer[0])

def task_16703():
  '''задача 16703 с портала https://kuzovkin.info/one_exercise_1/16703 Решите уравнение: 1/2⋅x−(2,5⋅x−3)=1,8'''
  while True:
    x_int_1 = random.randrange(1, 10)
    del_1 = random.randrange(x_int_1 + 1, x_int_1 + 20)
    deci_x, deci_answ = [random.randrange(-1000, 1000, 5) / 100 for i in range(1, 3)]
    int_1 = random.randrange(-10, 10)
    while int_1 == 0:
      int_1 = random.randrange(-10, 10)
    x = symbols('x')
    eq = Eq((x_int_1/del_1) * x - (deci_x * x + int_1), deci_answ)
    eq_show = Eq(UnevaluatedExpr(x_int_1*Pow(del_1, -1) * x) - (UnevaluatedExpr(deci_x * x) + int_1), deci_answ)
    task = r'Решите уравнение: \(' +latex(eq_show)+'\)'
    answer = solve(eq, x)
    if len(answer) > 0:
      if abs(int(answer[0]) - answer[0]) < 0.000001:
        break
  return task, round(answer[0])

def task_16704():
  '''задача 16704 с портала https://kuzovkin.info/one_exercise_1/16704 Решите уравнение: 2x**2−(2⋅x**2−5⋅x)−(4⋅x−2)=5'''
  while True:
    x_sq = random.randrange(-10, 10)
    while x_sq == 0:
      x_sq = random.randrange(-10, 10)
    x_int_1, x_int_2 = [random.randrange(-15, 15) for i in range(1, 3)]
    while x_int_1 * x_int_2 == 0:
      x_int_1, x_int_2 = [random.randrange(-15, 15) for i in range(1, 3)]
    int_1, int_2 = [random.randrange(-30, 30) for i in range(1, 3)]
    while int_1 * int_2 == 0:
      int_1, int_2 = [random.randrange(-30, 30) for i in range(1, 3)]
    x = symbols('x')
    eq = Eq(x_sq * x**2 - (x_sq * x**2 + x_int_1 * x) - (x_int_2 * x + int_1), int_2)
    eq_show = Eq(UnevaluatedExpr(x_sq * x**2) - (UnevaluatedExpr(x_sq * x**2) + x_int_1 * x) - (UnevaluatedExpr(x_int_2 * x) + int_1), int_2)
    task = r'Решите уравнение: \(' +latex(eq_show)+'\)'
    answer = solve(eq, x)
    if len(answer) > 0:
      if abs(int(answer[0]) - answer[0]) < 0.000001:
        break
  return task, round(answer[0])

def task_16705():
  '''задача 16705 с портала https://kuzovkin.info/one_exercise_1/16705 Решите уравнение: (y**3+y)+(3−6⋅y)−(4−5⋅y)=−2
  осталась нерешенная проблема с раскрытием скобок и урощением выводимого выражения
  '''
  while True:
    y_int_1, y_int_2, y_int_3 = [random.randrange(-10, 10) for i in range(1, 4)]
    while y_int_1 + y_int_2 - y_int_3 != 0 or y_int_1 * y_int_2 * y_int_3 == 0:
      y_int_1, y_int_2, y_int_3 = [random.randrange(-10, 10) for i in range(1, 4)]
    int_1, int_2, int_3 = [random.randrange(-30, 30) for i in range(1, 4)]
    while int_1 * int_2 * int_3 == 0:
      int_1, int_2, int_3 = [random.randrange(-30, 30) for i in range(1, 4)]
    y = symbols('y')
    eq = Eq((y**3 + y_int_1 * y) + (int_1 + y_int_2 *y) - (int_2 - y_int_3 * y), int_3)
    eq_show = Eq(UnevaluatedExpr(y**3 + UnevaluatedExpr(y_int_1 * y)) + UnevaluatedExpr(int_1 + UnevaluatedExpr(y_int_2 *y)) - UnevaluatedExpr(int_2 + UnevaluatedExpr(y_int_3 * y)), int_3)
    task = r'Решите уравнение: \(' +latex(eq_show)+'\)'
    answer = solve(eq, y)
    if len(answer) > 0 and im(solve(eq, y)[0])==0:
      if abs(int(answer[0]) - answer[0]) < 0.000001:
        break
  return task, round(answer[0])

def task_16706():
  '''задача 16706 с портала https://kuzovkin.info/one_exercise_1/16706 Решите уравнение: (x**2−7⋅x−11)−(5⋅x**2−13⋅x−18)=16−4⋅x**2
  осталась нерешенная проблема с раскрытием скобок и урощением выводимого выражения
  '''
  while True:
    x_sq_1, x_sq_2, x_sq_3 = [random.randrange(-10, 10) for i in range(1, 4)]
    while x_sq_1 - x_sq_2 + x_sq_3 != 0 or x_sq_1 * x_sq_2 * x_sq_3 == 0:
      x_sq_1, x_sq_2, x_sq_3 = [random.randrange(-10, 10) for i in range(1, 4)]
    x_int_1, int_1, x_int_2, int_2,  x_int_3, int_3 = [random.randrange(-20, 20) for i in range(1, 7)]
    while x_int_1 * int_1 * x_int_2 * int_2 *  x_int_3 * int_3 == 0:
      x_int_1, int_1, x_int_2, int_2,  x_int_3, int_3 = [random.randrange(-20, 20) for i in range(1, 7)]
    x = symbols('x')
    eq = Eq((x_sq_1 * x**2 + x_int_1 * x + int_1) - (x_sq_2 * x**2 + x_int_2 * x + int_2), int_3 + x_int_3 * x**2)
    eq_show = Eq(UnevaluatedExpr(x_sq_1 * x**2 + x_int_1 * x + int_1) - UnevaluatedExpr(x_sq_2 * x**2 + x_int_2 * x + int_2), int_3 + x_int_3 * x**2)
    task = r'Решите уравнение: \(' +latex(eq_show)+'\)'
    answer = solve(eq, x)
    if len(answer) > 0 and im(solve(eq, x)[0])==0:
      if abs(int(answer[0]) - answer[0]) < 0.000001:
        break
  return task, round(answer[0])

def task_16707():
  '''задача 16707 с портала https://kuzovkin.info/one_exercise_1/16707 Решите уравнение: (y**2−5⋅y**5−19)−(5⋅y**2−6⋅y**5−9)=22−4⋅y**2
  осталась нерешенная проблема с раскрытием скобок и урощением выводимого выражения
  '''
  while True:
    y_sq_1, y_sq_2, y_sq_3 = [random.randrange(-10, 10) for i in range(1, 4)]
    while y_sq_1 - y_sq_2 - y_sq_3 != 0 or y_sq_1 * y_sq_2 * y_sq_3 == 0:
      y_sq_1, y_sq_2, y_sq_3 = [random.randrange(-10, 10) for i in range(1, 4)]
    y_f_1 = random.randrange(-10, 10)
    while y_f_1 ==0:
      y_f_1 = random.randrange(-10, 10)
    y_f_2 = -1 * y_f_1
    int_1, int_2, int_3 = [random.randrange(-30, 30) for i in range(1, 4)]
    while int_1 * int_2 * int_3 == 0:
      int_1, int_2, int_3 = [random.randrange(-30, 30) for i in range(1, 4)]
    y = symbols('y')
    eq = Eq((y_sq_1 * y**2 + y_f_1 * y**5 + int_1) - (y_sq_2 * y**2 + y_f_2 * y**5 + int_2), int_3 + y_sq_3 * y**2)
    eq_show = Eq(UnevaluatedExpr(y_sq_1 * y**2 + y_f_1 * y**5 + int_1) - UnevaluatedExpr(y_sq_2 * y**2 + y_f_2 * y**5 + int_2), int_3 + y_sq_3 * y**2)
    task = r'Решите уравнение: \(' +latex(eq_show)+'\)'
    answer = solve(eq, y)
    if len(answer) > 0:
      if abs(int(answer[0]) - answer[0]) < 0.000001:
        break
  return task, round(answer[0])
