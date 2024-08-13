import matplotlib.pyplot as plt
from random import randint
import numpy as np
import math as m
from utilities.converting import save_to_base64

# Задача № 564531 с сайта https://ege.sdamgia.ru/problem?id=564531
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

def trigonometria_cos():
    fig = plt.figure()
    fig, ax = plot()

    while True:
      a = randint(1, 9)
      b = randint(1, 4)
      c = randint(1, 60)/24
      d = randint(1, 9)
      x = np.linspace(-3*np.pi, 3*np.pi, 1000, endpoint=True)
      y = a * np.cos(1/b * np.pi * x + np.pi*c) + d
      y_task = randint(a-d, a+d)
      y_max, y_min = 0, 0
      for i in x:
        y_i = a * np.cos(1/b * np.pi * i + np.pi*c) + d
        if y_i > y_max:
          y_max = y_i
        if y_i < y_min:
          y_min = y_i
      try:
        x_task = (m.acos((y_task-d)/a) - np.pi*c)*b / ( np.pi)
      except:
        continue
      if abs(int(x_task*1000) - x_task*1000) < 0.0001:
        if abs(int(b*c)-b*c)<0.0001:
          break
    task = "На рисунке изображен график функции вида $\\f(x)$=$a$ $\\cos$($\\frac{1}{b}\pi x + c) + d$, где $a, b$ и $d$ - целые. Найдите $\\f("+str(int(x_task*1000)/1000)+")$."
    answer = y_task

    plt.xlim(-3*np.pi, 3*np.pi)
    if y_max < 9.9 and y_min > (-9.9):
      plt.ylim(-10, 10)
    if y_max > 10 or y_min < (-10):
      plt.ylim(-10 + int((y_max + y_min)/2), 10 + int((y_max + y_min)/2))
    plt.plot(x, y)
    plt_base64 = save_to_base64(plt)
    plt.close()
    return {
        "condition": task,
        "answer": answer,
        "image": plt_base64,
    }