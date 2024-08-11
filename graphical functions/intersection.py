import matplotlib.pyplot as plt
from random import randint
import numpy as np
import math as m
from utilities.converting import save_to_base64
def plot():
  fig = plt.figure(figsize = (7, 7))
  ax = plt.axes()
  fig.add_axes(ax)
  ax.spines[["left", "bottom"]].set_position('zero')
  ax.spines[["top", "right"]].set_visible(False)
  ax.plot(1, 0, ">k", transform=ax.get_yaxis_transform(), clip_on=False)
  ax.plot(0, 1, "^k", transform=ax.get_xaxis_transform(), clip_on=False)
  plt.xticks(np.arange(-30, 30, 1), fontsize=8)
  plt.yticks(np.arange(-30, 30, 1), fontsize=8)
  ax.grid(True)
  arrow_length = 10
  ax.annotate('x', xy=(1, 0), xycoords=('axes fraction', 'data'),
              xytext=(0, arrow_length), textcoords='offset points',
              ha='center', va='bottom')
  ax.annotate('y', xy=(0, 1), xycoords=('data', 'axes fraction'),
              xytext=(arrow_length, 0), textcoords='offset points',
              ha='center', va='bottom')
  return fig, ax

# Задача №509149, №509158, №642371 с сайта https://ege.sdamgia.ru/test?category_id=296&filter=all
def parabola_and_straight():
    fig = plt.figure()
    fig, ax = plot()
    random_task = randint(0, 3)
    while True:
      a = randint(1, 3)
      b = randint(1, 9)
      c = randint(1, 5)
      d = randint(0, 9)
      k = randint(1, 9)
      x = np.linspace(-10, 10, 100)
      y_2 = a * x**2 + b * x + c
      if random_task == 0 or random_task == 1:
        y_1 = 5 * x + 9
        D = (b - 5)**2 - 4 * a *(c - 9)
        if D >= 0:
          x_task_A = ((5 - b) - D**0.5)/(2 * a)
          x_task_B = ((5 - b) + D**0.5)/(2 * a)
          y_task_A = 5 * x_task_A + 9
          y_task_B = 5 * x_task_B + 9
          # Определяем координаты вершины пораболы
          x_v = -b/(2 * a)
          y_v = - (b**2 - 4*a*c)/(4*a)
          if abs(int(x_task_A*1000) - x_task_A*1000) < 0.0001 and abs(int(x_task_B*1000) - x_task_B*1000) < 0.0001 and y_task_B > (20 - abs(int(y_v) - 1)):
              break
      if random_task == 2 or random_task == 3:
        y_1 = k * x + d
        D = (b - k)**2 - 4 * a *(c - d)
        if D > 0:
          x_task_A = ((k - b) - D**0.5)/(2 * a)
          x_task_B = ((k - b) + D**0.5)/(2 * a)
          y_task_A = k * x_task_A + d
          y_task_B = k * x_task_B + d
          # Определяем координаты вершины пораболы
          x_v = -b/(2 * a)
          y_v = - (b**2 - 4*a*c)/(4*a)
          if abs(int(x_task_A*1000) - x_task_A*1000) < 0.0001 and abs(int(x_task_B*1000) - x_task_B*1000) < 0.0001 and y_task_B > (20 - abs(int(y_v) - 1)):
              break

    if random_task == 0:
      task = "На рисунке изображены графики функций $\\f(x)= 5x + 9$ и $\\g(x)= ax^2 + bx +c$, которые пересекаются в точках A и B. Найдите абсциссу точки B."
      answer = x_task_B

    if random_task == 1:
      task = "На рисунке изображены графики функций $\\f(x)= 5x + 9$ и $\\g(x)= ax^2 + bx +c$, которые пересекаются в точках A и B. Найдите ординату точки B."
      answer = y_task_B

    if random_task == 2:
      task = "На рисунке изображены графики функций $\\f(x)= kx + d$ и $\\g(x)= ax^2 + bx +c$, которые пересекаются в точках A и B. Найдите абсциссу точки B."
      answer = x_task_B

    if random_task == 3:
      task = "На рисунке изображены графики функций $\\f(x)= kx + d$ и $\\g(x)= ax^2 + bx +c$, которые пересекаются в точках A и B. Найдите ординату точки B."
      answer = y_task_B

    # Определяем координаты вершины пораболы
    # x_v = -b/(2 * a)
    # y_v = - (b**2 - 4*a*c)/(4*a)

    x_mark_1 = int(x_v) - 2
    x_mark_2 = int(x_v) + 1
    x_mark_3 = int(x_v) + 2
    y_mark_1 = a * x_mark_1**2 + b * x_mark_1 + c
    y_mark_2 = a * x_mark_2**2 + b * x_mark_2 + c
    if random_task == 0 or random_task == 1:
      y_mark_3 = 5 * x_mark_3 + 9
    if random_task == 2 or random_task == 3:
      y_mark_3 = k * x_mark_3 + d
    plt.xlim(-10 + int(x_v), 10 + int(x_v))
    if y_v < (0):
      plt.ylim(int(y_v) - 1, (20 - abs(int(y_v) - 1)))
    else:
      plt.ylim(int(y_v) - 1, (20 - abs(int(y_v) - 1)))
    plt.plot(x, y_1)
    plt.plot(x, y_2, 'g')
    plt.scatter(x_task_A, y_task_A, color='black', marker='p', label = 'A')
    plt.scatter(x_task_B, y_task_B, color='black', marker='p')
    plt.scatter(x_mark_1, y_mark_1, color='blue', marker='p')
    plt.scatter(x_mark_2, y_mark_2, color='blue', marker='p')
    plt.scatter(x_mark_3, y_mark_3, color='blue', marker='p')
    plt.text(x_task_A, (y_task_A + 0.5), 'A', fontsize=20)
    plt_base64 = save_to_base64(plt)
    plt.close()
    return {
        "condition": task,
        "answer": answer,
        "image": plt_base64,
    }

# Задача №509149 и №509158 с сайта https://ege.sdamgia.ru/problem?id=564531
def two_parabolas():
    fig = plt.figure()
    fig, ax = plot()

    while True:
      a = randint(2, 4)
      b = randint(1, 9)
      c = randint(-6, 6)
      x = np.linspace(-10, 10, 100)
      y_1 = x**2 - x - 2
      y_2 = a * x**2 + b * x + c
      D = (b + 1)**2 - 4 * (a - 1) *(c + 2)
      if D >= 0:
        x_task_A = (-(b + 1) - D**0.5)/(2 *(a - 1))
        x_task_B = (-(b + 1) + D**0.5)/(2 *(a - 1))
        y_task_A = x_task_A**2 - x_task_A - 2
        y_task_B = x_task_B**2 - x_task_B - 2
        if abs(int(x_task_A*1000) - x_task_A*1000) < 0.0001 and abs(int(x_task_B*1000) - x_task_B*1000) < 0.0001:
            break

    random_task = randint(0, 1)
    if random_task == 0:
      task = "На рисунке изображены графики функций $\\f(x)= x^2 - x - 2$ и $\\g(x)= ax^2 + bx +c$, которые пересекаются в точках A и B. Найдите абсциссу точки B."
      answer = x_task_B

    if random_task == 1:
      task = "На рисунке изображены графики функций $\\f(x)= x^2 - x - 2$ и $\\g(x)= ax^2 + bx +c$, которые пересекаются в точках A и B. Найдите ординату точки B."
      answer = y_task_B

    # Определяем координаты вершины пораболы
    x_v_1 = 1/2
    y_v_1 = - ((-1)**2 - 4*(-2))/(4)
    x_v_2 = -b/(2 * a)
    y_v_2= - (b**2 - 4*a*c)/(4*a)
    x_v = x_v_2
    y_v = min(y_v_1, y_v_2)
    x_mark_1 = int(x_v_2) - 2
    x_mark_2 = int(x_v_2) + 1
    y_mark_1 = a * x_mark_1**2 + b * x_mark_1 + c
    y_mark_2 = a * x_mark_2**2 + b * x_mark_2 + c
    if y_task_A < y_task_B:
      y_known = y_task_A
      x_known = x_task_A
    else:
      y_known = y_task_B
      x_known = x_task_B

    plt.xlim(-10 + int(x_v), 10 + int(x_v))
    plt.ylim(int(y_v) - 1, (20 - abs(int(y_v) - 1)))
    plt.plot(x, y_1)
    plt.plot(x, y_2, 'g')
    plt.scatter(x_task_B, y_task_B, color='black', marker='p')
    plt.scatter(x_task_A, y_task_A, color='black', marker='p')
    plt.scatter(x_mark_1, y_mark_1, color='blue', marker='p')
    plt.scatter(x_mark_2, y_mark_2, color='blue', marker='p')
    plt.text(x_known, (y_known + 0.5), 'A', fontsize=20)
    plt_base64 = save_to_base64(plt)
    plt.close()
    return {
        "condition": task,
        "answer": answer,
        "image": plt_base64,
    }

# Задача №509167 и №509182 с сайта https://ege.sdamgia.ru/test?category_id=296&filter=all
def giperbola_and_straight():
    fig = plt.figure()
    fig, ax = plot()

    while True:
      a = randint(5, 12)
      b = randint(1, 9)
      k = randint(1, 3)
      x = np.linspace(-10, 10)
      x_g_1 = np.linspace(-10, -0.1)
      x_g_2 = np.linspace(0.1, 10)
      y_g_1 = k / x_g_1
      y_g_2 = k / x_g_2
      y = a * x + b
      D = b**2 - 4 * a * (-k)
      if D >= 0:
        x_task_A = (-b - D**0.5)/(2 * a)
        x_task_B = (-b + D**0.5)/(2 * a)
        y_task_A = a * x_task_A + b
        y_task_B = a * x_task_B + b
        x_mark = randint(-5, 5)
        y_mark = a * x_mark + b
        if abs(int(x_task_A*1000) - x_task_A*1000) < 0.0001 and abs(int(x_task_B*1000) - x_task_B*1000) < 0.0001 and (-10) < y_mark < 10 and y_mark != y_task_A and y_mark != y_task_B and y_task_B >= 10:
            break

    random_task = randint(0, 1)
    if random_task == 0:
      task = "На рисунке изображены графики функций $\\f(x)= \\frac{k}{x}$ и $\\g(x)= ax + b$, которые пересекаются в точках A и B. Найдите абсциссу точки B."
      answer = x_task_B

    if random_task == 1:
      task = "На рисунке изображены графики функций $\\f(x)= \\frac{k}{x}$ и $\\g(x)= ax + b$, которые пересекаются в точках A и B. Найдите ординату точки B."
      answer = y_task_B

    plt.xlim(-10, 10)
    plt.ylim(-10, 10)
    plt.plot(x, y)
    plt.plot(x_g_1, y_g_1, 'g')
    plt.plot(x_g_2, y_g_2, 'g')
    plt.scatter(x_task_A, y_task_A, color='blue', marker='p', label = 'A')
    plt.scatter(x_task_B, y_task_B, color='blue', marker='p')
    plt.scatter(x_mark, y_mark, color='black', marker='p')
    plt.text(x_task_A, (y_task_A + 0.5), 'A', fontsize=20)
    plt_base64 = save_to_base64(plt)
    plt.close()
    return {
        "condition": task,
        "answer": answer,
        "image": plt_base64,
    }
