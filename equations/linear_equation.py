import random
import numpy as np
from sympy import symbols, Eq, solve, latex

def task_16515():
  '''задача 16515 с портала https://kuzovkin.info/one_exercise_1/16515 Решите уравнение: 10⋅x2−(2⋅x−3)⋅(5⋅x−1)=31'''
  answer = [1.2345667]
  while abs(int(answer[0]) - answer[0]) > 0.000001:
    x_int_1, x_int_2, int_1, int_2  = np.random.randint(1, 30, size=4)
    eq_ans = random.randint(1, 300)
    x = symbols('x')
    eq = Eq(x_int_1 * x_int_2 * x**2 - (x_int_1 * x - int_1) * (x_int_2 * x - int_2), eq_ans)
    task = r'Решите уравнение: \(' +latex(eq)+'\)'
    answer = solve(eq, x)
  return task, round(answer[0])


def task_16616():
  '''задача 16616 (и аналогичные) с портала https://kuzovkin.info/one_exercise_1/16616 Решите уравнение: (x−2)⋅(x−3)=(x+2)⋅(x−5)'''
  answer = [1.2345667]
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
