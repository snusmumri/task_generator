import matplotlib.pyplot as plt
from random import randint
import numpy as np
import math as m
import random
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
  plt.xlim(-10, 10)
  plt.ylim(-10, 10)
  ax.grid(True)
  arrow_length = 10
  ax.annotate('x', xy=(1, 0), xycoords=('axes fraction', 'data'),
              xytext=(0, arrow_length), textcoords='offset points',
              ha='center', va='bottom')
  ax.annotate('y', xy=(0, 1), xycoords=('data', 'axes fraction'),
              xytext=(arrow_length, 0), textcoords='offset points',
              ha='center', va='bottom')
  return fig, ax

#СДАМ ГИА: РЕШУ ЕГЭ. Каталог заданий. Тригонометрические функции https://ege.sdamgia.ru/test?theme=297

def break_line():
  fig = plt.figure()
  fig, ax = plot()
  k = randint(0, 1)
  x = np.linspace(-10, 10, 1000)
  z_list = [-1, 1]
  z = random.choice(z_list)
  if z == -1:
    znak = '-'
  if z == 1:
    znak = '+'
  while True:
    a = randint(1, 9)
    b = randint(1, 9)
    c = randint(1, 9)
    d = randint(1, 9)
    y = a * x + z * abs(b * x + c) + d

    if k == 0:
      target = 'ax + d = 0'
      answer = - d/a
      if abs(int(answer*100) - answer*100) < 0.001:
        break
    if k == 1:
      target = 'bx + c = 0'
      answer = - c/b
      if abs(int(answer*100) - answer*100) < 0.001:
        break

  task = "На рисунке изображен график функции вида $\\f(x)$=$ax "+str(znak)+" |bx + c| + d$, где числа a, b, c, и d - целые. Найдите корень уравнения $"+str(target)+"$."

  if (a * (-12) + z * abs(b * (-12) + c) + d) > (a * (-11) + z * abs(b * (-11) + c) + d):
    k_1 = -(abs(a * (-12) + z * abs(b * (-12) + c) + d) - abs(a * (-11) + z * abs(b * (-11) + c) + d))
  else:
    k_1 = (abs(a * (-12) + z * abs(b * (-12) + c) + d) - abs(a * (-11) + z * abs(b * (-11) + c) + d))
  l_1 = d - c*z
  if (a * (12) + z * abs(b * (12) + c) + d) > (a * (11) + z * abs(b * (11) + c) + d):
    k_2 = abs(a * (12) + z * abs(b * (12) + c) + d) - abs(a * (11) + z * abs(b * (11) + c) + d)
  else:
    k_2 = -(abs(a * (12) + z * abs(b * (12) + c) + d) - abs(a * (11) + z * abs(b * (11) + c) + d))
  l_2 = d + c*z
  if (k_1 - k_2) != 0:
    x_point = (l_2 - l_1)/(k_1 - k_2)
  y_point = a * x_point + abs(b * x_point + c) + d
  if y_point > 8 or y_point < (-7):
    plt.ylim(-10 + y_point , y_point + 10)
  plt.scatter(x_point, y_point, color='blue', marker='p')
  plt.plot(x, y)
  plt_base64 = save_to_base64(plt)
  plt.close()

  return {
      'answer': answer,
      'condition': task,
      'image': plt_base64,
  }

#СДАМ ГИА: РЕШУ ЕГЭ. Каталог заданий. Тригонометрические функции https://ege.sdamgia.ru/problem?id=639948

def break_line_2():
  fig = plt.figure()
  fig, ax = plot()
  x = np.linspace(-10, 10, 1000)
  a = randint(1, 9)
  b = randint(1, 9)
  target = randint(4, 9)
  y = abs(a * x - b)

  answer = abs(a * target - b)
  task = "На рисунке изображен график функции вида $\\f(x)$=$|ax + b|$, где числа a и b - целые. Найдите  значение $f$($"+str(target)+"$)."

  plt.plot(x, y)
  plt_base64 = save_to_base64(plt)
  plt.close()

  return {
      'answer': answer,
      'condition': task,
      'image': plt_base64,
  }
